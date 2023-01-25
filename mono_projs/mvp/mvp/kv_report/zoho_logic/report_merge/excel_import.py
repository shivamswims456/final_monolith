import os, csv
from kv_report.zoho_logic import login
from kv_report.models import kv_creds, tran_psve, tran_orders
from django.conf import settings

SESSION = login.get_login()

basePath = os.path.join(settings.BASE_DIR, 'kv_report', 'zoho_logic', 'report_merge', 'excels')

billPath = os.path.join(basePath, 'bills.csv')
invPath = os.path.join(basePath, 'adj.csv')
tranPath = os.path.join(basePath, 'trans.csv')
itemMaster = os.path.join(basePath, 'items.csv')



def item_import():

    with open(itemMaster, 'r', encoding="utf8") as f:

        items = list(csv.reader(f))


    item_index = []


    for _ in ['Item ID','Opening Stock','Purchase Price', 'Warehouse Name']:

        try:

            item_index.append(items[0].index(_))


        except:

            item_index.append(None)


    for item in items[1:]:

        tp = tran_psve()

        tp.item_id = item[item_index[0]]
        tp.qty_inwards = item[item_index[1]] if item[item_index[1]] != "" else 0
        tp.cost_price = float(item[item_index[2]].split(" ")[1])
        tp.warehouse_id = item[item_index[3]]
        tp.date = "2000-01-01"        

        tp.save()


    




def from_db():

    creds = kv_creds.objects.all()[:1].get()

    return creds



def import_db():

    entries = psve_entries()

    for entry in entries:

        if float(entry[1]) > 0 and entry[0] != "":

            tran = tran_psve()

            tran.item_id = entry[0]
            tran.qty_inwards = entry[1]
            tran.cost_price = entry[2]
            tran.date = entry[3]
            tran.warehouse_id = entry[4]

            tran.save()




def psve_entries():

    adj_indexes = []
    bill_indexes = []

    psve_entries = []


    with open(invPath, "r", encoding="utf8") as f:

        adj_lists = list(csv.reader(f))


    with open(billPath, "r", encoding="utf8") as f:

        bill_lists = list(csv.reader(f))

    
    for _ in ["Item ID", "Quantity Adjusted", "Cost Price", "Date", "Warehouse Name"]:

        try:

            adj_indexes.append(adj_lists[0].index(_))

        except:

            adj_indexes.append(None)

    
    for _ in ["Product ID", "Quantity", "Rate", "Bill Date", "No Ware House"]:


        try:

            bill_indexes.append(bill_lists[0].index(_))

        except:

            bill_indexes.append(None)



    for row in adj_lists[1:]:

        temp = []

        

        for _ in adj_indexes:

            
            if _ != None:

                temp.append(row[_])

            else:

                temp.append(None)
        

        psve_entries.append(temp)


    for row in bill_lists[1:]:

        temp = []

        for _ in bill_indexes:

            if _ != None:

                temp.append(row[_])

            else:

                temp.append(None)

        psve_entries.append(temp)

    
    return psve_entries

    

def import_trans():

    with open(tranPath, 'r', encoding="utf8") as f:

        entries = list(csv.reader(f))

    field_indexes = []

    for each in ['Date','Transfer Order#','Status','Item Name','Product ID','Quantity Transferred','Cost Price','From Warehouse Name','To Warehouse Name']:

        try:

            field_indexes.append(entries[0].index(each))

        except:

            field_indexes.append(None)




    for entry in entries[1:]:


        to = tran_orders()

        to.date = entry[field_indexes[0]]
        to.transfer_order = entry[field_indexes[1]]
        to.status = entry[field_indexes[2]]
        to.item_Name = entry[field_indexes[3]]
        to.product_id = entry[field_indexes[4]]
        to.quantity_transferred = entry[field_indexes[5]]
        to.cost_price = entry[field_indexes[6]]
        to.from_warehouse_name = entry[field_indexes[7]]
        to.to_warehouse_name = entry[field_indexes[8]]

        to.save()


def get_trans():

    creds = from_db()

    SESSION.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})

    csvTransRequest = SESSION.get(f'https://inventory.zoho{creds.zoho_org_domain}/api/v1/export?entity=transfer_order&accept=csv&async=false&status=all&export_template_id=&includebatchdetails=false&includeserialnumbers=false&x-zb-source=zbclient&organization_id={creds.zoho_org_id}&frameorigin=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}')



    with open(tranPath, 'wb') as f:

        f.write(csvTransRequest.content)


def item_stock():

    creds = from_db()

    SESSION.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
    itemCSVRequest = SESSION.get(f'https://inventory.zoho{creds.zoho_org_domain}/api/v1/export?entity=item&accept=csv&async=false&status=all&can_export_pii_fields=false&export_template_id=&includebatchdetails=false&includeserialnumbers=false&x-zb-source=zbclient&organization_id={creds.zoho_org_id}&frameorigin=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}')

    with open(itemMaster, 'wb') as f:

        f.write(itemCSVRequest.content)


def get_csv():


    creds = from_db()


    SESSION.headers.update({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})

    csvBillRequest = SESSION.get(f'https://inventory.zoho{creds.zoho_org_domain}/api/v1/export?entity=bill&accept=csv&async=false&status=all&can_export_pii_fields=false&export_template_id=&includebatchdetails=false&includeserialnumbers=false&x-zb-source=zbclient&organization_id={creds.zoho_org_id}&frameorigin=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}')

    csvAdjRequest = SESSION.get(f'https://inventory.zoho{creds.zoho_org_domain}/api/v1/export?entity=inventory_adjustment&accept=csv&async=false&status=all&export_template_id=&includebatchdetails=false&includeserialnumbers=false&x-zb-source=zbclient&organization_id={creds.zoho_org_id}&frameorigin=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}')


    with open(invPath, "wb") as f:

        f.write(csvAdjRequest.content)



    with open(billPath, "wb") as f:

        f.write(csvBillRequest.content)


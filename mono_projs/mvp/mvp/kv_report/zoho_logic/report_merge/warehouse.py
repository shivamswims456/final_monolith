from kv_report.zoho_logic import login
import json, os, time
from django.conf import settings
from kv_report.models import warehouse_total, kv_creds

SESSION = login.get_login()




def from_db():

    creds = kv_creds.objects.all()[:1].get()

    return creds





def insertReport():

    storePath = os.path.join(settings.BASE_DIR, 'kv_report', 'zoho_logic', 'report_merge', 'warehouse_summary.json')

    with open(storePath, 'r') as f:
        
        data = json.load(f)


    for each in data[0]:

        item_id = each.get('item_id')

        for warehouse in each.get("warehouses"):

            wt = warehouse_total(
                    item_id = item_id,
                    warehouse_status = warehouse.get('warehouse_status'),
                    quantity_sold = warehouse.get('quantity_sold'),
                    quantity_ordered = warehouse.get('quantity_ordered'),
                    warehouse_name = warehouse.get('warehouse_name'),
                    is_primary_warehouse = warehouse.get('is_primary_warehouse'),
                    quantity_available_for_sale = warehouse.get('quantity_available_for_sale'),
                    quantity_demanded = warehouse.get('quantity_demanded'),
                    quantity_purchased = warehouse.get('quantity_purchased'),
                    warehouse_id = warehouse.get('warehouse_id'),
                    quantity_available = warehouse.get('quantity_available'))

            wt.save()








def getWarehouseReport(filterMap="TransactionDate.ThisMonth", start_date=None):

    print("good")


    storePath = os.path.join(settings.BASE_DIR, 'kv_report', 'zoho_logic', 'report_merge', 'warehouse_summary.json')


    creds = from_db()


    reportUrl = lambda pageNumber: f'https://inventory.zoho.in/api/v1/reports/warehouse?page={pageNumber}&per_page=500&sort_column=item_name&sort_order=A&response_option=1&filter_by={filterMap}&show_actual_stock=false&organization_id={creds.zoho_org_id}'
    
    if start_date != None:

        reportUrl = lambda pageNumber: f'https://inventory.zoho.in/api/v1/reports/warehouse?page={pageNumber}&per_page=500&sort_column=item_name&sort_order=A&response_option=1&filter_by=TransactionDate.CustomDate&show_actual_stock=false&to_date={start_date}&organization_id={creds.zoho_org_id}'

    

    

    page = 1

    store = []


    while True:

        resp = SESSION.get(reportUrl(page))

        time.sleep(3)

        print("sleeping")

        print(resp.status_code)

        if resp.status_code == 200:

            warehouseReport = resp.json()

            store.append(warehouseReport.get("warehouse_stock_info"))

            print(warehouseReport.get("warehouse_stock_info")[0], warehouseReport.get("page_context").get("has_more_page"))

            
            if not warehouseReport.get("page_context").get("has_more_page"):

                break

        else:

            break

        page += 1


            


    with open(storePath, "w") as f:

        json.dump(store, f, indent=4)





    








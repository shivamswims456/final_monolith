from kv_report.zoho_logic import login
import json, os, time
from django.conf import settings
from kv_report.zoho_logic.login import from_db
from math import ceil
from kv_report.models import transactions_psve, bill_fetches


SESSION = login.get_login()




def get_psve_adjustments(adj_no_list, org_id):

    pass


def get_adjustments():

    creds = from_db()


    get_adj_counts = lambda:SESSION.get(f'https://inventory.zoho.in/api/v1/inventoryadjustments?page=1&per_page=25&filter_by=AdjustmentDate.All%2CAdjustmentType.All&sort_column=created_time&sort_order=D&response_option=2&organization_id={creds.zoho_org_id}')







def get_bill_details(bill_no_list, org_id):

    bill_no_list = bills_filter(bill_no_list)
    

    for bill_no in bill_no_list:

        PREVIOUS_HEADER = SESSION.headers

        SESSION.headers.update({'Accept': '*/*',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Connection': 'keep-alive',
                                'Host': 'inventory.zoho.in',
                                'Referer': f'https://inventory.zoho.in/app/{org_id}',
                                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-ZB-Asset-Version': 'Jan_06_2023_2_564',
                                'X-ZB-SOURCE': 'zbclient',
                                'X-ZOHO-Include-Formatted': 'true'})

        
        bill_data = SESSION.get(f"https://inventory.zoho.in/api/v1/bills/{bill_no}?organization_id={org_id}").json().get("bill")


        bill_date = bill_data.get("date")

        bill_id = bill_data.get("bill_id")


        for line_item in bill_data.get  ("line_items"):

            item_id = line_item.get("item_id")

            if item_id != "":

                tsve = transactions_psve()

                tsve.bill_id = bill_id
                tsve.type = "bill"
                tsve.bill_date = bill_date
                tsve.bill_item = item_id
                tsve.item_name = line_item.get("name")
                tsve.item_qty = line_item.get("quantity")
                tsve.item_total = line_item.get("item_total")

                tsve.save()

        

        bf = bill_fetches()
        bf.bill_id = bill_no
        bf.bill_date = bill_data.get("created_time")
        bf.save()
        time.sleep(1.3)
        print(bill_no, "crossed")



        



def bills_filter(to_fetch):

    fetchingLeft = set(to_fetch) - set([each.bill_id for each in bill_fetches.objects.all()])


    return fetchingLeft







def get_bills():

    
    creds = from_db()
    

    get_total_bill_count = lambda:SESSION.get(f"https://inventory.zoho.in/api/v1/bills?page=1&per_page=200&filter_by=Status.All&sort_column=created_time&sort_order=D&response_option=2&organization_id={creds.zoho_org_id}").json().get("page_context").get("total")

    get_bill_page = lambda page: SESSION.get(f'https://inventory.zoho.in/api/v1/bills?page={page}&per_page=200&filter_by=Status.All&sort_column=date&sort_order=A&usestate=true&organization_id={creds.zoho_org_id}').json()
                                               

    
    billsLeft = get_total_bill_count()
    
    pagesLeft = ceil(billsLeft/200)


    
    for page in range(1, pagesLeft + 1):
        
        pageData = get_bill_page(page)
       
        bills = pageData.get("bills")

        bill_list = []

        for _bill_ in bills:

            bill_list.append(_bill_.get('bill_id'))


        get_bill_details(bill_list, creds.zoho_org_id)

        print(page)
        time.sleep(1.5)



        


    






    
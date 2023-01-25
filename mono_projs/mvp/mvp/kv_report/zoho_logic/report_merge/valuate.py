import json, csv
import os
from kv_report.models import tran_psve, tran_orders
from django.conf import settings
from datetime import date, timedelta, datetime
from django.db.models import Q

warehouse_file = os.path.join(settings.BASE_DIR, 'kv_report', 'zoho_logic', 'report_merge', 'warehouse_summary.json')






def calculate_ind(price_qty_map, qty):

    tp = 0
    
    for chunk in price_qty_map:

        if qty >= chunk[0]:

            tp += chunk[0] * chunk[1]

            qty -= chunk[0]

        elif qty < chunk[0]:

            tp += qty * chunk[1]

            break

        if qty <= 0:

            break

        print(chunk, qty, tp)
    

    return tp 


def get_warehouse(warehouse_search='Main Store'):

    with open("warehouse_valuation.json", 'r') as f:

        items = json.load(f)


    csv_rows = []

    for item_chunk in items:

        for item in item_chunk:

            for warehouse in item.get("warehouses"):

                warehouse_name = warehouse.get("warehouse_name")

                if warehouse_name == warehouse_search and not item.get('is_combo_product'):

                    csv_rows.append([item.get("item_name"), item.get("unit"), warehouse.get('quantity_available'),  warehouse.get('quantity_purchased'), warehouse.get('quantity_sold'), warehouse.get('quantity_available_for_sale'), warehouse.get('valuation')])


    with open(f'{warehouse_search}.csv', 'w', newline='', encoding='utf-8') as f:

        writer = csv.writer(f)

        writer.writerow(["Item Name", "Unit", "Qunatity Available", "Quantity Purcahsed", "Qunatity Sold", "Qunatity Avaialble for sale", "Valuation"])

        writer.writerows(csv_rows)





    


def valuate(warehouse, item_id, last_qty = 0, period_from = datetime.now() - timedelta(days = 30), period_to = datetime.now() - timedelta(days = 1)):

    
    
    price_qty_map = []


    if warehouse == "Main Store":

        wq = Q(warehouse_id=warehouse) | Q(warehouse_id=None)
    

        trans = tran_psve.objects.filter(Q(item_id=item_id) & wq & Q(date__lte=period_to)).order_by('-date')

        for each in trans:

            price_qty_map.append([each.qty_inwards, each.cost_price])

    else:

        wq = Q(to_warehouse_name=warehouse)

        trans = tran_orders.objects.filter(Q(product_id=item_id) & wq & Q(date__lte=period_to)).order_by('-date')

        for each in trans:

            price_qty_map.append([each.quantity_transferred, each.cost_price])

    
    


    return calculate_ind(price_qty_map=price_qty_map, qty=last_qty)





def get_items():

    with open(warehouse_file, 'r') as f:

        item_store = json.load(f)


    item_map = {}

    print("item_store", len(item_store))

    for item_chunk in item_store:

        print("item_chunk", len(item_chunk))
        
        for item in item_chunk:

            item_id = item.get("item_id")

            for box in item.get("warehouses"):


                box_name = box.get("warehouse_name")
                last_qty = box.get('quantity_available')

                
                box.update({"valuation":valuate(warehouse=box_name, item_id=item_id, last_qty=last_qty, period_to=datetime(2022, 12, 31))})

            
            
            item_map.update(item)

    print("readyTowrite", len(item_map))

    with open("warehouse_valuation.json", "w") as f:

        json.dump(item_store, f, indent=4)









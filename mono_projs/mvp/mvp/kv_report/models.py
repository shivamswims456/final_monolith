from django.db import models

# Create your models here.




class warehouse_total(models.Model):

    item_id = models.PositiveBigIntegerField()
    warehouse_status = models.TextField(max_length=30)
    quantity_sold = models.FloatField()
    quantity_ordered = models.FloatField()
    warehouse_name = models.TextField(max_length=150)
    is_primary_warehouse = models.BooleanField()
    quantity_available_for_sale = models.FloatField()
    quantity_demanded = models.FloatField()
    quantity_purchased = models.FloatField()
    warehouse_id = models.PositiveBigIntegerField()
    quantity_available = models.FloatField()







class tran_orders(models.Model):

    date = models.DateField()
    transfer_order = models.TextField(max_length=30)
    status = models.TextField(max_length=30)
    item_Name = models.TextField(max_length=150)
    product_id = models.PositiveBigIntegerField()
    quantity_transferred = models.FloatField()
    cost_price = models.FloatField()
    from_warehouse_name = models.TextField(max_length=150)
    to_warehouse_name = models.TextField(max_length=150)





class tran_psve(models.Model):

    item_id = models.PositiveBigIntegerField()
    qty_inwards = models.FloatField()
    cost_price = models.FloatField()
    type = models.TextField(max_length=30)
    warehouse_id = models.TextField(max_length=150, blank=True, null=True)
    date = models.DateTimeField()




class kv_creds(models.Model):

    zoho_user_name = models.EmailField()
    zoho_user_pwd = models.TextField(max_length=30)
    zoho_org_id = models.TextField(max_length=100)
    zoho_org_domain = models.TextField(max_length=10, default=".in")
    zoho_item_export_template = models.PositiveBigIntegerField()

    

    def __str__(self):

        return self.zoho_user_name
from sdks.django.utility import multiModel
from ECOM_users.models import ECOM_model_register, ECOM_registers
from ECOM_pincodes.helpers import vendors_pincode_table


def remove_ECOM_super_vendors_pincode_table(django_user_obj):

    """
        @django_user_obj: (django_user_obj)
        multiModel models creates database only once  
    """

    db_register_name = "ECOM_pincodes"
    db_register_obj = ECOM_registers.objects.get(name=db_register_name)

    mm = vendors_pincode_table(django_user_obj.username)
    mm_model = mm.get()
    mm_fake= vendors_pincode_table(django_user_obj.username, fake=True)
    mm_fake_model = mm_fake.get()

    ECOM_model_register.objects.get(name=mm_model._meta.db_table,
                                    register=db_register_obj,
                                    user=django_user_obj).delete()

    ECOM_model_register.objects.get(name=mm_fake_model._meta.db_table,
                                    register=db_register_obj,
                                    user=django_user_obj).delete()
    
    mm.remove()
    mm_fake.remove()


def create_ECOM_super_vendors_pincode_table(django_user_obj):

    """
        @django_user_obj: (django_user_obj)
        multiModel models creates database only once  
    """

    db_register_name = "ECOM_pincodes"
    db_register_obj = ECOM_registers.objects.get(name=db_register_name)

    mm = vendors_pincode_table(django_user_obj.username).get()
    mm_fake = vendors_pincode_table(django_user_obj.username, fake=True).get()
    
    ECOM_model_register.objects.get_or_create(name=mm._meta.db_table,
                                              register=db_register_obj,
                                              user=django_user_obj)
    
    ECOM_model_register.objects.get_or_create(name=mm_fake._meta.db_table,
                                              register=db_register_obj,
                                              user=django_user_obj)
    



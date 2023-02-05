from ECOM_users.models import user_addition_instruction, ECOM_super_vendors
from ECOM_users import instrunctions
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model

um = get_user_model()
@receiver(m2m_changed, sender=um.groups.through)
def follow_instrunctions(**kwargs):

    """
        always group should be added to user,
        USER SHOULD NOT BE ADDED TO GROUP
    """

    inst_set = []


    for inst in user_addition_instruction.objects.filter(
        group__id__in = kwargs["pk_set"]
    ):
        action_instrunctions = []

        if kwargs["action"] == "post_add":

            action_instrunctions = inst.instruction
        
        elif kwargs["action"] == "post_remove":

            action_instrunctions = inst.remove_instructions
            
            
        for each in action_instrunctions:
            getattr(instrunctions, each)(kwargs["instance"])
    
from django.contrib import admin
from .models import info_user

# Register your models here.
@admin.register(info_user)
class admin_user_info(admin.ModelAdmin):
    list_display=["id",'name_pc',"processor"]
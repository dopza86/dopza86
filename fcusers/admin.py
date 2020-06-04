from django.contrib import admin
from .models import Fcusers

# Register your models here.


class FcusersAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "registerd_dttm")


admin.site.register(Fcusers, FcusersAdmin)

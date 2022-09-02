from django.contrib import admin
from.models import mydata
# Register your models here.


@admin.register(mydata)
class adminmydata(admin.ModelAdmin):
    list_display = ["published"]
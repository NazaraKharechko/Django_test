from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import UsersModel, OrdersModel, Person

admin.site.register(UsersModel)
admin.site.register(OrdersModel)


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

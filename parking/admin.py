from django.contrib import admin
from .models import (Vehicle, Cell, cell_has_vehicle)

# Register your models here.
class Vehicles(admin.ModelAdmin):
    """ admin para los tipos de documento """

    list_filter = ('type_vehicle',)
    search_fields = ('employee__name', 'vehicle_registration_number',)
    list_display = ['id', 'employee', 'type_vehicle', 'cylinder_capacity', 'gears', 'vehicle_model',
                    'doors_number', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = Vehicle


class Cells(admin.ModelAdmin):
    """ admin para los tipos de documento """

    list_filter = ('type_cell', 'status',)
    search_fields = ('name',)
    list_display = ['id', 'type_cell', 'name',  'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = Cell


class cell_has_vehicles(admin.ModelAdmin):
    """ admin para los tipos de documento """

    list_filter = ('cell', 'status',)
    search_fields = ('vehicle__vehicle_registration_number', 'cell__name')
    list_display = ['id', 'cell', 'employee', 'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = cell_has_vehicle

admin.site.register(Vehicle, Vehicles)
admin.site.register(Cell, Cells)
admin.site.register(cell_has_vehicle, cell_has_vehicles)
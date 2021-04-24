from django.urls import path

from .views import *

urlpatterns = [
  path('vehicles/list', VehiclesList.as_view(), name='vehicles_list'),
  path('vehicles/new', VehiclesCreateView.as_view(), name='vehicles_new'),
  path('vehicles/update/<int:pk>', VehiclesUpdateView.as_view(), name='vehicles_update'),
  path('vehicles/delete/<int:pk>', VehiclesDeleteView.as_view(), name='vehicles_delete'),

  path('vehicles/new/admin', VehiclesAdminCreateView.as_view(), name='vehicles_new_admin'),
  path('vehicles/update/admin/<int:pk>', VehiclesAdminUpdateView.as_view(), name='vehicles_update_admin'),
  path('vehicles/detail/<int:pk>', VehicleDetailView.as_view(), name='vehicle_detail'),

  path('cell/update/enable/<int:pk>', cell_enable, name='cell_enable'),
  path('cell/list', CellsListView.as_view(), name='cell_list'),
  path('cell/new', CellsCreateView.as_view(), name='cell_new'),
  path('cell/update/<int:pk>', CellsUpdateView.as_view(), name='cell_update'),
  path('cell/delete/<int:pk>', CellDeleteView.as_view(), name='cell_delete'),
  path('cell/select/vehicle/<int:pk>', DetailSelectVehicle.as_view(), name='cell_select'),
  path('cell/select/assing/<int:pk_cell>/<int:pk_vehicle>', cell_assign_vehicle, name='cell_assign'),

]

#django
from django.urls import path

#views
from .views import *

urlpatterns = [
  path('employees/list', EmployeList.as_view(), name='employees_list'),
  path('employees/new',EmployeCreateView.as_view(), name='employees_new'),
  path('employees/update/<int:pk>',EmployeUpdateView.as_view(), name='employees_update'),
  path('employees/delete/<int:pk>',EmployeDeleteView.as_view(), name='employees_delete'),

]
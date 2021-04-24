from django.views.generic import (ListView)
from django.shortcuts import render, redirect

from datetime import datetime, timedelta

from django.db.models import Count, Q, Case, When, Value, IntegerField, Prefetch, Sum
from django.db.models.functions import TruncDay

from django.contrib.auth.mixins import (LoginRequiredMixin)

from parking.models import Cell, cell_has_vehicle, Vehicle
from employees.models import User

# Create your views here.
class Home(LoginRequiredMixin, ListView):
    """ vista basada en clase para el home del conserje """
    model = Cell
    template_name = "base/home.html"
    context_object_name = "cells"

    def get_queryset(self):
        queryset = self.model.objects.\
            filter(deleted_at =None, status=True).\
            annotate(num_vehicles=Count('vehicles', filter=Q(deleted_at=None, cell_has_vehicle__status=True)))
        return queryset


    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        user_type = self.request.user.type_user
        if user_type == '3':
            return redirect("vehicles_list")
        context = self.get_context_data()
        return self.render_to_response(context)


class Report(LoginRequiredMixin, ListView):
    model = cell_has_vehicle
    template_name = "reports/report.html"
    context_object_name = "cells"

    def get_queryset(self):
        last_month = datetime.today() - timedelta(days=30)
        queryset = self.model.objects.values('employee__id','created_at__month','employee__name').\
                                            filter(status=False, created_at__gte=last_month).annotate(data_sum=Count('id'))
           
        return queryset

   
     
                 
                    
                    

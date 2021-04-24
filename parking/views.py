# utils
import sys
from django.utils import timezone
from django.utils import timezone as tz

# Django
from django.views.generic import (ListView, CreateView, UpdateView, DetailView ,DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin )
from django.urls import (reverse_lazy)
from django.shortcuts import render, redirect
from django.db import transaction
from django.db.models import Q

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.urls import reverse

#import models
from .models import Vehicle, Cell, cell_has_vehicle
from employees.models import User

# Forms
from .forms import (VehiclesForm, VehiclesForm2, CellForm, SearchForm, CellHasVehicleForm)

# Create your views here.
class VehiclesList(LoginRequiredMixin, ListView):
    """ vista para listar los vehiculos """
    
    permission_required = "parking.view_vehicle"
    model = Vehicle
    template_name = "vehicles/list_vehicles.html"
    context_object_name = "vehicles"

    # se listan los vehiculos que no esten eliminados
    # El empleado solo puede ver sus vehiculos registrados
    def get_queryset(self):
        user = self.request.user.id
        type_user = self.request.user.type_user
        if type_user == '3':
            queryset = self.model.objects.filter(employee = user, deleted_at = None)
        else:
            queryset = self.model.objects.filter(deleted_at = None)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos'
        context['create_url'] = reverse_lazy("vehicles_new")
        return context

# Crear Vehiculos
class VehiclesCreateView(LoginRequiredMixin, CreateView):
    permission_required="parking.add_vehicle"
    model = Vehicle
    template_name="vehicles/form_vehicles.html"
    context_object_name = "obj"
    form_class = VehiclesForm
    success_url = reverse_lazy("vehicles_list")
    success_message = "Registro Creado Satisfactoriamente"

    # se le agrega el usuario que esta creando el vehiculo
    def form_valid(self, form):
        form_pre_save = form.save(commit=False)
        user = User.objects.filter(pk=self.request.user.id).first()
        form_pre_save.employee = user
        form_pre_save.save()
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos'
        context['list_url'] = self.success_url
        return context

# Crear Vehiculos por el ADMIN o CONCERJE
class VehiclesAdminCreateView(LoginRequiredMixin, CreateView):
    permission_required="parking.add_vehicle"
    model = Vehicle
    template_name="vehicles/form_vehicles.html"
    context_object_name = "obj"
    form_class = VehiclesForm2
    success_url = reverse_lazy("vehicles_list")
    success_message = "Registro Creado Satisfactoriamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos Admin'
        context['list_url'] = self.success_url
        return context


# Actualizar Vehiculos
class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    permission_required="parking.change_vehicle"
    model = Vehicle
    template_name="vehicles/form_vehicles.html"
    context_object_name = "obj"
    form_class = VehiclesForm
    success_url = reverse_lazy("vehicles_list")
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form_pre_save = form.save(commit=False)
        form_pre_save.updated_at = timezone.now()
        form_pre_save.save()
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos'
        context['list_url'] = self.success_url
        return context                   

# Actualizar Vehiculos Admin concerje
class VehiclesAdminUpdateView(LoginRequiredMixin, UpdateView):
    permission_required="parking.change_vehicle"
    model = Vehicle
    template_name="vehicles/form_vehicles.html"
    context_object_name = "obj"
    form_class = VehiclesForm2
    success_url = reverse_lazy("vehicles_list")
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form_pre_save = form.save(commit=False)
        form_pre_save.updated_at = timezone.now()
        form_pre_save.save()
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos'
        context['list_url'] = self.success_url
        return context     

# Eliminar Vehiculo este eliminado es logico.
class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    context_object_name = "vehicle"
    template_name = 'cells/view_vehicle_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entradas = self.object.cell_has_vehicle_set.all()
        entradas = entradas.filter(deleted_at=None)
        context['entradas'] = entradas
        return context 


# Eliminar Vehiculo este eliminado es logico.
class VehiclesDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    permission_required="parking.delete_vehicle"
    template_name="vehicles/delete_vehicles.html"
    success_url = reverse_lazy("vehicles_list")

    def delete(self, request, *args, **kwargs):
        # se obtiene la instancia y se elimina logicamente
        vehi = self.get_object()
        vehi.status = False
        vehi.deleted_at = timezone.now()
        vehi.save()
        return redirect("vehicles_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Vehiculos'
        context['list_url'] = self.success_url
        return context


class DetailSelectVehicle(LoginRequiredMixin, DetailView):
    """ vista para ver detalle de un post """

    model = Cell
    context_object_name = "cell"
    template_name = 'cells/select_vehicle.html'
    form_class = CellHasVehicleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #filtro para buscar por numero de matricula, nombre o documento del empleado
        search = self.request.GET or None
        query = Vehicle.objects.filter(deleted_at=None)
        if search:
            search = search['search'] or None
            if search:
                query = query.filter(Q(vehicle_registration_number__icontains=search) |
                                    Q(employee__name__icontains=search) |
                                    Q(employee__document__icontains=search))
        
        context['vehicles'] = query
        context['SearchForm'] = SearchForm
        return context


@login_required(login_url="/login")
def cell_assign_vehicle(request, pk_cell, pk_vehicle):
    """ vista basada en funcion para habilitar celda"""

    try:
        cell = Cell.objects.get(pk=pk_cell)

        context={}
        template_name = "cells/enable_cell.html"

        if request.method == 'GET':
            vehicle = Vehicle.objects.get(pk=pk_vehicle)
            # se verifica si ya tienen un vehiculo o una celda respectivamente
            cell_has_vehicle_exists = cell_has_vehicle.objects.filter(deleted_at=None, status=True, cell=cell).exists()
            vehicle_has_cell_exists = cell_has_vehicle.objects.filter(deleted_at=None, status=True, vehicle=vehicle).exists()
            if cell_has_vehicle_exists or vehicle_has_cell_exists:
                context={'obj':cell, "title":"Ocupar", "message":"El vehiculo o la celda ya estan ocupados", "form_status":False}
            else:
                context={'obj':cell, "title":"Ocupar", "message":False, "form_status":True}
            return render(request, template_name, context)

        if request.method == 'POST':
            # se obtiene la celda y el vehiculo
            vehicle = Vehicle.objects.get(pk=pk_vehicle)

            # se verifica si ya tienen un vehiculo o una celda respectivamente
            cell_has_vehicle_exists = cell_has_vehicle.objects.filter(deleted_at=None, status=True, cell=cell).exists()
            vehicle_has_cell_exists = cell_has_vehicle.objects.filter(deleted_at=None, status=True, vehicle=vehicle).exists()
            if cell_has_vehicle_exists or vehicle_has_cell_exists:
                context={'obj':cell, "title":"Ocupar", "message":"El vehiculo o la celda ya estan ocupados"}
                return render(request, template_name, context)
            else:
                if cell.type_cell == vehicle.type_vehicle:
                    employe = User.objects.get(pk = vehicle.employee.id)
                    cell_has_vehicle.objects.create(vehicle=vehicle,cell=cell, status=True, employee=employe)
                    return redirect('home')
                else:
                    context={'obj':cell, "title":"Ocupar", "message":"Esta casilla no es para este tipo de vehiculo"}
                    return render(request, template_name, context)

    except Exception:
        return render(request, template_name, context)

    return render(request, template_name, context)


@login_required(login_url="/login")
def cell_enable(request, pk):
    """ vista basada en funcion para habilitar celda"""

    try:
        cell = Cell.objects.get(pk = pk)
        
        context={}
        template_name = "cells/enable_cell.html"
        
        if request.method == 'GET':
            context={'obj':cell, "title":"Desocupar", "message":False, "form_status":True}
        
        if request.method == 'POST':
            # se valida si la celda esta ocupada
            cell_has_vehicle_exists = cell_has_vehicle.objects.filter(deleted_at=None, status=True, cell=cell).exists()
            if cell_has_vehicle_exists:
                # si esta ocupada dar salida al vehiculo cambiando el estado de la relacion
                cell_has_vehicle.objects.filter(status=True, cell=cell.id).update(status=False, updated_at=timezone.now())
            return redirect("home")
            
    except Exception:
        return render(request, template_name, context)

    return render(request, template_name, context)


# Listar Celdas
class CellsListView(LoginRequiredMixin, ListView):
    """ vista para listar las celdas """
    
    permission_required = "parking.view_cell"
    model = Cell
    template_name = "cells/list_cells.html"
    context_object_name = "cells"

    # se listan las celdas que no esten eliminados
    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at = None)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Celdas'
        context['create_url'] = reverse_lazy("cell_new")
        return context    


# Crear celdas
class CellsCreateView(LoginRequiredMixin, CreateView):
    permission_required="parking.add_cell"
    model = Cell
    template_name = "cells/form_cell.html"
    context_object_name = "obj"
    form_class = CellForm
    success_url = reverse_lazy("cell_list")
    success_message = "Registro Creado Satisfactoriamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Celda'
        context['list_url'] = self.success_url
        return context


# Actualizar Celdas
class CellsUpdateView(LoginRequiredMixin, UpdateView):
    permission_required="parking.change_cell"
    model = Cell
    template_name = "cells/form_cell.html"
    context_object_name = "obj"
    form_class = CellForm
    success_url = reverse_lazy("cell_list")
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form_pre_save = form.save(commit=False)
        form_pre_save.updated_at = timezone.now()
        form_pre_save.save()
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Celda'
        context['list_url'] = self.success_url
        return context     

# Eliminar Celda este eliminado es logico.
class CellDeleteView(LoginRequiredMixin, DeleteView):
    model = Cell
    permission_required="parking.delete_cell"
    template_name = "cells/delete_cell.html"
    success_url = reverse_lazy("cell_list")

    def delete(self, request, *args, **kwargs):
        # se obtiene la instancia y se elimina logicamente
        obj = self.get_object()
        obj.status = False
        obj.deleted_at = timezone.now()
        obj.save()
        return redirect("cell_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Celda'
        context['list_url'] = self.success_url
        return context        
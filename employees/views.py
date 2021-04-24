# utils
from django.utils import timezone
from django.utils import timezone as tz

#django
from django.contrib.auth.mixins import (LoginRequiredMixin)

from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from django.urls import (reverse_lazy)
from django.shortcuts import render, redirect

#models
from .models import User

#forms
from .forms import (CustomUserCreationForm, CustomUserChangeForm)

class EmployeList(LoginRequiredMixin,ListView):
    """ vista para listar los empleados """
    
    permission_required = "employees.view_user"
    model = User
    template_name = "employees/list_employee.html"
    context_object_name = "employees"
    
    # se listan los usuarios que no esten eliminados
    def get_queryset(self):
        queryset = self.model.objects.filter(deleted_at = None)
        return queryset

# Crear Empleados
class EmployeCreateView(LoginRequiredMixin, CreateView):
    permission_required="employees.add_user"
    model = User
    template_name="employees/form_employee.html"
    context_object_name = "obj"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("employees_list")
    success_message = "Registro Creado Satisfactoriamente"

# Editar Empleados
class EmployeUpdateView(LoginRequiredMixin, UpdateView):
    permission_required="employees.change_user"
    model = User
    template_name = "employees/form_employee.html"
    context_object_name = "obj"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("employees_list")
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form_pre_save = form.save(commit=False)
        form_pre_save.updated_at = timezone.now()
        form_pre_save.save()
        form.save()
        return super().form_valid(form)

# Eliminar Empleados este eliminado es logico.
class EmployeDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    permission_required="employees.delete_user"
    template_name = "employees/delete_employee.html"
    success_url = reverse_lazy("employees_list")

    def delete(self, request, *args, **kwargs):
            # se obtiene la instancia y se elimina logicamente
            # se desactiva para q no pueda iniciar sesion
            obj = self.get_object()
            obj.is_active = False
            obj.deleted_at = timezone.now()
            obj.save()
            return redirect("employees_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Usuario'
        context['list_url'] = self.success_url
        return context              

# utils
from datetime import datetime

# django
from django import forms
from django.forms import ModelForm

# models
from parking.models import Vehicle, Cell, cell_has_vehicle
from employees.models import User


class SearchForm(forms.Form):
    """ fomulario para el buscador de cliente o vehiculo """

    search = forms.CharField(required=False)

# Forms Vehiculos
class VehiclesForm(ModelForm):
    """ clase form para vehiculos, esta clase permite representar 
        los campos del modelo de vehiculos en un formulario web """

    class Meta:
        model = Vehicle
        exclude = ['created_at', 'updated_at', 'deleted_at','employee']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


# Forms Vehiculos Admin Concerje
class VehiclesForm2(ModelForm):
    """ clase form para vehiculos, esta clase permite representar 
        los campos del modelo de vehiculos en un formulario web """

    class Meta:
        model = Vehicle
        exclude = ['created_at', 'updated_at', 'deleted_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        # se filtra el tipo de usuario q se va mostrar en el select
        self.fields['employee'].queryset = User.objects.filter(type_user=3)


class CellForm(ModelForm):
    """ clase form para celdas, esta clase permite representar 
        los campos del modelo de celdas en un formulario web """

    class Meta:
        model = Cell
        exclude = ['created_at', 'updated_at', 'deleted_at', 'vehicles']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class CellHasVehicleForm(ModelForm):
    """ clase form para vehiculos, esta clase permite representar 
        los campos del modelo de vehiculos en un formulario web """

    class Meta:
        model = cell_has_vehicle
        exclude = ['created_at', 'updated_at', 'deleted_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


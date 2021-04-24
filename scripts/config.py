import os
import sys
import argparse
from parking.models import (Vehicle, Cell, cell_has_vehicle)
from employees.models import (User, Type_Document)
import django
django.setup()


def run():

    configuration()


def configuration():
    print("cargando configuraciones iniciales")

    if Type_Document.objects.filter(name="CEDULA DE CIUDADANIA").exists() != True: 
        Type_Document.objects.create(name="CEDULA DE CIUDADANIA",initials="C.C")

    if Type_Document.objects.filter(name="NUMERO DE IDENTIFICACION TRIBUTARIA").exists() != True: 
        Type_Document.objects.create(name="NUMERO DE IDENTIFICACION TRIBUTARIA" ,initials="NIT")
    
    print("documentos creados")

    print("Creando  Admin")

    tdocument = Type_Document.objects.get(pk=1)
    

    if User.objects.filter(username="admin").exists() !=True:
        user = User(type_user="1",type_document=tdocument,document="152525252525",\
                    name="administrador",surnames="apellidos del admin", username="admin",email="admin@parking.com")
        user.set_password("qwerty123")
        user.save()

    print("Admin creados")
    
    print("Creando corcerje")
    if User.objects.filter(username="concerje").exists() !=True:
        user = User(type_user="2",type_document=tdocument,document="10738493",\
                    name="concerje",surnames="lopez", username="concerje",email="concerje@parking.com")
        user.set_password("qwerty123")
        user.save()   

    print("Conserje creado")     

    print("Creando Empleado y asigando un vehiculo")
    if User.objects.filter(username="pablo").exists() !=True:
        user = User(type_user="3",type_document=tdocument,document="90909090",\
                    name="pablo",surnames="ramos", username="pablo",email="pablo@parking.com")
        user.set_password("qwerty123")
        user.save() 
        print(user)
        if Vehicle.objects.filter(vehicle_registration_number="DXW414").exists() !=True:
            vehicle = Vehicle(employee=user,type_vehicle='3', vehicle_registration_number="DXW414")
            vehicle.save()   
         
    print("Empleado creado y vehiculo asignado")    

    
    print("Creando Celdas")
    if Cell.objects.filter(name="cell1").exists() !=True:
        cell = Cell(type_cell="1", name="cell1")
        cell.save()     

    if Cell.objects.filter(name="cell2").exists() !=True:
        cell = Cell(type_cell="1", name="cell2")
        cell.save()             

    if Cell.objects.filter(name="cell3").exists() !=True:
        cell = Cell(type_cell="1", name="cell3")
        cell.save()             

    if Cell.objects.filter(name="cell4").exists() !=True:
        cell = Cell(type_cell="2", name="cell4")
        cell.save()     

    if Cell.objects.filter(name="cell5").exists() !=True:
        cell = Cell(type_cell="2", name="cell5")
        cell.save()     

    if Cell.objects.filter(name="cell6").exists() !=True:
        cell = Cell(type_cell="2", name="cell6")
        cell.save()                                        

    if Cell.objects.filter(name="cell7").exists() !=True:
        cell = Cell(type_cell="3", name="cell7")
        cell.save()   

    if Cell.objects.filter(name="cell8").exists() !=True:
        cell = Cell(type_cell="3", name="cell8")
        cell.save()           
        

    if Cell.objects.filter(name="cell9").exists() !=True:
        cell = Cell(type_cell="3", name="cell9")
        cell.save()   

    if Cell.objects.filter(name="cell10").exists() !=True:
        cell = Cell(type_cell="3", name="cell10")
        cell.save()   
    print("Celdas creadas")        
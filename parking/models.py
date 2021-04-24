#django
from django.db import models

# utils
from django.utils import timezone
from parking_challenge.utils import vehicle_photo_name, valid_extension

#models
from employees.models import (User)


class Vehicle(models.Model):

    """ modelo para los vehiculos """

    type_vehicles = (
        ('1', 'AUTOMOVIL'),
        ('2', 'MOTOCICLETA'),
        ('3', 'BICICLETA'),
    )

    employee = models.ForeignKey(User, related_name='user_vehicle',
                                    on_delete=models.PROTECT, null=False, blank=False)

    type_vehicle = models.CharField(max_length=4, choices=type_vehicles, default='1', 
                                    null=False, blank=False)
    #cilindraje
    cylinder_capacity = models.CharField(max_length=45, null=True, blank=True) 
    # tiempo o marchas del vehiculo
    gears = models.IntegerField(null=True, blank=True, default=0) 
    # modelo del vehiculo
    vehicle_model = models.CharField(max_length=15, null=True, blank=True) 
    # puertas del vehiculo
    doors_number = models.IntegerField(null=True, blank=True, default=0) 
    # matricula del vehiculo
    vehicle_registration_number = models.CharField(max_length=10, null=False, 
                                                    blank=False, unique=True) 
    
    photo = models.ImageField(upload_to=vehicle_photo_name,
                                max_length=200, null=False, blank=False,
                                validators=[valid_extension,])

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"

    def __str__(self):
        return str("ID:{} |Registration:{} ".format(self.id, self.vehicle_registration_number))


class Cell(models.Model):

    """ modelo para los espacios del parqueadero """

    type_cells = (
        ('1', 'AUTOMOVIL'),
        ('2', 'MOTOCICLETA'),
        ('3', 'BICICLETA'),
    )

    #indica para que tipo de vehiculo esta adecuado el espacio
    type_cell = models.CharField(max_length=4, choices=type_cells, default='1', 
                                    null=False, blank=False)

    name =  models.CharField(max_length=50, null=False, blank=False)

    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # relación tipo muchos a muchos para guardar el historicos de vehiculos
    # y para poder comprobar cuanto uso le dió cada empleado al parqueadero
    vehicles = models.ManyToManyField(Vehicle, through='cell_has_vehicle', 
                                        blank=False, through_fields=('cell','vehicle'))

    class Meta:
        verbose_name = "Celda"
        verbose_name_plural = "Celdas"

    def __str__(self):
        return str("ID:{} |Registration:{} ".format(self.id, self.type_cell))



class cell_has_vehicle(models.Model):

    """ modelo para las Celdas del parqueadero """
    vehicle = models.ForeignKey(Vehicle,
                                on_delete=models.PROTECT, null=False, blank=False)

    employee = models.ForeignKey(User, related_name='employeed_has_parking',
                                    on_delete=models.PROTECT, null=False, blank=False)

    cell = models.ForeignKey(Cell, 
                                on_delete=models.PROTECT, null=False, blank=False)

    status = models.BooleanField(default=True)                                

    # las estampas de tiempo permitiran controlar la hora y fecha de entrada y salida del vehiculo
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Celda y vehiculo"
        verbose_name_plural = "Celdas y Vehiculos"

    def __str__(self):
        return str("ID:{} ".format(self.id))



from os.path import splitext
from datetime import datetime


def vehicle_photo_name(instance, filename):
    """ metodo para asignar el nombre a una imagen """

    timestamp = datetime.now()
    # se toma la matricula del vehiculo y se marca tambien con la fecha para formar el nombre de la imagen
    nombrefinal = "{}_{}_{}_{}_{}_{}_{}".format (instance.vehicle_registration_number,
                        timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)

    file_name,extension = splitext(filename)
    nombrefinal = nombrefinal+str(extension)

    return 'vehicles/{}'.format(nombrefinal)


def valid_extension(value):
    """ metodo para validar que sean imagenes por su extension """

    file_name,extension = splitext(value.name)
    if extension.lower() not in('.png','.jpeg','.jpg'):
        raise ValidationError("Solo se permite archivos: png, jpg, jpeg")
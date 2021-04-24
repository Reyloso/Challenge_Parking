#django
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, AbstractUser, PermissionsMixin)
from django.contrib.auth.models import User

#utils
from django.utils import timezone


class Type_Document(models.Model):
    """ modelo para los tipos de documento """

    name = models.CharField(max_length=45, null=False)
    initials = models.CharField(max_length=3, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"

    def __str__(self):
        return str("ID:{} |Name:{} | Initial: {}".format(self.id, self.name,self.initials))


# class abstrac user for extend model user
class UserManager(BaseUserManager):
    """ clase manager de usuario para extender el modelo usuario y poder 
        agregarle campos personalizados al modelo de usuario pero conservando toda el sistema de
        autenticacion propia de django """

    def create_user(self, username, password=None, **other_fields):
        if not username:
            raise ValueError('Debe tener un nombre de usuario')

        user = self.model(
            username=username,
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **other_fields):
        user = self.create_user(username, password=password,**other_fields)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# super class user
class User(AbstractUser, PermissionsMixin):
    """ clase usuario hereda de la clase abstracta user manager y de la clase de permisos de django"""

    type_users = (
        ('1', 'ADMIN'),
        ('2', 'CONSERJE'),
        ('3', 'EMPLEADO'),
    )
    
    type_document = models.ForeignKey(Type_Document, 
                                    on_delete=models.PROTECT, null=True, blank=True)
    document =  models.CharField(max_length=25, null=False, blank=False, unique=True)
    type_user = models.CharField(max_length=20, choices=type_users, default='3', null=False, blank=False)
    name =  models.CharField(max_length=50, null=False, blank=False)
    surnames = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=25, null=False, blank=False)
    username = models.CharField('username', max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField('email', max_length=255, unique=True, blank=True, null=True)
    
    #campos de permisos propios de django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def get_full_name(self):
        return str("{} {}".format(self.name, self.surnames))

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
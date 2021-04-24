#django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#froms
from employees.forms import (CustomUserCreationForm, CustomUserChangeForm)

#models
from .models import *

# Register your models here.
class Type_Documents(admin.ModelAdmin):
    """ clase para representar el modelo tipos de documento en el panel admin de djangoen el panel admin de django """

    list_filter = ('status',)
    search_fields = ('name',)
    list_display = ['id', 'name', 'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = Type_Document


class Users(BaseUserAdmin):
    """ clase para representar el modelo de usuarios en el panel admin de django"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    
    fieldsets = (
        (None, {'fields': ( 'username', 'password')}),
        ('Information', {'fields': ('type_user', 'type_document', 'document','name', 'surnames', 'email','phone', 'date_joined', 'last_login',)}),
        ('Permissions', {'fields': ('user_permissions', 'groups', 'is_staff', 'is_active', 'is_superuser','is_admin')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'type_user', 'username','password1', 'password2','type_document','document','name','surnames', 'phone', 'email',
                        'user_permissions','groups','is_staff','is_active','is_superuser','is_admin')}
        ),
    )

    list_filter = ('is_active',)
    search_fields = ('name', 'initials',)
    list_display = ['id', 'document', 'name', 'surnames','phone','is_active', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = User

admin.site.register(Type_Document, Type_Documents)
admin.site.register(User, Users)
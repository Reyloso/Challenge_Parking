from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from employees.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm):
        model = User
        fields = ['name', 'username', 'type_document', 'type_user', 'surnames', 
                'document',  'phone',  'email',  'password1', 'password2', 
                'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'type_document', 'type_user', 'surnames', 
                'document',  'phone',  'email', 'is_active']


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })        
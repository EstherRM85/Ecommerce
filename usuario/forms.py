from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username','email']
        labels = {
            'first_name': 'Nombre de usuario',
            'last_name': 'Apellido de usuario',
            'username': 'Indica correo electrónico',
            'email': 'Indica email',
            }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'id': 'first_name', 'placeholder':'indica nombre'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'id': 'last_name', 'placeholder':'indica correo'}),
            'username' : forms.TextInput(attrs={'class':'form-control', 'id': 'username', 'placeholder':'indica usuario nick'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'id': 'email'}),
        }
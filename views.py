from django.contrib.auth.models import User #estos son modelos propios de django para crear el modelo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.views.generic import CreateView,FormView,TemplateView, RedirectView
from django.urls import reverse_lazy,reverse
from .forms import FormularioLogin,RegistroForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect



# Create your views here.


class RegistroUsuario(CreateView):
    model= User
    template_name= 'usuario/registrar.html'
    form_class= RegistroForm
    
    def get_success_url(self):
        return reverse('login')
    
class Login(FormView):
    model= User
    template_name = 'usuario/login.html'
    form_class= FormularioLogin
    def get_success_url(self):
        return reverse('app:carro')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

<<<<<<< HEAD
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 4a479e64b193376f83d147cd6b36d3adf5978e66

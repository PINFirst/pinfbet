from django.shortcuts import render, redirect
from django import forms
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login, authenticate, logout



def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        surnames = form.cleaned_data.get("surnames")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = Student(username=username)
        newUser.first_name = name
        newUser.last_name = surnames
        newUser.email = email
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect("Feed")

    return render(request, 'SignUp.html', {'form': form})


class Terms(View):
    template = 'Terms.html'

    def get(self, request):
        return render(request, self.template)


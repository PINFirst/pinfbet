from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class Feed(View):
    template = 'feed.html'

    def get(self, request):
        return render(request, self.template)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.info(request, 'Usuario o contraseña incorrectas')
            print('Usuario incorrecto')

    return render(request, 'login.html')
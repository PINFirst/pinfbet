from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):

    name = forms.CharField(label="",max_length=20, widget=forms.TextInput(attrs={'class': 'input','placeholder':"Nombre"}))
    surnames = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'class': 'input','placeholder':"Apellidos"}))
    username = forms.CharField(label="",max_length=20, widget=forms.TextInput(attrs={'class': 'input','placeholder': 'Usuario'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'input','placeholder':"Email"}))
    password = forms.CharField(max_length=20,label="", widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':"Contraseña"}))
    confirm = forms.CharField(max_length=20, label="", widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':"Repite contraseña"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        name = self.cleaned_data.get("name")
        surnames = self.cleaned_data.get("surnames")
        password = self.cleaned_data.get("password")

        if User.objects.filter(email=email).exists():
            self.add_error("email","El email no es único")
        else:
            if User.objects.filter(username=username).exists():
                self.add_error("username", "El usuario no es único")
        values = {
            "email": email,
            "username": username,
            "name": name,
            "surnames": surnames,
            "password": password,
        }
        return values




from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credencias invalidas'
        else:
            msg = 'Erro na validação do formulario'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

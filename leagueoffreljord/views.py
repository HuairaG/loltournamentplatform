from django.shortcuts import render, redirect
from . import userviews
from django.contrib import messages
from leagueoffreljord.userforms import UserForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            i = form.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return render(request, 'index.html')
        messages.error(request, 'La cuenta ya existe o el formulario es invalido.')
    form = UserForm()
    return render(request, 'index.html', {'form': form})

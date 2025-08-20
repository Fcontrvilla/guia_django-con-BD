from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})


def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('lista_tareas')

    else:
        form = TareaForm()
        return render(request, 'nueva_tarea.html', {'form':form})
from django.shortcuts import redirect, render

from .forms import TareaForm
from .models import Tarea


def lista_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()

    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'gestor_tareas/lista.html', {'form': form, 'tareas': tareas})

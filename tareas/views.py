from django.shortcuts import render, get_object_or_404, redirect

from .models import Tarea

# Ejercicio 6: Listar todas las tareas (Modelo → Vista)

def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista.html', {'tareas': tareas})

# Ejercicio 7: Crear nueva tarea

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        tarea = Tarea(titulo=titulo, descripcion=descripcion)
        tarea.save()
        return redirect('lista')
    return render(request, 'crear.html')

# Ejercicio 8: Editar tarea existente

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.titulo = request.POST['titulo']
        tarea.descripcion = request.POST['descripcion']
        tarea.completada = 'completada' in request.POST
        tarea.save()
        return redirect('lista')
    return render(request, 'editar.html', {'tarea': tarea})

# Ejercicio 9: Eliminar tarea

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista')
    return render(request, 'eliminar.html', {'tarea': tarea})

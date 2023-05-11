from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Curso

def home(request):

    cursosListados=Curso.objects.all().order_by('nombre')
    
    data={
        'titulo': 'Gestión de Cursos',
        'cursos': cursosListados
    }

    return render(request, "gestionCursos.html", data)

class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        return context


def eliminar_curso(request, id):
    curso=Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')

def registrar_curso(request):
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(nombre= nombre, creditos=creditos)
    return redirect('/')

def edicion_curso(request, id):
    curso=Curso.objects.get(id=id)
    data={
        'titulo': 'Edición de Curso',
        'curso': curso
    }

    return render(request, "edicionCurso.html", data)

def editar_curso(request):
    id = int(request.POST['id'])
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def contacto(request):
    return render(request, "contacto.html")

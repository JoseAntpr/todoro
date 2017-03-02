from django.http import HttpResponseNotFound
from django.shortcuts import render
from tasks.models import Task

# Create your views here.
def tasks_list(request):
    """
    Recupera todas las tareas de la base de datos y las
    pinta
    :param request:
    :return: HttpResponse
    """
    # Recuperamos todas las tareas
    tasks =  Task.objects.select_related("owner","assignee").all()

    #Devolver respuesta

    context = {
        'task_objects': tasks
    }

    return render(request, "tasks/list.html",context)

def task_detail(request, task_pk):
    """
    Recupera una tarea de la base de datos y la pinta con una plantilla
    :param request:  HttpRequest
    :param task_pk: Primary Key de la tarea a recuperar
    :return: HttpResponse
    """

    #Recuperar la tarea
    try:
        task = Task.objects.get(pk=task_pk)
    except Task.DoesNotExist:
        return HttpResponseNotFound("La tarea que buscas no existe.")
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese identificador",status=300)


    #Preparar el contexto

    context = {
        'task': task
    }



    #Renderizar la plantilla
    return render(request, 'tasks/detail.html',context)
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
    tasks =  Task.objects.all()

    #Devolver respuesta

    context = {
        'task_objects': tasks
    }

    return render(request, "tasks/list.html",context)

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


def login(request):
    """

    :param request: HttoRequest
    :return: HttpResponse
    """

    context = dict()

    if request.method == "POST":
        username = request.POST.get("usr")
        password = request.POST.get("pwd")

        user = authenticate(username=username, password=password)

        if user is not None:
            #usuarios autenticadoq
            request.session["default-language"] = "es"
            django_login(request, user)
            url = request.GET.get('next', 'tasks_list')
            return redirect(url)
        else:
            #usuario no autenticado
            context["error"] = "Wrong username or password"



    return render(request, 'login.html', context)

def logout(request):
    """
    Hace logout de un usuario
    :param request: HttpRequest
    :return: HttpResponse
    """
    django_logout(request)

    return redirect('login')

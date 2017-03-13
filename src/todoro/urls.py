"""todoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from tasks.views import tasks_list, task_detail, NewTaskView
from users.api import UsersApi, UserDetailApi
from users.views import LoginView, logout
from tasks.api import TasksApi

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tasks_list, name="tasks_list"),
    url(r'^tasks/(?P<task_pk>[0-9]+)$', task_detail, name="task_detail"),
    url(r'^tasks/new$', NewTaskView.as_view(), name="tasks_new"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'logout', logout, name="logout"),

    #Url
    url(r'api/1.0/users/$', UsersApi.as_view(), name="users_api"),
    url(r'api/1.0/users/(?P<pk>[0-9]+)/?$', UserDetailApi.as_view(), name="user_detail_api"),

    #Api de tasks
    url(r'^api/1.0/tasks/$', TasksApi.as_view(), name="tasks_api")

]

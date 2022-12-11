"""darmoktrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.track import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("projects", views.project_list, name="projects"), 
    path("create_project", views.create_project, name="create_project"),
    path("track/edit_project/<int:pk>", views.edit_project.as_view(), name="edit_project"), 
    path("project/<int:id>", views.project, name="project"),
    path("track/update_task/<int:pk>", views.update_task, name="update_task"), 
    path('tasks/', views.view_tasks, name='view_tasks'), 
    path("tasks/<int:pk>/", views.view_task, name="view_task"),
    path("create_task", views.create_task, name="create_task"),
    path("invoice/<int:project_id>", views.invoice, name="invoice"),
    path("invoices_list/", views.invoices_list, name="invoices_list"), 
 

]

urlpatterns += staticfiles_urlpatterns()

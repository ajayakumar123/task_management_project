"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from taskApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',auth_views.login, {'template_name': 'task/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^task_list/', views.task_list_view, name='task_list'),
    url(r'^task_create/', views.task_create_view, name='task_create'),
    url(r'^task_update/(?P<pk>\d+)/',views.TaskUpdateView.as_view(), name='task_update'),
    url(r'^task_delete/(?P<pk>\d+)/',views.TaskDeleteView.as_view(), name='task_delete'),
    url(r'^user_data/(?P<id>\d+)/',views.user_detail_view, name='user_data'),
    url(r'^ajax/validate_workers_selection/$', views.validate_workers_selection, name='validate_workers_selection'),
]

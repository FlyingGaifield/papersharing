from django.urls import path
from django.conf.urls import include, url

from . import views


appname  = 'share'
urlpatterns = [
    path('', views.index, name='index'),
    url(r"^add/$",views.add,name = 'add'),
    path('<int:catalogue_id>/', views.detail, name='detail'),
]
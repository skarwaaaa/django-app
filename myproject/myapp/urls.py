from django.urls import path, include
from . import views


app_main = 'myapp'

urlpatterns = [
    path('', views.Index, name='index'),
]
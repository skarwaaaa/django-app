from django.urls import path, include
from . import views


app_main = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
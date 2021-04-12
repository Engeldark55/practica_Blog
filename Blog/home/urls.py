
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('programacion/',views.Programacion,name='programacion'),
    path('videojuegos/',views.VideoJuegos,name='VJ'),
    path('tecnologia/',views.Tecnologia,name='Tecno'),
    path('<slug:slug>/',views.post,name='post'),
]

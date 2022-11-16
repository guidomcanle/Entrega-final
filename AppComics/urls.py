from django.urls import path
from AppComics import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('comics/', views.comics, name = "Lista de comics"),
    path('agregar_comics/', views.agregar_comics, name = "Agregar comics"),
    path('agregar_guionistas/', views.agregar_guionistas, name = "Agregar guionistas"),
    path('agregar_dibujantes/', views.agregar_dibujantes, name = "Agregar dibujantes"),
    path('agregar_editoriales/', views.agregar_editoriales, name = "Agregar editoriales"),
    path('buscar_comics/', views.buscar_comics, name = "Buscar comics"),
    path('buscar/', views.buscar)
]
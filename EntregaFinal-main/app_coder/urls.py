from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #NAVEGACIÓN PRINCIPAL
    path("", views.inicio, name= "inicio"),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    path("directivos", views.directivos, name="directivos"),
    #path("about", views.about, name= "about"),
    #ALTAS
    path("alta_curso" , views.alta_curso, name="alta_curso"),
    path("alta_profesores", views.alta_profesores, name="alta_profesores"),
    path("alta_alumnos", views.alta_alumnos, name="alta_alumnos"),
    path("alta", views.alta, name="alta"),

    #BUSCAR
    path("buscar_curso" , views.buscar_curso, name= "buscar_curso"),
    path("buscar", views.buscar, name= "buscar"),

    #EDITAR Y ELIMINAR
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    path("editar_curso" , views.editar_curso ,name="editar_curso"),

    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("editar_profesor" , views.editar_profesor ,name="editar_profesor"),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    
    path("elimina_alumno/<int:id>" , views.elimina_alumno ,name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_alumno" , views.editar_alumno ,name="editar_alumno"),

    #LOGS y REGISTER
    path("login" , views.login_request , name="Login"),
    path("register" , views.register , name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_perfil" , views.editarPerfil , name="editar_perfil")
]

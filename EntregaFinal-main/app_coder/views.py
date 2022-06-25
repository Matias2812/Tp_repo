from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Alumno, Curso, Profesores, Avatar
from django.template import loader
from app_coder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario
from app_coder.forms import Curso_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 

#VISTAS GENERALES

def inicio(request):
    return render( request , "plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alumnos(request):

    alumnos = Alumno.objects.all()
    dicc = {"alumno" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )


def directivos(request):

    return render( request , "directivos.html" )


def profesores(request):

    profesores = Profesores.objects.all()
    dicc = {"profesores" : profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento ) 


#ALTAS
@login_required
def alta_curso(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "plantillas.html")

    return render( request, "formulario.html")




@login_required
def alta_profesores(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesor = Profesores(nombre = datos['nombre'], legajo = datos['legajo'], fecha_alta = datos['fecha_alta'], dicta_materia = datos['dicta_materia'], email = datos['email'] )
            profesor.save()

        return render(request, "plantillas.html")
    
    return render( request, "alta_profesores.html")





@login_required
def alta_alumnos(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'], nacimiento=datos['nacimiento'])
            alumno.save()

            return render( request , "plantillas.html")

    return render( request, "alta_alumnos.html")

@login_required
def alta(request):
    return render(request, "alta.html")



#BUSCAR
def buscar_curso(request):

    return render( request , "buscar_curso.html")




def buscar_alumnos(request):

    return render( request , "buscar_alumnos.html")




def buscar_profesores(request):

    return render( request , "buscar_profesores.html")



def resultado_curso(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")





def resultado_alumnos(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        alumnos = Alumno.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_alumnos.html" , {"alumnos": alumnos})
    else:
        return HttpResponse("Campo vacio")




def resultado_profesores(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesores = Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_profesores.html", {"profesores": profesores})
    else:
        return HttpResponse("Campo vacio")







#ELIMINAR Y EDITAR
@login_required
def elimina_alumno( request , id):

    
    alumno = Alumno.objects.get(id=id)



    alumno.delete()
        
    alumno = Alumno.objects.all()
    return render(request , "alumnos.html" , {"alumno": alumno})

@login_required
def elimina_curso( request , id):

    
    curso = Curso.objects.get(id=id)



    curso.delete()
        
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos": curso})



def editar_alumno( request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.camada = datos['camada']
            alumno.nacimiento = datos ['nacimiento']
            alumno.save()

            alumno = Alumno.objects.all()          
            return render(request , "alumnos.html" , {"alumnos": alumno})
    else:
        mi_formulario = Alumno_formulario(initial={'nombre':alumno.nombre , "camada":alumno.camada, "nacimiento":alumno.nacimiento})
    
    return render( request , "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumnos": alumno})   




@login_required
def editar_curso( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos.html" , {"cursos": curso})
    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})

def editar_profesor( request , id):

    profesores = Profesores.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesores.nombre = datos['nombre']
            profesores.legajo = datos['legajo']
            profesores.fecha_alta = datos['fecha_alta']
            profesores.dicta_materia = datos['dicta_materia']
            profesores.email= datos['email']        
            profesores.save()

            profesor = Profesores.objects.all()          
            return render(request , "profesores.html" , {"profesores": profesor})
    else:
        mi_formulario = Profesor_formulario(initial={'nombre':profesores.nombre,'legajo':profesores.legajo, 'fecha_alta': profesores.fecha_alta,'dicta_materia':profesores.dicta_materia,'email':profesores.email})
    
    return render( request , "editar_profesor.html" , {"mi_formulario":mi_formulario, "profesores": profesores})

def elimina_profesor( request , id):

    
    profesor = Profesores.objects.get(id=id)

    profesor.delete()
        
    profesor = Profesores.objects.all()
    return render(request , "profesores.html" , {"profesores": profesor})
    

#LOGS y REGISTER
def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html")
                
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render (request, "plantillas.html")


    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})


#EDITAR PERFIL
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})


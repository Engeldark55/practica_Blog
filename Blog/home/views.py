from django.shortcuts import render
from .models import Categoria, Post
from django.db.models import Q #consulta de db
from django.core.paginator import Paginator #paginator #paginacion 

#==============================================
                #FUNCION iNDEX
#==============================================
# Create your views here.
def index(request):
    query=request.GET.get("buscar")#buscar
    lista_post=Post.objects.filter(estado = True)#enlistar
    if query:#buscar
        lista_post=Post.objects.filter(
            Q(titulo__icontains=query)|#___icontains significa que no importa que haya adelante y atras busca la palabra indicada
            Q(descropcion__icontains=query)
        ).distinct()#para que no traiga lo mismo que la primera busqueda ya sea ,titlo o descripcion en este caso  (no repita)
    lista_post=paginacion(request,lista_post)
    contex={
        'post':lista_post
    }
    return render(request, 'layaut.html',contex)
    

#==============================================
                #FUNCION PAGINACION
#==============================================
def paginacion(request,lista_post):
    paginacion=Paginator(lista_post,3)#numero de paginas que quieres que se dibida
    page=request.GET.get('page')#esto por que se se tiene en que pagina esta actual mente 
    lista_post=paginacion.get_page(page)#se accigna de nuevo a ala lista post para que de lo element que faltan
    return lista_post

 #==============================================
                #FUNCION POST
#==============================================   
def post(request,slug):
    consulta_post=Post.objects.get(slug=slug)
    context={
        'post':consulta_post
        }
    return render(request,'post.html',context)

#==============================================
                #FUNCION PROGRAMCION
#==============================================

def Programacion(request):
    post_programacion=Post.objects.filter(estado = True, categoria=Categoria.objects.get(nombre = 'programacion'))    
    post_programacion=paginacion(request,post_programacion)#paginacion
    context={
            'titulo':'Programacion',
            'post':post_programacion,
    }
    return render(request,'programacion.html',context)

#==============================================
                #FUNCION VIDEO-JUEGOS
#==============================================

def VideoJuegos(request):
    query=request.GET.get("buscar")#buscar
    post_videojuego=Post.objects.filter(estado = True, categoria=Categoria.objects.get(nombre__iexact = 'video juegos'))
    if query:#buscar
        lista_post=Post.objects.filter(
            Q(titulo__icontains=query)|#___icontains significa que no importa que haya adelante y atras busca la palabra indicada
            Q(descropcion__icontains=query),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='video juegos')#solo buscara este genero
        ).distinct()#para que no traiga lo mismo que la primera busqueda ya sea ,titlo o descripcion en este caso  (no repita)
   
    context={
         'titulo':'video Juegos XD',
         'post':post_videojuego
    }
    return render(request,'videoJuegos.html',context)

#==============================================
                #FUNCION TECNOLOGIA
#==============================================

def Tecnologia(request):

    post_tecnologia=Post.objects.filter(estado = True, categoria=Categoria.objects.get(nombre = 'tecnologia'))
    context={
        'titulo':'tecnologia',
        'post': post_tecnologia,
    }
    return render(request,'tecnologia.html',context)



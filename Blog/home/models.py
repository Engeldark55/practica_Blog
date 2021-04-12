from django.db import models
from ckeditor.fields import RichTextField #el instalado para word
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombre de categoria', max_length=100, null=False,blank=False)
    estado=models.BooleanField('Categoria activada/categoria no activada', default=True)
    fecha_creacion=models.DateField('Fecha de creacion categoria',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.nombre
class Autor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('nombre del autor',max_length=255, null=False, blank=False)
    apellidos=models.CharField('apellidos del autor', max_length=300, null=False,blank=False)
    facebook=models.URLField('facebook', null=True,blank=True)
    email=models.EmailField('correo del autor', blank=False,null=False)
    estado=models.BooleanField('autor activo/no activo', default=True)
    fecha_creacion=models.DateField('fecha de creacion autor',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

        def __str__(self):
            return f"{self.apellidos} {self.nombre}"

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField('titulo',max_length=40,blank=False,null=False)
    slug=models.CharField('slug',max_length=100,null=False,blank=False)
    descropcion=models.CharField('descripcion',max_length=110,null=False,blank=False)
    contenido=RichTextField('contenido')
    imagen=models.URLField(max_length=250,blank=False,null=False)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado=models.BooleanField('publico/no publico',default=True)
    fecha_creacion=models.DateField('fecha_creacion',auto_now=False,auto_now_add=True)
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
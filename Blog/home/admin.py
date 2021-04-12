from django.contrib import admin
from .models import *
#esta es la herramienta esxtra que instalamos de import_export
from import_export import resources
from import_export.admin import ImportExportModelAdmin as Imp_Exp


class categoriaResource(resources.ModelResource):
    class Meta:
        model=Categoria
# Register your models here.
class categoriaAdmin(Imp_Exp,admin.ModelAdmin):
    search_fields=['nombre']#esto agrega la barra de busqueda de admin
    #esta parte se agregan los atributos extra que se crearon los modelos para referencia o una mejor visualizacion
    #estos mismosayudan a los formularios
    list_display=('nombre','estado',)#se visualiza el nombre que le dimos en los modelos, estado si esta activo, etc
    resources_class=categoriaResource


class autorResouerce(resources.ModelResource):
    class Meta:
        model=Autor

class autoraAdmin(Imp_Exp,admin.ModelAdmin):
    search_fields=['nombre']#esto agrega la barra de busqueda de admin
    #esta parte se agregan los atributos extra que se crearon los modelos para referencia o una mejor visualizacion
    #estos mismosayudan a los formularios
    list_display=('nombre','apellidos','email','facebook','estado',)#se visualiza el nombre que le dimos en los modelos, estado si esta activo, etc
    resources_class=autorResouerce
   
 

#registro al panel de admin lovalhost    
admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Autor,autoraAdmin)
admin.site.register(Post)

from django.contrib import admin
from .models import Curso, Docente

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=('id','coloreado','creditos')
    ordering = ('nombre',) 

    search_fields = ('nombre', 'creditos')

    """
    fieldsets=(
        (None, {
            'fields': ('nombre',)
        }),
        ('Advances options', {  #Documentación de Django class FlatPageAdmin
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )
    """

admin.site.register(Docente)

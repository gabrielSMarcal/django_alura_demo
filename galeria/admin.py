from django.contrib import admin

from .models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'categoria', 'publicada')
    list_display_links = ('nome',)
    search_fields = ('nome', 'legenda')
    list_filter = ('categoria', 'publicada')
    list_editable = ('publicada',)
    list_per_page = 10
    
admin.site.register(Fotografia, ListandoFotografias)

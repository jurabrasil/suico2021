from django.contrib import admin
from .models import Time, Jogo, Pontuar

# Register your models here.

class ListandoPontuar(admin.ModelAdmin):
    list_display = ('id', 'time', 'j', 'pg', 'v', 'e', 'd', 'gp', 'gc', 'sg' )

class ListandoJogos(admin.ModelAdmin):
    list_display = ('id', 'rodada', 'timea', 'placara', 'placarb', 'timeb', 'gols_total')
    list_editable = ('timea', 'timeb', 'placara', 'placarb', 'gols_total')

admin.site.register(Time)
admin.site.register(Jogo, ListandoJogos)
admin.site.register(Pontuar, ListandoPontuar)
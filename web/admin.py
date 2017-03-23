from django.contrib.gis import admin
from models import *

class FotoInLine(admin.TabularInline):
  model = Foto
  exclude = ('foto_med', 'foto_peq',)

class PlantaAdmin(admin.OSMGeoAdmin):
  default_lon = -420709
  default_lat = 4882227
  default_zoom = 5
  inlines = [ FotoInLine, ]

admin.site.register(Planta, PlantaAdmin)
admin.site.register(Familia)

from django.contrib import admin
from .models import Incidences, Sub_Counties
from leaflet.admin import LeafletGeoAdmin 

# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    # pass
    list_display = ("name", "location") # arranging incidences in a tabular manner

class SubCountiesAdmin(LeafletGeoAdmin):
    display_list = ('constituen', 'geom')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Sub_Counties, SubCountiesAdmin)

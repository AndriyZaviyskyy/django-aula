from django.conf.urls import url
from .views import descarregaAlumnes
#from .views import descarregaAules
from .views import descarregaHoraris
#from .views import descarregaPresencia
from .views import descarregaAssignatures

urlpatterns = [
    url(r'^descarregaAlumnes/$', descarregaAlumnes,
       name="administracio__descarrega__alumnes" ),

#    url(r'^descarregaAules/$', descarregaAules,
#        name="administracio__descarrega__aules" ),

    url(r'^descarregaHoraris/$', descarregaHoraris,
        name="administracio__descarrega__horaris" ),

#    url(r'^descarregaPresencia/$', descarregaPresencia,
#        name="administracio__descarrega__presencia" ),

    url(r'^descarregaAssignatures/$', descarregaAssignatures,
        name="administracio__descarrega__assignatures" ),

]
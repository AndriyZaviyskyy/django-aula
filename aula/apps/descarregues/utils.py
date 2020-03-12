import csv

from django.http import HttpResponse

from aula.apps.alumnes.models import Alumne
from aula.apps.aules.models import Aula
from aula.apps.horaris.models import Horari
from aula.apps.presencia.models import ControlAssistencia #hay que revisar que sea correcta la informacion que llega.
from aula.apps.assignatures.models import Assignatura

def compose_alumnes_csv_response():
    """ composes the alumnes data in a csv format and returns it as a http response """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alumnes.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Cognoms', 'Grup', 'Data de naixement'])

    alumnes = Alumne.objects.all()
    for alumne in alumnes:
        row = [alumne.ralc, alumne.cognoms, alumne.grup, alumne.data_neixement]
        writer.writerow(row)

    return response
"""
def compose_alues_csv_response():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aules.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Cognoms', 'Grup', 'Data de naixement'])

    aules = Aula.objects.all()
    for aula in aules:
        row = [alumne.nom, alumne.cognoms, alumne.grup, alumne.data_neixement]
        writer.writerow(row)

    return response
"""

def compose_horaris_csv_response():
    """ composes the horaris data in a csv format and returns it as a http response """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="horaris.csv"'
    writer = csv.writer(response)
    writer.writerow(['assignatura', 'professor', 'grup', 'dia_de_la_setmana', 'hora', 'nom_aula'])

    horaris = Horari.objects.all()
    for horari in horaris:
        row = [horari.assignatura, horari.professor, horari.grup, horari.dia_de_la_setmana, horari.hora, horari.nom_aula]
        writer.writerow(row)

    return response

"""
def compose_presencia_csv_response():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="presencia.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Cognoms', 'Grup', 'Data de naixement'])

    alumnes = Alumne.objects.all()
    for alumne in alumnes:
        row = [alumne.nom, alumne.cognoms, alumne.grup, alumne.data_neixement]
        writer.writerow(row)

    return response
"""

def compose_assignatures_csv_response():
    """ composes the assignatures data in a csv format and returns it as a http response """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assignatures.csv"'
    writer = csv.writer(response)
    writer.writerow(['curs', 'tipus_assignatura', 'codi_assignatura', 'nom_assignatura'])

    assignatures = Assignatura.objects.all()
    for assignatura in assignatures:
        row = [assignatura.curs, assignatura.tipus_assignatura, assignatura.codi_assignatura, assignatura.nom_assignatura]
        writer.writerow(row)

    return response
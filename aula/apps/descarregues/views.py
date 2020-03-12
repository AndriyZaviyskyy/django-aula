from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from aula.utils.decorators import group_required
from .forms import descarregaForm
from .utils import compose_alumnes_csv_response
#from .utils import compose_aules_csv_response
from .utils import compose_horaris_csv_response
#from .utils import compose_presencia_csv_response
from .utils import compose_assignatures_csv_response
from aula.apps.alumnes.models import Grup

@login_required
@group_required(['direcció'])
def descarregaAlumnes(request):
    """ Download the students in a csv file """
    if request.method == 'POST':
        form = descarregaForm(request.POST)
        if form.is_valid():
            return compose_alumnes_csv_response()
    else:
        form = descarregaForm()

    grups = [g.descripcio_grup for g in Grup.objects.all()]
    return render(request,
                  'formDescarregaAlumnes.html',
                  {'form': form, 'head': 'Descarrega Alumnes', 'grups': grups}
                  )

#descarregaAula
"""
def descarregaAules(request):
    if request.method == 'POST':
        form = descarregaForm(request.POST)
        if form.is_valid():
            return compose_alumnes_csv_response()
    else:
        form = descarregaForm()

    return render(request,
                  'form.html',
                  {'form': form, 'head': 'Descarrega'}
                  )
"""
#descarregaHoraris    
def descarregaHoraris(request):
    """ Download the students in a csv file """
    if request.method == 'POST':
        form = descarregaForm(request.POST)
        if form.is_valid():
            return compose_horaris_csv_response()
    else:
        form = descarregaForm()

    return render(request,
                  'form.html',
                  {'form': form, 'head': 'Descarrega'}
                  )

#descarrregaPresencia
"""
def descarregaPresencia(request):

    if request.method == 'POST':
        form = descarregaForm(request.POST)
        if form.is_valid():
            return compose_alumnes_csv_response()
    else:
        form = descarregaForm()

    return render(request,
                  'form.html',
                  {'form': form, 'head': 'Descarrega'}
                  )
"""
#descarregaAssignatures
def descarregaAssignatures(request):
    """ Download the students in a csv file """
    if request.method == 'POST':
        form = descarregaForm(request.POST)
        if form.is_valid():
            return compose_assignatures_csv_response()
    else:
        form = descarregaForm()

    return render(request,
                  'form.html',
                  {'form': form, 'head': 'Descarrega'}
                  )


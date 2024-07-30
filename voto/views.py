from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from candidato.models import *
from estudiante.models import *
from voto.models import Voto
from listas.models import Listas
from weasyprint import HTML
from django.template.loader import get_template

    
def voto(request): 
    votos = Voto.objects.all()
    datos = {}
    resultados = Listas.objects.all()
    datos['resultados']= resultados

    return render(request, 'resultados/votos.html', datos)


def reporte(request):
    context = {}
    context['listas'] = Listas.objects.all()
    html = get_template('resultados/reporte.html')
    render_html = html.render(context)
    pdf = HTML(string = render_html).write_pdf()
    reporte = HttpResponse(pdf, content_type='aplication/pdf')
    reporte['Content_Disposition'] = 'inline; fillname=reporte.pdf'
    
    return reporte
    #return render(request, 'resultados/reporte.html', context)

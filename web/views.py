from django.http import HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from web.models import *

def listado(request):
  plantas = Planta.objects.order_by('familia__nombre')
  return render(request, 'listado.html', {'plantas': plantas})

def plantas_json(request):
  points_as_geojson = serialize('geojson', Planta.objects.all())
  return HttpResponse(points_as_geojson, content_type='json')

def MainPageView(request):
  plantas = Planta.objects.all()
  return render(request, 'index.html', {'plantas': plantas})

class HerbarioPDF(View):
  def get(self, request):
    response = HttpResponse(content_type='application/pdf')
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(225, 790, u"Herbario Maria Soledad Fernandez Contreras")
    pdf.showPage()
    meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
    for planta in Planta.objects.order_by('familia__nombre'):
      pdf.setFont("Helvetica", 12)
      pdf.drawString(40, 790, u"Familia: " + planta.familia.nombre)
      pdf.drawString(40, 770, u"Nombre: " + planta.genero + ' ' + planta.especie)
      pdf.drawString(40, 750, u"Fecha recogida: " + str(planta.fecha_recogida.day) + " de " + meses[planta.fecha_recogida.month] + " de " + str(planta.fecha_recogida.year))
      pdf.drawString(40, 730, u"Lugar: " + planta.municipio + ", " + planta.provincia)
      if planta.foto_set.count() < 3:
        for i,f in enumerate(planta.foto_set.all()):
          pdf.drawImage('/home/nano/herbario' + f.foto.url, 90, 400 - i*370, 420, 290, preserveAspectRatio=True)
      elif planta.foto_set.count() == 3:
        for i,f in enumerate(planta.foto_set.all()):
          pdf.drawImage('/home/nano/herbario' + f.foto.url, 90, 500 - i*220, 280, 210, preserveAspectRatio=True)
      #Con show page hacemos un corte de pagina para pasar a la siguiente
      pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

from __future__ import unicode_literals

from django.contrib.gis.db import models
from web.utils import get_upload_path
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Municipio(models.Model):
  codigo = models.CharField(max_length=5)
  texto = models.CharField(max_length=254)
  cod_prov = models.CharField(max_length=2)
  provincia = models.CharField(max_length=50)
  cod_ca = models.CharField(max_length=2)
  comunidad_autonoma = models.CharField(max_length=50)
  
  mpoly = models.MultiPolygonField()

  def __str__(self):              # __unicode__ on Python 2
        return self.texto

class Familia(models.Model):
  nombre = models.CharField(max_length=100)

  def __unicode__(self):
    return self.nombre

  class meta:
    ordering = ['nombre',]

class Planta(models.Model):
  familia = models.ForeignKey(Familia, blank=True)
  genero = models.CharField(max_length=100)
  especie = models.CharField(max_length=100)
  autor = models.CharField(max_length=100)
  lugar = models.PointField(srid=4326)
  fecha_recogida = models.DateField()
  provincia = models.CharField(max_length=100)
  municipio = models.CharField(max_length=100)

  def save(self, *args, **kwargs):
    pnt = Municipio.objects.get(mpoly__contains=self.lugar.geojson)
    self.municipio = pnt.texto
    self.provincia = pnt.provincia
    super(Planta, self).save(*args, **kwargs)

  @property
  def popupContent(self):
    return '''<div class="media">
              <div class="media-left">
                <a href="{}">
                  <img class="media-object" width="200" height="200" src="{}">
                </a>
              </div>
              <div class="media-body">
                 <h4 class="media-heading">{} {}</h4>
                 <p>{}</p>
                 <p>{}</p>
                 <p>{}</p>
              </div>
            </div>'''.format(
          self.foto_set.all()[0].foto_med.url,
          self.foto_set.all()[0].foto_peq.url,
          self.genero,
          self.especie,
          self.municipio,
          self.provincia,
          self.fecha_recogida)

  def __unicode__(self):
    return '%s %s' % (self.genero, self.especie) 

  class meta:
    ordering = ['familia.nombre',]


class Foto(models.Model):
  planta = models.ForeignKey(Planta, blank=True)
  tipo = models.CharField(max_length=100, choices=(
    ('porte', 'Porte'),
    ('hoja', 'Hoja'),
    ('flor', 'Flor'),
    ('fruto', 'Fruto'),
    ('dni', 'DNI'),
    )
  )
  foto = models.ImageField(upload_to=get_upload_path)
  foto_med= ImageSpecField(source='foto',
                           processors=[ResizeToFill(1200,900)],
		   	   format='JPEG',
			   options={'quality':95})
  foto_peq= ImageSpecField(source='foto',
                           processors=[ResizeToFill(200,200)],
  			   format='JPEG',
			   options={'quality':95})

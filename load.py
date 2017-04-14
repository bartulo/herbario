import os
from django.contrib.gis.utils import LayerMapping
from web.models import Municipio

municipios_mapping = {
    'codigo' : 'Codigo',
    'texto' : 'Texto',
    'cod_prov' : 'Cod_Prov',
    'provincia' : 'Provincia',
    'cod_ca' : 'Cod_CCAA',
    'comunidad_autonoma' : 'ComAutonom',
    'mpoly' : 'POLYGON',
}

municipios_shp = '/home/nano/herbario/municipios/Municipios_ETRS89_30N.shp'

def run(verbose=True):
    lm = LayerMapping(Municipio, municipios_shp, municipios_mapping)
    lm.save(strict=True, verbose=verbose)

import os 

def get_upload_path(instance, filename):
  ext = filename.split('.')[-1]
  filename = '%s_%s_%s.%s' % (instance.planta.genero, instance.planta.especie, instance.tipo, ext)

  return os.path.join(instance.planta.familia.nombre, filename)


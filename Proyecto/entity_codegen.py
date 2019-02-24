
#sirve para mover archivos
import shutil
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_metaModelo_Entidad
from entity_test import main2

def main(debug=False):

    this_folder = dirname(__file__)

    metaModeloEntidad = get_metaModelo_Entidad(debug)

    # Construye en modelo para la entidad Comida
    modelo_comida = metaModeloEntidad.model_from_file(join(this_folder, 'Comida.ent'))

    def javatype(s):
        #asimila enteto y texto con la escritura int y String
        return {
                'entero': 'int',
                'texto': 'String'
        }.get(s.name, s.name)

    # crea una carpeta donde poner el HTML 
    carpeta_generacion_HTML = join(this_folder, 'htmlGenerado')
    if not exists(carpeta_generacion_HTML):
        mkdir(carpeta_generacion_HTML)

    # inicializa la plantilla
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    
    # Carga la plantilla 
    plantilla = jinja_env.get_template('Plantilla.template')

    for entity in modelo_comida.entidades:
        # para cada entidad genera un archivo java
        with open(join(carpeta_generacion_HTML,
                       "Menu%s.html" % entity.nombre.capitalize()), 'w') as f:
            f.write(plantilla.render(entidad=entity))
        with open(join(this_folder,"informacion.json")) as  origen:
                   with open(join(carpeta_generacion_HTML,
                              "informacion.json"), 'w') as destino:
                              shutil.copyfileobj(origen,destino)

if __name__ == "__main__":
    main()
    main2()

from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export


this_folder = dirname(__file__)


class TipoSimple(object):
   
    def __init__(self, parent, nombre):
        self.parent = parent
        self.nombre = nombre

    def __str__(self):
        return self.nombre


def get_metaModelo_Entidad(debug=False):
    
    # Creamos un modelo en el cual se indica la Gramatica y sintaxis que tendra
    # Le indicamos que asocie entero y texto con integer y string
    
    type_builtins = {
            'entero': TipoSimple(None, 'integer'),
            'texto': TipoSimple(None, 'string')
    }
    metaModeloEntidad = metamodel_from_file(join(this_folder, 'Gramatica.tx'),
                                    classes=[TipoSimple],
                                    builtins=type_builtins,
                                    debug=debug)

    return metaModeloEntidad


def main2(debug=False):

    metaModeloEntidad = get_metaModelo_Entidad(debug)

    # Exporta un archivo .dot para la visualizacion en la carpeta dotGenerados
    carpeta_dot = join(this_folder, 'dotGenerados')
    if not os.path.exists(carpeta_dot):
        os.mkdir(carpeta_dot)
    metamodel_export(metaModeloEntidad, join(carpeta_dot, 'metaModeloEntidad.dot'))

    # Construye un modelo para la entidad Comida basado en el modelo creado previamente con la gramatica stablecida
    modelo_comida = metaModeloEntidad.model_from_file(join(this_folder, 'Comida.ent'))

    # Exporta un archivo .dot esta vez para la entidad comida
    model_export(modelo_comida, join(carpeta_dot, 'Comida.dot'))


    #Si llaman al main corra main2
if __name__ == "__main__":
    main2()

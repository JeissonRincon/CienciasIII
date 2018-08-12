from random import*
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    def nombres(self):
        return ["El Alquimista","Pinocho", "La cenicienta", "El final", "Por amor", "Metamorfosis" , "Encerrados en la puerta de atrás", "El retrato de Dorian Grey","Mi lucha", "La caída de los dioses"]
    def autores(self):
        return["José Asunción Silva", "Dan brown", "Óscar Wilde", "Gabriel García Márquez", "William Shakespeare", "Karen Mac Combie","Stephen  Chbosky", "Stephen King","Verónica Roth", "Jhon Boyne"]
    def entrada(self):
        return [(x,y) for x in self.nombres() for y in self.autores()]
    def revolver(self):
        return sample(self.entrada(),len(self.entrada()))
    def funcionar(self):
        verificacion="S"
        while(verificacion=="S" or verificacion=="s"):
            print("Bienvenido: Que desea hacer? \n")
            opcion=int(input("1: Ingresar libros \n2: Sacar libros \n3: Ver cola \n*: Salir \n"))
            if(opcion==1):
                cantidad=int(input("Cuantos libros desea ingresar? \n"))
                while(cantidad!=0):
                    libro=self.revolver()
                    lib=libro.pop(0)
                    for v in lib:
                        self.apilar(v)
                    cantidad=cantidad-1
            else:
                if(opcion==2):
                    cantidad=int(input("Cuantos libros desea sacar? \n"))*2
                    while(cantidad!=0):
                        self.desapilar()
                        cantidad=cantidad-1
                else:
                    if(opcion==3):
                        print(list(self.items))
                    else:
                        print("Por favor ingrese una opcion validad")
            verificacion=input("Desea continuar? S/N ")
    
pila=Pila()
pila.funcionar()

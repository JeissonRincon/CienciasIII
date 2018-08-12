from random import sample
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)
        

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    def nombres(self):
        return ["Andres Lopez","Pedro Campo", "Ruben Suarez", "Carlos Roca", "James Falcao", "Lionel Ronaldo" , "Pibe Higuita", "Faustino Renteria","Jeisson Tocarruncho", "Luis Meltrozo"]
    def placas(self):
        return["ABC 123", "BCD 234", "CDE 345", "DEF 456", "SXO 666", "ANL 069","PNE 414", "XXX 666","CKT 789", "POP 000"]
    def entrada(self):
        return [(x,y) for x in self.nombres() for y in self.placas()]
    def revolver(self):
        return sample(self.entrada(),len(self.entrada()))
    
    
cola=Cola()

print("Bienvenido:")
opcion=int(input("Cuantos vehiculos desea ingresar?"))
while(opcion!=0):
    vehiculo=cola.revolver()
    vehi=vehiculo.pop(0)
    for v in vehi:
        cola.encolar(v)
    opcion=opcion-1
print(list(cola.items))

opcion=int(input("Cuantos vehiculos desea sacar?"))*2 
while(opcion!=0):
    cola.desencolar()
    opcion=opcion-1
print(cola.items)

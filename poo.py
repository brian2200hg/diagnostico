## crear una clase llamada vehiculo capaz de procesar la informacion basica de los autos en una consencionaria. debera tener constructor y los atributos del vehiculo seran:
## patente, marca, modelo, kilometraje. crear metodos (de acceso) getter y (modificacion) aetter. mostrar por pantalla al menos un atributo y modificar el kilometraje. 
class vehiculo:
  def __init__(self, patente, marca, modelo , kilometraje):
  self.patente= patente
  self.marca= marca
  self.modelo= modelo 
 self.kilometraje=kilometraje

def get_kilometraje(self):
  return self.kilometraje=kilometraje 

def set_kilometraje(self,nuevo_lilometraje):
  self.kilometraje = nuevo_nuevo_kilometraje

vehiculo = vehiculo ("ABC123", "toyota", "corolla", 50000)

print("kilometraje actual:", vehiculo.get_kilometraje())

nuevo_kilometraje = 55000
vehiculo.set_kilometraje(nuevo-kilometraje)
print("kilometraje modificado:", vehiculo1.get_kilometraje())

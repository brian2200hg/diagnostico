## crear un programa un que simule la entrada a un boliche. debe dejar ingresar la edad del usuario, si es mayor a 18 por pantalla mostrar ingresar, de lo contrario mostrar por pantalla no puede entrar 
def simular_ingreso_boliche():
  edad = int(inout("ingrese su edad:"))
  if edad >= 18:
    print("puede ingrsar al boliche.")
  else:
    pint("no puede ingrsar al boliche.")

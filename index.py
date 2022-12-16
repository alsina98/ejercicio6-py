class Vehiculo(): 
    color = ''
    ruedas = 0
    puertas = 0


class Coche(Vehiculo):
    velocidad = 0.0
    cilindrada = ''

bmw = Coche()

bmw.color = 'white'
bmw.ruedas = 4
bmw.puertas = 2
bmw.velocidad = 250.0
bmw.cilindrada = '250cc'

print("Color:",bmw.color)
print("Ruedas:",bmw.ruedas)
print("Puertas:",bmw.puertas)
print("Velocidad:",bmw.puertas)
print("Cilindrada:",bmw.puertas)
bloques = int(input("Ingrese el número de bloques:"))

#
# Escribe tu código aquí.
#

contador = 1
altura = 0
suma = 0

while contador <= bloques:
    altura += 1
    
    contador += 1
    
    suma += contador

    if suma >= bloques:
        break

print("La altura de la pirámide:", altura)
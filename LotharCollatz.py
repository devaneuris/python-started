c0 = int(input("Escriba un numero entero:  "))

step = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    step +=1
    print(c0)
    
print("Pasos = " + str(step))

#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

#Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
#Si c0 ≠ 1, salta al punto 2.

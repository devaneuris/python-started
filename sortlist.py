miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

# fill list
for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

# sort list swapped=intercambio
while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

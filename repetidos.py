miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#

aux = []

for i in range(len(miLista)):
    # print(miLista[i])
    if miLista[i] in aux:
        continue
    
    aux.append(miLista[i])

print("La lista solo con elementos únicos:")
print(aux)

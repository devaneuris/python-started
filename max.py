miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in miLista:
   if i > mayor:
        mayor = i

print(mayor)
# El programa anterior realiza una comparación innecesaria, cuando el primer elemento se compara consigo mismo,
# slice
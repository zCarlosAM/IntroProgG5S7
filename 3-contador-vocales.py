vocales = {'a', 'e', 'i', 'o', 'u'}
contador_vocales = [0, 0, 0, 0, 0]

cadena = input("Ingrese una cadena de texto: ").lower()

for i in set(cadena) and vocales:
    if i == 'a':
        contador_vocales[0] += 1 
    elif i == 'e':
        contador_vocales[1] += 1
    elif i == 'i':
        contador_vocales[2] += 1
    elif i == 'o':
        contador_vocales[3] += 1
    elif i == 'u':
        contador_vocales[4] += 1
        
print("Cantidad de vocales en la cadena")
print("-" * 64)
print("A:", contador_vocales[0])
print("E:", contador_vocales[1])
print("I:", contador_vocales[2])
print("O:", contador_vocales[3])
print("U:", contador_vocales[4])
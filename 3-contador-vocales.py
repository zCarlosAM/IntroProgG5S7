import os
os.system("cls || clear")

vocales = "aeiou"
contador_vocales = [0, 0, 0, 0, 0]

cadena = input("Ingrese una cadena de texto: ").lower()

for i in cadena:
    if i in vocales:
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
      
print("-" * 64)      
print("Frecuencia de vocales en la cadena")
print("-" * 64)

for i in range(5):
    print(f"{vocales[i].upper()}: {contador_vocales[i]}")

print("-" * 64)
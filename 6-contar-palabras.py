import os
os.system("cls || clear")

texto = input("Ingrese una cadena de texto: ")

palabras = 0
for i in texto.split():
    palabras += 1
    
print("-" * 64)
print(f"El texto introducido contiene exactamente {palabras} palabras")
import os

os.system("cls || clear")
print("")
num = int(input("¿Cuántas calificaciones va a ingresar?: "))

print("-" * 64)
suma = 0
for i in range(1, num + 1):
    suma += int(input(f"Ingrese la calificación número {i}: "))
    
promedio = suma / num
print("-" * 64)
print(f"Su promedio es de {promedio}")
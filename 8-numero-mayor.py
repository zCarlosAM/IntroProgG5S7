import os
os.system("cls || clear")

cantidad = int(input("¿Cuántos números van a ingresarse?: "))

mayor = 0
menor = 0

print("-" * 64)
for i in range(cantidad):
    num = int(input(f"Ingrese el número #{i+1}: "))
    
    if i == 0:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

print("-" * 64)
print(f"El número mayor es: {mayor}")
print(f"Mientras que el número menor es: {menor}")
import os
os.system("cls || clear")

print("-" * 64)
print("Ingrese una lista de números enteros")
print("Escriba \"0\" para terminar")
print("-" * 64)

sum_pares = 0
sum_impares = 0
num = 1
i = 1

while num > 0:
    num = int(input(f"N°{i}: "))
    
    if num % 2 == 0:
        sum_pares += num
    else:
        sum_impares += num
    
    i += 1

print("-" * 64)
print("La suma de los números pares es de:", sum_pares)
print("Mientras que la de los impares es:", sum_impares)
print("-" * 64)
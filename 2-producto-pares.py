num = int(input("Ingrese un número entero positivo: "))
print("-" * 64)

print(f"Primeros {num} números pares: ", end="")

i = 0
contador = 0
prod = 1

while contador < num:
    if(i > 0 and i % 2 == 0):
        prod *= i
        print(i, end=" ")
        contador += 1
    i += 1

print(f"\nEl producto de estos números es: {prod}")
print("-" * 64)
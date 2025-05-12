num = int(input("Ingrese un número entero: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i
    
print(f"El factorial de este número es {factorial}")
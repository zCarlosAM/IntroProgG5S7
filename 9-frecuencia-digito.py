import os
os.system("cls || clear")

digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("-" * 64)
num = input("Ingrese un número entero: ")
print("-" * 64)

for i in num:
    if i == '0':
        digitos[0] += 1
    if i == '1':
        digitos[1] += 1
    if i == '2':
        digitos[2] += 1
    if i == '3':
        digitos[3] += 1
    if i == '4':
        digitos[4] += 1
    if i == '5':
        digitos[5] += 1
    if i == '6':
        digitos[6] += 1
    if i == '7':
        digitos[7] += 1
    if i == '8':
        digitos[8] += 1
    if i == '9':
        digitos[9] += 1
        
print("Frecuencia de dígitos de este número")

cont = 0
for i in digitos:
    print(f"{cont}: {i}")
    cont += 1
import os

def pantalla_inicial(saldo):
    print("-" * 64)
    print("CAJERO AUTOMÁTICO")
    print("-" * 64)
    print(f"Saldo actual: {saldo}")
    print("-" * 64)
    print("1. Depósito")
    print("2. Retiro")
    print("3. Salir")
    print("-" * 64)
    
    opcion = int(input("Operación a realizar: "))
    if opcion >= 1 and opcion <= 3:
        return opcion
        
def pantalla_deposito(saldo):
    print("-" * 64)
    print("DEPÓSITO")
    print("-" * 64)
    
    deposito = int(input("Ingrese la cantidad a depositar: "))
    print("-" * 64)
    if deposito <= 0:
        print("La cantidad introducida no es válida. ")
        input("Pulse cualquier tecla para continuar. ")
        return saldo
    
    saldo += deposito
    print("Correcto. Su saldo es ahora de: ", saldo)
    print("-" * 64)
    input("Pulse cualquier tecla para continuar. ")
    return saldo
    
def pantalla_retiro(saldo):
    print("-" * 64)
    print("RETIRO")
    print("-" * 64)
    
    retiro = int(input("Ingrese la cantidad a retirar: "))
    print("-" * 64)
    if retiro <= 0 or retiro > saldo:
        print("La cantidad introducida no es válida. ")
        input("Pulse cualquier tecla para continuar. ")
        return saldo
    
    saldo -= retiro
    print("Correcto. Su saldo es ahora de: ", saldo)
    print("-" * 64)
    input("Pulse cualquier tecla para continuar. ")
    return saldo
    
saldo = 100
ejecutando = True
while ejecutando:
    os.system("cls || clear")
    opcion = pantalla_inicial(saldo)
    
    os.system("cls || clear")
    if opcion == 1:
        saldo = pantalla_deposito(saldo)
    elif opcion == 2:
        saldo = pantalla_retiro(saldo)
    elif opcion == 3:
        ejecutando = False
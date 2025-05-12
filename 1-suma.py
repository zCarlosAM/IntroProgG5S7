def main():
    num = int(input("Ingrese un número entero positivo: "))
    sum = 0

    if num < 1:
        print("El número introducido no es válido")
        return
    
    for i in range(1, num + 1):
        sum += i

    print(f"La suma de los números del 1 al {num} es de: {sum}")

main()
print("Conversor Decimal ↔ Binario")

opcion = ""
while opcion != "3":
    print("\nElige una opción:")
    print("1. Convertir Decimal a Binario")
    print("2. Convertir Binario a Decimal")
    print("3. Salir")
    opcion = input("Opción (1/2/3): ")

    if opcion == "1":
        numero = input("Ingresa un número decimal: ")
        if numero.isdigit():
            numero_decimal = int(numero)
            if numero_decimal == 0:
                print("Binario: 0")
            else:
                binario = ""
                while numero_decimal > 0:
                    residuo = numero_decimal % 2
                    binario = str(residuo) + binario
                    numero_decimal = numero_decimal // 2
                print("Binario:", binario)
        else:
            print("Error: Debes ingresar un número entero positivo.")

    elif opcion == "2":
        numero = input("Ingresa un número binario: ")
        es_binario = True
        for digito in numero:
            if digito != "0" and digito != "1":
                es_binario = False
        if es_binario and numero != "":
            decimal = 0
            potencia = len(numero) - 1
            for digito in numero:
                decimal = decimal + int(digito) * (2 ** potencia)
                potencia = potencia - 1
            print("Decimal:", decimal)
        else:
            print("Error: Ingresa solo números binarios (compuestos de 0 y 1).")

    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Intenta otra vez.")
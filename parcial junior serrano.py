# Importamos la biblioteca para trabajar con archivos JSON
import json

# Diccionario para almacenar las cuentas bancarias
cuentas = {}

# Función para abrir una nueva cuenta
def abrir_nueva_cuenta(numero_cuenta, nombre_titular, saldo_inicial):
    if numero_cuenta not in cuentas:
        cuentas[numero_cuenta] = {"nombre_titular": nombre_titular, "saldo": saldo_inicial}
        print("Nueva cuenta creada.")
    else:
        print("El número de cuenta ya existe.")

# Función para depositar dinero en una cuenta
def depositar_en_cuenta(numero_cuenta, cantidad):
    if numero_cuenta in cuentas:
        cuentas[numero_cuenta]["saldo"] += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {cuentas[numero_cuenta]['saldo']}")
    else:
        print("Cuenta no encontrada.")

# Función para retirar dinero de una cuenta
def retirar_de_cuenta(numero_cuenta, cantidad):
    if numero_cuenta in cuentas:
        if cuentas[numero_cuenta]["saldo"] >= cantidad:
            cuentas[numero_cuenta]["saldo"] -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {cuentas[numero_cuenta]['saldo']}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Cuenta no encontrada.")

# Función para consultar el saldo de una cuenta
def consultar_saldo(numero_cuenta):
    if numero_cuenta in cuentas:
        saldo = cuentas[numero_cuenta]["saldo"]
        print(f"Saldo actual de la cuenta {numero_cuenta}: {saldo}")
    else:
        print("Cuenta no encontrada.")

# Función para listar todas las cuentas
def listar_todas_las_cuentas():
    print("Lista de cuentas:")
    for numero_cuenta, cuenta in cuentas.items():
        print(f"Número de cuenta: {numero_cuenta}, Titular: {cuenta['nombre_titular']}, Saldo: {cuenta['saldo']}")

# Función para guardar los datos en un archivo JSON
def guardar_datos(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(cuentas, archivo)
        print("Datos guardados en el archivo JSON.")

# Ejecución del programa
while True:
    print("\nBienvenido al Gestor de Cuentas Bancarias")
    print("1. Abrir Nueva Cuenta")
    print("2. Depositar en Cuenta")
    print("3. Retirar de Cuenta")
    print("4. Consultar Saldo")
    print("5. Listar Todas las Cuentas")
    print("6. Guardar Datos")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        numero_cuenta = input("Ingrese el número de cuenta: ")
        nombre_titular = input("Ingrese el nombre del titular: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        abrir_nueva_cuenta(numero_cuenta, nombre_titular, saldo_inicial)
    elif opcion == "2":
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        depositar_en_cuenta(numero_cuenta, cantidad)
    elif opcion == "3":
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        retirar_de_cuenta(numero_cuenta, cantidad)
    elif opcion == "4":
        numero_cuenta = input("Ingrese el número de cuenta: ")
        consultar_saldo(numero_cuenta)
    elif opcion == "5":
        listar_todas_las_cuentas()
    elif opcion == "6":
        nombre_archivo = input("Ingrese el nombre del archivo para guardar los datos: ")
        guardar_datos(nombre_archivo)
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

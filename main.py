def menu():
    print("\n--- Sistema de Caja ---")
    print("1. Registrar venta")
    print("2. Ver total en caja")
    print("3. Salir")

def main():
    caja = 0  # Aquí guardaremos el dinero acumulado
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            monto = float(input("Ingresa el monto de la venta: "))
            caja += monto
            print(f"Venta registrada: ${monto}")
        elif opcion == "2":
            print(f"Total en caja: ${caja}")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()git init

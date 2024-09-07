lista_compras = []

while True:
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        articulo = input("Ingresa el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"'{articulo}' ha sido agregado a la lista.")
    
    elif opcion == '2':
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("\nLista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i + 1}. {articulo}")
            
            indice = input("Ingresa el número del artículo que deseas eliminar: ")
            
            try:
                indice = int(indice) - 1 
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"'{eliminado}' ha sido eliminado de la lista.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    elif opcion == '3':
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("\nLista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i + 1}. {articulo}")

    elif opcion == '4':
        print("¡Gracias por usar la aplicación de lista de compras!")
        break
    
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

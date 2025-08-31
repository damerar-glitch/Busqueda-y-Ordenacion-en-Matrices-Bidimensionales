def buscar_valor(matriz, valor_buscar):
    """
    Función que busca un valor en una matriz bidimensional
    y devuelve su posición si se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscar:
                return (i, j)
    return None


def main():
    # Definir una matriz 3x3
    matriz = [
        [15, 23, 7],
        [42, 8, 91],
        [3, 67, 12]
    ]

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Valor a buscar
    valor_buscar = 8

    # Realizar la búsqueda
    resultado = buscar_valor(matriz, valor_buscar)

    # Mostrar resultados
    print(f"\nBuscando el valor: {valor_buscar}")

    if resultado:
        fila, columna = resultado
        print(f"¡Valor encontrado!")
        print(f"Posición: Fila {fila + 1}, Columna {columna + 1}")
        print(f"Coordenadas (índices): [{fila}][{columna}]")
    else:
        print("El valor no se encontró en la matriz.")


if __name__ == "__main__":
    main()
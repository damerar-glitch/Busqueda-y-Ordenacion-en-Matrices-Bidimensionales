def bubble_sort(arr):
    """
    Implementación del algoritmo Bubble Sort para ordenar un array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def ordenar_fila_matriz(matriz, fila):
    """
    Función que ordena una fila específica de la matriz
    """
    if fila < 0 or fila >= len(matriz):
        print("Número de fila inválido")
        return matriz

    # Crear una copia de la matriz para no modificar la original
    matriz_ordenada = [fila_matriz[:] for fila_matriz in matriz]

    # Ordenar la fila especificada
    matriz_ordenada[fila] = bubble_sort(matriz_ordenada[fila][:])

    return matriz_ordenada


def main():
    # Definir una matriz 3x3
    matriz = [
        [15, 23, 7],
        [42, 8, 91],
        [3, 67, 12]
    ]

    print("Matriz original:")
    for i, fila in enumerate(matriz):
        print(f"Fila {i}: {fila}")

    # Fila a ordenar (0-indexed)
    fila_a_ordenar = 1  # Segunda fila

    # Ordenar la fila especificada
    matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

    print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
    for i, fila in enumerate(matriz_ordenada):
        print(f"Fila {i}: {fila}")

    # Mostrar comparación
    print(f"\nComparación de la fila {fila_a_ordenar}:")
    print(f"Original: {matriz[fila_a_ordenar]}")
    print(f"Ordenada: {matriz_ordenada[fila_a_ordenar]}")


if __name__ == "__main__":
    main()
import numpy as np
import time


# rekurencyjna implementacja algorytmu strassena
def strassen(a, b):
    n = a.shape[0]
    # warunek wyjścia dla funkcji rekurencyjnej
    if n == 1:
        return a * b
    # rekurencja
    # nc ma być najmniejszą potęgą 2 większą od n
    nc = int(2**np.ceil(np.log2(n)))
    # macierz zer dla c
    c = np.zeros((nc, nc))
    # padding zerami
    temp = np.zeros((nc, nc))
    temp[:n, :n] = a
    a = temp
    temp = np.zeros((nc, nc))
    temp[:n, :n] = b
    b = temp
    # podzielenie na ćwiartki
    l = nc // 2

    a11 = a[:l, :l]
    a12 = a[:l, l:]
    a21 = a[l:, :l]
    a22 = a[l:, l:]

    b11 = b[:l, :l]
    b12 = b[:l, l:]
    b21 = b[l:, :l]
    b22 = b[l:, l:]
    # działania strassena
    m1 = strassen(a11 + a22, b11 + b22)
    m2 = strassen(a21 + a22, b11)
    m3 = strassen(a11, b12 - b22)
    m4 = strassen(a22, b21 - b11)
    m5 = strassen(a11 + a12, b22)
    m6 = strassen(a21 - a11, b11 + b12)
    m7 = strassen(a12 - a22, b21 + b22)

    c[:l, :l] = m1 + m4 - m5 + m7
    c[:l, l:] = m3 + m5
    c[l:, :l] = m2 + m4
    c[l:, l:] = m1 - m2 + m3 + m6
    # docięcie macierza do rozmiaru
    c = c[:n, :n]

    return c


if __name__ == "__main__":
    # stworzenie dwóch macierzy
    x1 = np.random.random((4, 4))
    x2 = np.random.random((4, 4))

    # wywołanie funkcji strassen
    matrix_mul = strassen(x1, x2)
    print(matrix_mul)

    # sprawdzenie błędów
    print(matrix_mul - x1.dot(x2))

    # porówananie czasów wykonywania
    start = time.time()
    for _ in range(10000):
        matrix_mul = strassen(x1, x2)
    stop = time.time()
    print("strassen:", stop - start)

    start2 = time.time()
    for _ in range(10000):
        matrix_dot = x1.dot(x2)
    stop2 = time.time()
    print("numpy.dot:", stop2 - start2)

def sumar_matrices(m1, m2):
    resultado = []

    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)

    return resultado


def multiplicar_matrices(m1, m2):
    resultado = []

    for i in range(len(m1)):
        fila = []
        for j in range(len(m2[0])):
            suma = 0
            for k in range(len(m2)):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado
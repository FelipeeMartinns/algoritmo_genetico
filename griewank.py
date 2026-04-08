import math

def griewank(x):
    soma = 0
    produto = 1

    for i in range(len(x)):
        soma += (x[i] ** 2) / 4000
        produto *= math.cos(x[i] / math.sqrt(i + 1))

    return soma - produto + 1
import random

def mutacao(individuo, taxa, limite):
    for i in range(len(individuo)):
        if random.random() < taxa:
            individuo[i] = round(random.uniform(-limite, limite), 2)
    return individuo
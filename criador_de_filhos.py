import random


def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1)-1)
    filho = pai1[:ponto] + pai2[ponto:]
    return filho
import random

def criar_individuo(tamanho, limite):
    return [round(random.uniform(-limite, limite), 2) for _ in range(tamanho)]


def criar_populacao(tamanho_populacao, tamanho_individuo, limite_numero_de_cada_individuo):
    return [criar_individuo(tamanho_individuo, limite_numero_de_cada_individuo) for _ in range(tamanho_populacao)]


import random


def avaliar_populacao(populacao, funcao):
    return [funcao(individuo) for individuo in populacao]


def selecao_torneio(pop, fitness, num_participantes=3):
    selecionados = random.sample(list(zip(pop, fitness)), num_participantes)
    melhor = min(selecionados, key=lambda x: x[1])
    return melhor[0]
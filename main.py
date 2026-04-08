from criador_de_populacao import criar_populacao
from avaliador import avaliar_populacao, selecao_torneio
from criador_de_filhos import crossover
from mutacao import mutacao
from griewank import griewank
from akley import ackley


TAMANHO_POPULACAO = 10
TAMANHO_INDIVIDUO = 2
LIMITE = 30
GERACOES = 100
TAXA_MUTACAO = 0.1
FORMULA=griewank
#FORMULA=ackley


pop = criar_populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, LIMITE)



for geracao in range(GERACOES):

    fitness = avaliar_populacao(pop,FORMULA)

    nova_pop = []

    for _ in range(len(pop)):

        pai1 = selecao_torneio(pop, fitness)
        pai2 = selecao_torneio(pop, fitness)

        filho = crossover(pai1, pai2)
        filho = mutacao(filho, TAXA_MUTACAO, LIMITE)

        nova_pop.append(filho)

    pop = nova_pop

    fitness = avaliar_populacao(pop, FORMULA)
    melhor = min(fitness)
    print(f"Geração {geracao}: melhor = {round(melhor, 4)}")



fitness_final = avaliar_populacao(pop,FORMULA)
melhor_final = min(fitness_final)

print("\nMelhor resultado final:", round(melhor_final, 6))


erro = abs(melhor_final)
porcentagem = (1 / (1 + erro)) * 100

print(f"Aproximação: {round(porcentagem, 2)}%")
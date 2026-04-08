import math

def ackley(lista):
    n = len(lista)
    
    sum1 = sum(num**2 for num in lista)
    sum2 = sum(math.cos(2 * math.pi * num2) for num2 in lista)
    
    return -20 * math.exp(-0.2 * math.sqrt(sum1/n)) \
           - math.exp(sum2/n) \
           + 20 + math.e
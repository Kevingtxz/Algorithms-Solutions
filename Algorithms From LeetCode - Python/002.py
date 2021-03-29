# T[] é um array que armazena os tamanhos em mm
def my_function():   
    N = int(input())
    K = int(input())
    Y = 0
    result = 0
    T = []

    for x in range(K):
        T.append(int(input()))

    T.sort()

    if(K >= N):
        return T[K-N]

    # Z = Contagem de pedaços
    Z = 0
    # Y = Representação do mínimo tamanho
    Y = T[0]
    Z = 0
    while(True):
        result = Y
        for x in T:
            Z += (x//Y)
            if(Z >= N):
                return result
        Z = 0
        Y -= 1
        if(Y == 0):
            return 'Não existem tamanhos possíveis'
    return result
print(my_function())
#  Enquanto o número de pedaços contados (Z) for menor que o número necessário (N), o algoritmo vai ficar diminuindo 1 ml em (Y), que é a variável que armazena o maior valor possível atual no algoritmo e vai testar quantos pedaços desse tamanho será possível
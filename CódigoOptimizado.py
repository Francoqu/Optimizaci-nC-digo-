def criba_eratostenes(n):
    primos = [True] * n
    primos[0] = primos[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n, i):
                primos[j] = False
    return [i for i, es_primo in enumerate(primos) if es_primo]

n = 100
print(criba_eratostenes(n))

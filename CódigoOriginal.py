def encontrar_primos(n):
    primos = []
    for i in range(2, n):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

n = 100
print(encontrar_primos(n))

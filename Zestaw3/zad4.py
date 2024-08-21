# Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

def euler(n):
    e = [0] * (n + 3) # nie bede juz myslal na ktore miejsce po przecinku to ma wskoczyc i jak
    # miejsce n+1 bedzie niedokladne wiec wyprintujemy n,
    # dogenerowane wiecej by zaokraglenie sie nie psulo
    e[0] = 2 # i pomijamy 2 pierwsze wyrazy

    b = 2 # 2!
    fact = 3

    while b < 10 ** (n + 3):
        a = 10 # bo pomijamy to jedno 1 co nam zrobi pusty przelot
        for j in range(1, n + 3):
            e[j] += a // b
            a %= b
            a *= 10
            if e[j] > 9: # zwiekszenie cyfry po lewej gdy ta po prawe bedzie wieksza od 9
                e[j - 1] += 1
                e[j] %= 10
        
        b *= fact
        fact += 1
    
    for ch in range(n + 2, n, -1): # zaokragli koniec
        if e[ch] >= 5:
            e[ch - 1] += 1
            e[ch] %= 10
    print(e[0], end='.')
    for k in range(1, n + 1):
        print(e[k], end='')

euler(1000)
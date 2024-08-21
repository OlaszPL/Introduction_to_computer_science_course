# Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory cyfr
# występujące w liczbie są identyczne. Na przykład:
# 13(10) = 31(4) i 23(10) = 113(4)
# 18(10) = 102(4) i 33(10) = 201(4)
# 107(10) = 1223(4) i 57(10) = 321(4).
# Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca
# długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.

# w calym ciagu maja byc 4 zgodne do wszystkich wyrazow w podciagu

def same_digits_in_sys_four(a, b):
    # 4 bo jest tyle cyfr 0-3
    t_a = [False] * 4
    t_b = [False] * 4

    while a > 0:
        t_a[a % 4] = True
        a //= 4
    
    while b > 0:
        t_b[b % 4] = True
        b //= 4
    
    return t_a == t_b

def find_four_consistent(T):
    n = len(T)
    max_cnt = 0

    for i in range(n - 1):
        cnt = 1
        for j in range(i + 1, n):
            if same_digits_in_sys_four(T[i], T[j]):
                cnt += 1

        max_cnt = max(max_cnt, cnt)

    return max_cnt

T = [13, 18, 107, 23, 33, 57]

print(find_four_consistent(T))
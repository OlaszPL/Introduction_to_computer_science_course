# Proszę napisać program obliczający pierwiastek całkowitoliczbowy z
# liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n

n = int(input())
sum = 0
iter = 0

for i in range(1, n + 1, 2):
    sum += i
    iter += 1
    if sum > n:
        print(iter - 1)
        break

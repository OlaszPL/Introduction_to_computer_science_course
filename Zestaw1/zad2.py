#Proszę znaleźć wyrazy początkowe zamiast 1, 1 o najmniejszej sumie, aby w ciągu analogicznym
#do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.(zał: a > b)

# do tego najlepsza będzie zagnieżdżona pętla for w for, bo ładnie najpierw sprawdzi wszystkie
# opcje zmiany jednej
# po czym opcje zmiany drugiej. !!!!!Zał: a < b (bo to jest jednak ciąg)

#szukamy 2 sąsiednich wyrazów, których suma da 2023 - bo tak to działa w tym ciągu

should_end = False

for i in range(2, 2023 + 1):
    if not should_end:
        for j in range(1, i // 2 + 1):

            a, b = j, i

            while (a + b) < 2023:
                a, b = b, a + b

            if (a + b) == 2023:
                print(j, i) #bo i, j stały się początkowmi wyrazami, które przeszły w pętli while
                should_end = True
                


# for i in range(2, 2023 + 1):
#     for j in range(1, i // 2 + 1):

#         a = j
#         b = i - j

#         while b < 2023:
#             a, b = b, a + b
#         if b == 2023:
#             print(j, i - j)


# a, b = 17, 49

# while a <= 2023:
#     print(a)
#     a, b = b, a + b
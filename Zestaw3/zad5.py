# Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym
# wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu.
# Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

def zad5(n): # ktora co do wielkosci, ostatnia w tablicy to bedzie ta, bo pierwsza bedzie najwieksza, nadmiar bedzie wywalany z niej
    last_n = [0] * n

    while True:
        x = int(input())
        if x == 0:
            break

        for i in range(n):
            if x > last_n[i]:
                x, last_n[i] = last_n[i], x #na przemian bedziemy zamieniac
        
    return last_n[-1]
    
print(zad5(10))
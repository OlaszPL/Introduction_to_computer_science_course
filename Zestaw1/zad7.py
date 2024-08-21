#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego. 1 1 2 3 5 8 13 21

n = int(input())

a, b = 1, 1

while (a * b) < n:
    a, b = b, a + b

if a * b == n:
    print('True')
else:
    print('False')
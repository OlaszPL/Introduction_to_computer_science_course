#Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
#sumie. 1 1 2 3 5 8 13 21

s = int(input())

a, b = 1, 1
curr = 0

while curr < s:
    curr += a
    a, b = b, a + b

if curr == s:
    print('True')
else:
    an, bn = 1, 1
    while curr > s: #jak idąc od początku przejdziemy poza sumę to odejmujemy odpowiednią ilość początkowych wyrazów
        curr -= an
        an, bn = bn, an + bn
    if curr == s:
        print('True')
    else:
        print('None')
# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2, 3, 5.
# Jedynka też jest taką liczbą. Proszę napisać program, który wylicza ile takich liczb znajduje się w przedziale od 1 do n włącznie.

def zad4(n):

    count = 0
    i = 1
    
    while i <= n:
        j = i

        while j <= n:
            k = j
            
            while k <= n:
                count += 1
                print(k)
                k *= 5

            j *= 3

        i *= 2

    return count

n = int(input())
print('Liczba cyfr: ' + str(zad4(n)))

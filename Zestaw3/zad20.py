# Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę napisać funkcję, która
# zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie jego elementów każdy czynnik pierwszy
# występuje co najwyżej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.


MAX_NUM_VAL = 1000

def longest_part(t):
    factors = [0] * (MAX_NUM_VAL + 1)
    t_len = len(t)
    max_len = 0
    right = left = 0 # pointery

    while right < t_len:
        if max(factors) <= 1:
            copy_num = t[right]

            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] += 1
                    copy_num //= d

                d += 1
            right += 1

        else:
            copy_num = t[left]

            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] -= 1
                    copy_num //= d

                d += 1
            left += 1

        if max(factors) <= 1:
            max_len = right - left

    return max_len


t= [2,23,33,35,7,4,6,7,5,11,13,22]
print(longest_part(t))
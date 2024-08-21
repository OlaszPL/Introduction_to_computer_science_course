# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek
# oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład
# "ula" → 117, 108, 971 oraz "exe" → 101, 120, 101.
# Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu
# z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1.
# Dodatkowo funkcja powinna wypisać znaleziony wyraz.

def czy_samogloska(a):
    return 1 if a in ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó'] else 0

def wyraz(s1, s2):
    samogloski_s1 = 0
    suma_asci_s1 = 0
    for el in s1:
        samogloski_s1 += czy_samogloska(el)
        suma_asci_s1 += ord(el)

    n = len(s2)

    def rek(samogloski_s1, suma_asci_s1, i = 0, res = ''):
        if samogloski_s1 < 0 or suma_asci_s1 < 0:
            return False
        if samogloski_s1 == suma_asci_s1 == 0:
            print(res)
            return True
        if i == n:
            return False
        
        return rek(samogloski_s1 - czy_samogloska(s2[i]), suma_asci_s1 - ord(s2[i]), i + 1, res + s2[i]) or rek(samogloski_s1, suma_asci_s1, i + 1, res)
    
    return rek(samogloski_s1, suma_asci_s1)

print(wyraz('ula', 'studntexe'))
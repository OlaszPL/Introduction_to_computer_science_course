# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których
# są zbudowane są identyczne, na przykład "ula" → 117, 108, 97 oraz "exe" → 101, 120, 101.
# Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1.
# Dodatkowo funkcja powinna wypisać znaleziony wyraz.

def czy_samogloska(a):
    samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
    return 1 if a in samogloski else 0

def wyraz(s1, s2):
    ilosc_sam_s1 = 0
    suma_ascii_s1 = 0

    for i in range(len(s1)):
        ilosc_sam_s1 += czy_samogloska(s1[i])
        suma_ascii_s1 += ord(s1[i])

    n = len(s2)

    def rek(s2, n, ilosc_sam_s1, suma_ascii_s1, i = 0, res = ''):

        if ilosc_sam_s1 < 0 or suma_ascii_s1 < 0: # odjelismy za duzo
            return False
        if ilosc_sam_s1 == 0 and suma_ascii_s1 == 0:
            return True, res
        if i == n:
            return False
        
        return rek(s2, n, ilosc_sam_s1, suma_ascii_s1, i + 1, res) or rek(s2, n, ilosc_sam_s1 - czy_samogloska(s2[i]), suma_ascii_s1 - ord(s2[i]), i + 1, res + s2[i])
    
    return rek(s2, n, ilosc_sam_s1, suma_ascii_s1)

print(wyraz('ula', 'saffkexe'))
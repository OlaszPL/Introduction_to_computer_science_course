# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na kawałki, tak aby każdy
# kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję cutting(s), która zwraca liczbę
# sposobów pocięcia słowa na kawałki.
# Przykłady:
# print(cutting(’student’)) # wypisze 2 bo stu-dent, stud-ent
# print(cutting(’sesja’)) # wypisze 3 bo se-sja, ses-ja, sesj-a
# print(cutting(’ocena’)) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
# print(cutting(’informatyka’)) # wypisze 36

def czy_samogloska(a):
    return a in ['a', 'e', 'i', 'o', 'u', 'y']

def cutting(s):
    n = len(s)

    def rek(s, n, i = 0, cnt = 0): # cnt zlicza samogloski, ale takze liczbe podzialow
        if i == n:
            return cnt
        
        if czy_samogloska(s[i]):
            cnt += 1
        
        if cnt == 2: # bo przypadek kiedy zlepimy 2 samogloski nas nie obchodzi
            return 0
        
        elif cnt == 1:
            return rek(s, n, i + 1, 0) + rek(s, n, i + 1, cnt) # 0 - kiedy dzielimy za samoglaska, cnt kiedy nie dzielimy
        
        return rek(s, n, i + 1, 0) # w przypadku kiedy cnt == 0 to dzielimy i lecimy dalej
        
    return rek(s, n)

print(cutting('student')) # wypisze 2 bo stu-dent, stud-ent
print(cutting('sesja')) # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting('ocena')) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
print(cutting('informatyka')) # wypisze 36
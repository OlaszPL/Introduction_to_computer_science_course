# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na kawałki, tak aby każdy
# kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję cutting(s), która zwraca liczbę
# sposobów pocięcia słowa na kawałki.
# Przykłady:
# print(cutting(’student’)) # wypisze 2 bo stu-dent, stud-ent
# print(cutting(’sesja’)) # wypisze 3 bo se-sja, ses-ja, sesj-a
# print(cutting(’ocena’)) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
# print(cutting(’informatyka’)) # wypisze 36

def czy_samogloska(a):
    return 1 if a in ['a', 'e', 'i', 'o', 'u', 'y'] else 0

def cutting(s):
    n = len(s)

    def rek(i = 0, cnt = 0):
        if i == n:
            return cnt
        
        if czy_samogloska(s[i]):
            cnt += 1
        
        if cnt == 2:
            return 0
        
        elif cnt == 1:
            return rek(i + 1, cnt) + rek(i + 1, 0)
        
        return rek(i + 1, cnt)

    return rek()

print(cutting('informatyka'))
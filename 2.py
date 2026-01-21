'''
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon,
ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon,
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
'''

import random
számok_listája = []
Run = True
for i in range(11):
    ran_num = random.randint(1, 3)
    számok_listája.append(ran_num)

print(f'{számok_listája}')

useri = int(input('Adj meg egy számot 1 és 3 között, amit ki szeretnél törölni  a listából\n'))

while useri in számok_listája:
        számok_listája.remove(useri)

print(f'{számok_listája}')

'''
3. Feladat
Írj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg betűt, csupán egy ENTER-t üt!

A program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne
(a felhasználó korábban még nem adta meg)! A program NE különböztesse meg a kis- és nagybetűket egymástól,
de olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.

Ha a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!

Minden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!
'''

betűklistája = []
Run = True

while Run == True:
    useri = (input('Adj meg betűket, ha 0-át vagy ENTER-t ütsz, a program leáll\n'))
    if useri != '' and useri != '0':
        if useri in betűklistája:
            print('Ezt a betűt már rögzítettem')
        else:
            betűklistája.append(useri)
            betűklistája.sort()
            print(f'{betűklistája}')
    else:
        Run = False
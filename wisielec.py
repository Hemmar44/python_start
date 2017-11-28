haslo = "Niedzwiedź polarny"
wisielec = list('Wisielec')
test = len('Wisielec')
kategoria = 'Zwierze'
litery = []
litery=list(haslo)
odkryte = []
liczba_liter = len(litery)
flag = False

print('Kategoria: %s' % kategoria)

def modyfikuj(haslo):
    do_odkrycia = []
    for i in range(0, liczba_liter):
        if(litery[i] == ' '):
            do_odkrycia.append(litery[i])
        else:
            do_odkrycia.append('_')

    return do_odkrycia

odkryte = modyfikuj(haslo)
wisisz = []
print(''.join(odkryte))

while(len(wisisz) < test):
    literka = input("Podaj literkę: ")

    for j in range(0, liczba_liter):
        if(litery[j].lower() == literka):
            odkryte[j] = litery[j]
            flag = True            
    if(flag == False):
        wisisz.append(wisielec[0])
        wisielec.pop(0)

    flag = False    
            
    print(''.join(odkryte))
    print(''.join(wisisz))

    if(odkryte == litery):
        print("Brawo odkryłeś całe hasło!")
        break

    if(''.join(wisisz) == "Wisielec"):
        print('Przegrałeś!!! będziesz wisiał!!!')
        break

    zgadujesz = input("Czy chcesz odgadnąć hasło (T/N)?: ")

    if(zgadujesz.lower() == "t"):
        proba = input("Podaj haslo; ")
        if proba == haslo:
            print("Brawo poprawne hasło!")
            break
        else:
            print("Niepoprawne hasło graj dalej")

print('Dziękuję za udział w grze')
    

    




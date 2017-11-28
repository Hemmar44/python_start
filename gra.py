import random
liczba = random.randint(0,100)

proby = int(input('Ile chcesz mieć prób? Wpisz liczbę od jeden do 10: '))



print('Odgaduj liczbę od 1 do 100 masz %s prób' % proby)
for i in range(0, proby):
    
    odp = int(input("Podaj liczbę: "))

    print(odp)

    if odp == liczba:
        print('Brawo prawidłowa odpowiedź')
        break
    elif odp < liczba:
        print('Za mało')
    else:
        print('Za dużo')

print('Dzięki za grę')
print(liczba)

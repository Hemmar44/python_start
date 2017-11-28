myAge = 34

i = 0;

while i <= myAge:
    if i % 2 == 0:
        print(i)
    i = i + 1

while i <= myAge:
    print(i)
    i = i + 2

toppings = ['pasztet', 'bekon', 'ser', 'makrela', 'podwawelska']

for i in range(0,5):
    print('%s %s' %(i, toppings[i]))
    

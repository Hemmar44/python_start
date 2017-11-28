class Cars:
    def kola(self):
        return 4
    def kolor():
        pass
    def biegi(self,x):
        return x


class Audi(Cars):
    pass

class Skoda(Cars):
    pass

class A4(Audi):
    pass

class Fabia(Skoda):
    def rocznik(self, rocznik):
        return rocznik
    def wypiszRocznik(self, x):
        print('Rocznik twojego auta to %s' % self.rocznik(x))



mojeAuto = Fabia()

print(mojeAuto.kola())
print(mojeAuto.biegi(4))
print(mojeAuto.rocznik(2000))
print(mojeAuto.wypiszRocznik(2012))

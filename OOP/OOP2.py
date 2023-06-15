class calisan:
    personel_sayisi = 0
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas
        calisan.personel_sayisi += 1

print(calisan.personel_sayisi)
calisan1 = calisan("Ali", 5000)
print(calisan.personel_sayisi)
calisan2 = calisan("Ahmet", 6000)
print(calisan.personel_sayisi)

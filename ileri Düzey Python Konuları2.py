import sys

# ------------------------
# 1. Metaclass örneği
# ------------------------
class OtomatikIsim(type):
    def __new__(cls, name, bases, dct):
        dct["sinif_adi"] = name
        return super().__new__(cls, name, bases, dct)

class Arac(metaclass=OtomatikIsim):
    def yaz(self):
        print(f"Sınıf adı: {self.sinif_adi}")

a = Arac()
a.yaz()

# ------------------------
# 2. __slots__ ile bellek optimizasyonu
# ------------------------
class Ogrenci:
    __slots__ = ["ad", "yas"]  # Bellekte sabit yer ayırır

    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

o = Ogrenci("Mithat", 24)
print(f"{o.ad}, {o.yas} yaşında")

# ------------------------
# 3. Hafıza karşılaştırması
# ------------------------
class Normal:
    def __init__(self):
        self.x = 1
        self.y = 2

n = Normal()
print("Normal nesne boyutu:", sys.getsizeof(n))

s = Ogrenci("Ali", 20)
print("Slots kullanılan nesne boyutu:", sys.getsizeof(s))

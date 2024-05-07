class Telebe:
    def __init__(self, ad, soyad, nomre):
        self.ad = ad
        self.soyad = soyad
        self.nomre = nomre

    def melumatlari_goster(self):
        return f"{self.ad} {self.soyad} - {self.nomre}"

class Sinif:
    def __init__(self, sinif_adi, telebeler=None):
        self.sinif_adi = sinif_adi
        self.telebeler = telebeler if telebeler else []

    def telebe_daxilet(self, telebe):
        self.ogrenciler.append(telebe)

    def telebe_sil(self, nomre):
        for telebe in self.telebeler:
            if telebe.nomre == nomre:
                self.ogrenciler.remove(telebe)
                return f"{telebe.ad} {telebe.soyad} sinifden silindi."
        return "telebe tapilmadi."

    def sinif_listesi(self):
        if self.telebeler:
            return [Telebe.melumatlari_goster() for telebe in self.telebeler]
        else:
            return "sinifde telebe yoxdur."

# Örnekler oluştur
ogrenci1 = Telebe("Ali", "Yılmaz", 101)
ogrenci2 = Telebe("Ayşe", "Demir", 102)

sinif1 = Sinif("9/A")
sinif1.telebe_daxilet(ogrenci1)
sinif1.telebe_daxilet(ogrenci2)

# Sınıf işlemleri
print("Sınıf Adı:", sinif1.sinif_adi)
print("Sınıf Listesi:", sinif1.sinif_listesi())
print(sinif1.telebe_sil(102))
print("Güncel Sınıf Listesi:", sinif1.sinif_listesi())

class Student:
    def __init__(self, isim, yas, sinifi):
        self.isim = isim
        self.yas = yas
        self.sinifi = sinifi

    def display_info(self):
        print(f"İsim: {self.isim}, Yas: {self.yas}, sinifisi: {self.sinifi}")

    def study(self, subject):
        print(f"{self.isim} is studying {subject}")
ogrenciler.append(student2)
ogrenci.append(student3)

for ogretmen in ogretmenler:
    print("Öğretmen Adı :", ogretmen.isim, "Yaşı:", ogretmen.yas, "Bölümü :", ogretmen.bolumu)


for ogrenci in ogrenciler:
    print("Öğrenci Adı :", ogrenci.isim, "Yaşı:", ogrenci.yas, "Sınıfı :", ogrenci.sinifi)
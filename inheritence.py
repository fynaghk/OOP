class İshchiler():
    def __init__(self, ad, maash, sahe):
        print("İşçi heyəti")
        self.ad = ad
        self.maash = maash
        self.sahe = sahe

    def meulmat(self):
        print("Melumatlar:")
        print("Ad:", self.ad, "Maaş:", self.maash, "İşlədiyi sahə:", self.sahe)

    def maashi_artir(self, miqdar):
        print("Maaşınız artdı")
        self.maash += miqdar


class Mudur(İshchiler):
    def __init__(self, ad, maash, sahe, ishchileri):
        super().__init__(ad, maash, sahe)
        self.ishchileri = ishchileri

    def print(self):
        print("Melumatlar:")
        print("Ad:", self.ad, "Maaş:", self.maash, "İşlədiyi sahə:", self.sahe, "İşçi sayı:", self.ishchileri)

ishchi = İshchiler("Nağıyeva Fidan", 600, "laborant")
ishchi.meulmat()
ishchi.maashi_artir(100)
print("--------------------")
mudur = Mudur("Cavid Aliyev", 5000, "Müdür", 30)
mudur.print()

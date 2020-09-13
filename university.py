class Universitet:
    def __init__(self, telebe_sayi=1000, mezun_sayi=500):
        self.telebe_sayi = telebe_sayi
        self.mezun_sayi = mezun_sayi
    def print(self):
        print(f"Telebe sayi: {self.telebe_sayi}")
        print(f"Mezun sayi: {self.mezun_sayi}")

bdu_telebeleri  = Universitet(22000, 12000)
adu_telebeleri = Universitet(10000, 7000)
bmu_telebeleri = Universitet()
bdu_telebeleri.print()
print("---------------------------")
adu_telebeleri.print()
print("---------------------------")
bmu_telebeleri.print()

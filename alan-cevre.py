import math

class AlanCevreHesaplama():


    baslik = "Seçeceğiniz geometrik şeklin alanını veya çevresini bulan uygulama..."
    giris = """
    (1) = Dikdörtgen
    (2) = Üçgen
    (3) = Daire
    """

    print(baslik, giris, sep="\n")

    def __init__(self):
        self.tercih()

    def tercih(self):
        self.durum = input("Alan için 1, çevre için 2'ye basınız.")
        if self.durum not in ["1", "2"]:
            print("Geçersiz bir numara girdiniz. İşleminiz iptal ediliyor.")
            return False

        islem = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

        if islem == "1":
            self.dikdortgen()
        elif islem == "2":
            self.ucgen()
        elif islem == "3":
            self.daire()
        else:
            print("Doğru bir işlem numarası girmediniz. Lütfen tekrar deneyiniz! ")
            

    def dikdortgen(self):
        try:    
            k = float(input("Dikdörtgen kısa kenarı: "))
            u = float(input("Dikdörtgen uzun kenarı: "))
        except:
            print("Düzgün bir sayı girilmediği için işlem iptal ediliyor...")
        else:
            if self.durum == "1":
                print("Uzun kenarı {}, Kısa kenarı {} olan dikdörtgenin alanı {}".format(u,k,(k*u)))
            else:
                print("Uzun kenarı {}, Kısa kenarı {} olan dikdörtgenin çevresi {}".format(u,k,((u*2)+(k*2))))

    def daire(self):
        try:
            r = float(input("Dairenin yarıçapı: "))
        except:
            print("Düzgün bir sayı girilmediği için işlem iptal ediliyor...")
        else:
            if self.durum == "1":
                print("Yarıçapı {} olan dairenin alanı {}".format(r, (3.14*r*r)))
            else:
                print("Yarıçapı {} olan dairenin çevresi {}".format(r, (2*3.14*r)))

    def ucgen(self):
        try:
            t = float(input("Üçgenin tabanı: "))
            h = float(input("Üçgenin yüksekliği: "))
            y1 = input("Üçgen yan kenar: ")   
        except:
            print("Düzgün bir sayı girilmediği için işlem iptal ediliyor...")
        else:
            if self.durum == "1":
                print("Tabanı {}, yüksekliği {} olan üçgenin alanı {}".format(t, h, (h*t/2)))
            else:
                print("Tabanı {}, yan kenarı {} olan üçgenin çevresi {}".format(t, y1, (t+y1*2)))


if __name__ == "__main__":
    AlanCevreHesaplama(),
    input("Çıkış için bir tuşa basınız...")




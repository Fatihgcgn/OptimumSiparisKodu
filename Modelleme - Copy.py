import random

print("Hesaplama Islemleri icin tus giriniz...")
sayac = int(input("Kac adet ornek istiyorsunuz:"))
i = 0

SatinMiktar_a = 50
SatinMiktar_b = 60
SatinMiktar_c = 70
optimumKar50 = 0
optimumKar60 = 0
optimumKar70 = 0


def KarHesap(Talep_k, SatinMiktar_k):
    if Talep >= SatinMiktar_k:
        SatisKaybi = (Talep_k - SatinMiktar_k) * 20
        SatisGeliri = SatinMiktar_k * 50
        HurdaGeliri = 0
    else:
        SatisKaybi = 0
        SatisGeliri = Talep_k * 50
        HurdaGeliri = (SatinMiktar_k - Talep_k) * 5

    Maliyet = SatinMiktar_k * 30
    Kar = SatisGeliri + HurdaGeliri - Maliyet - SatisKaybi
    return Kar


def egerfonksiyon(Talep_t, SatinMiktar_t):
    if Talep_t >= SatinMiktar_t:
        SatisKaybi = (Talep_t - SatinMiktar_t) * 20
        SatisGeliri = SatinMiktar_t * 50
        HurdaGeliri = 0
    else:
        SatisKaybi = 0
        SatisGeliri = Talep_t * 50
        HurdaGeliri = (SatinMiktar_t - Talep_t) * 5

    Maliyet = SatinMiktar_t * 30
    Kar = SatisGeliri + HurdaGeliri - Maliyet - SatisKaybi

    print(i + 1, ".günün bilgileri:", "Rs1:", Rs1, "Talep Tipi:", TalepTipi, "Rs2:", Rs2, "Talep:", Talep_t,
          "Satıs Geliri", SatisGeliri, "Satıs Kaybı:", SatisKaybi, "Maliyet:", Maliyet, "Hurda Geliri:",
          HurdaGeliri, "Kar:", Kar)
    return Kar


while i < sayac:
    Rs1 = random.randint(0, 100)
    Rs2 = random.randint(0, 100)
    Talep = 0
    Kar = 0
    TalepTipi = "bos"
    Maliyet = 0
    HurdaGeliri = 0
    SatisGeliri = 0
    SatisKaybi = 0

    if Rs1 >= 0 and Rs1 <= 45:  # YUKSEKKKK
        TalepTipi = "YUKSEK"
        if Rs2 >= 0 and Rs2 <= 3:

            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 4 and Rs2 <= 8:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 9 and Rs2 <= 23:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 24 and Rs2 <= 43:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 44 and Rs2 <= 78:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 79 and Rs2 <= 93:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 94 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        else:
            print("Error YUKSEKKK")

    elif Rs1 >= 46 and Rs1 <= 75:  # ORTAAAA
        TalepTipi = "ORTA"
        if Rs2 >= 0 and Rs2 <= 10:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 11 and Rs2 <= 28:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 29 and Rs2 <= 68:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 69 and Rs2 <= 88:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 89 and Rs2 <= 96:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 96 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        else:
            print("Error ORTAAA")

    elif Rs1 >= 76 and Rs1 <= 100:  # DUSUKKKK
        TalepTipi = "DUSUK"
        if Rs2 >= 0 and Rs2 <= 44:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 45 and Rs2 <= 66:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 67 and Rs2 <= 82:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 83 and Rs2 <= 94:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        elif Rs2 >= 95 and Rs2 <= 100:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_a)
            optimumKar50 += KarHesap(Talep, SatinMiktar_a)

        else:
            print("Error DUSUKKK")

    i = i + 1

i = 0
print("--------------------------------------------------")
while i < sayac:
    Rs1 = random.randint(0, 100)
    Rs2 = random.randint(0, 100)
    Talep = 0
    Kar = 0
    TalepTipi = "bos"
    Maliyet = 0
    HurdaGeliri = 0
    SatisGeliri = 0
    SatisKaybi = 0

    if Rs1 >= 0 and Rs1 <= 45:  # YUKSEKKKK
        TalepTipi = "YUKSEK"
        if Rs2 >= 0 and Rs2 <= 3:

            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 4 and Rs2 <= 8:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 9 and Rs2 <= 23:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 24 and Rs2 <= 43:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 44 and Rs2 <= 78:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 79 and Rs2 <= 93:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 94 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        else:
            print("Error YUKSEKKK")

    elif Rs1 >= 46 and Rs1 <= 75:  # ORTAAAA
        TalepTipi = "ORTA"
        if Rs2 >= 0 and Rs2 <= 10:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 11 and Rs2 <= 28:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 29 and Rs2 <= 68:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 69 and Rs2 <= 88:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 89 and Rs2 <= 96:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 96 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        else:
            print("Error ORTAAA")

    elif Rs1 >= 76 and Rs1 <= 100:  # DUSUKKKK
        TalepTipi = "DUSUK"
        if Rs2 >= 0 and Rs2 <= 44:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 45 and Rs2 <= 66:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 67 and Rs2 <= 82:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 83 and Rs2 <= 94:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        elif Rs2 >= 95 and Rs2 <= 100:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_b)
            optimumKar60 += KarHesap(Talep, SatinMiktar_b)

        else:
            print("Error DUSUKKK")

    i = i + 1

i = 0
print("--------------------------------------------------")
while i < sayac:
    Rs1 = random.randint(0, 100)
    Rs2 = random.randint(0, 100)
    Talep = 0
    Kar = 0
    TalepTipi = "bos"
    Maliyet = 0
    HurdaGeliri = 0
    SatisGeliri = 0
    SatisKaybi = 0

    if Rs1 >= 0 and Rs1 <= 45:  # YUKSEKKKK
        TalepTipi = "YUKSEK"
        if Rs2 >= 0 and Rs2 <= 3:

            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 4 and Rs2 <= 8:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 9 and Rs2 <= 23:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 24 and Rs2 <= 43:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 44 and Rs2 <= 78:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 79 and Rs2 <= 93:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 94 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        else:
            print("Error YUKSEKKK")

    elif Rs1 >= 46 and Rs1 <= 75:  # ORTAAAA
        TalepTipi = "ORTA"
        if Rs2 >= 0 and Rs2 <= 10:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 11 and Rs2 <= 28:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 29 and Rs2 <= 68:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 69 and Rs2 <= 88:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 89 and Rs2 <= 96:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 96 and Rs2 <= 100:
            Talep = 100
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        else:
            print("Error ORTAAA")

    elif Rs1 >= 76 and Rs1 <= 100:  # DUSUKKKK
        TalepTipi = "DUSUK"
        if Rs2 >= 0 and Rs2 <= 44:
            Talep = 40
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 45 and Rs2 <= 66:
            Talep = 50
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 67 and Rs2 <= 82:
            Talep = 60
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 83 and Rs2 <= 94:
            Talep = 70
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        elif Rs2 >= 95 and Rs2 <= 100:
            Talep = 80
            egerfonksiyon(Talep, SatinMiktar_c)
            optimumKar70 += KarHesap(Talep, SatinMiktar_c)

        else:
            print("Error DUSUKKK")

    i = i + 1

opt50=optimumKar50 / SatinMiktar_a
opt60=optimumKar60 / SatinMiktar_b
opt70=optimumKar70 / SatinMiktar_c

print("\nOptimum Kar (50) icin:", optimumKar50 / SatinMiktar_a)
print("Optimum Kar (60) icin:", optimumKar60 / SatinMiktar_b)
print("Optimum Kar (70) icin :", optimumKar70 / SatinMiktar_c)

if opt50 >= opt60 and opt50 >= opt70:
    print("\nEn optimum sonuc icin 50 adet Gazete siparis verilmelidir!!!")

elif opt60 >= opt70 and opt60 >= opt50:
    print("\nEn optimum sonuc icin 60 adet Gazete siparis verilmelidir!!!")

elif opt70 >= opt50 and opt70 >= opt60:
    print("\nEn optimum sonuc icin 70 adet Gazete siparis verilmelidir!!!")
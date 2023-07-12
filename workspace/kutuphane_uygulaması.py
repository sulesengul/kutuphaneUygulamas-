import os
kitapListe = list()

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış

"""

def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı..")
    print("Ana menüye dönmek için 'enter'e basın.")
    input()


def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False
    
def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Çıkarma işlemi tamamlandı..")
        print("Ana menüye dönmek için 'enter'e basın.")
        input()

    else:
        print("Arattığınız kitap mevcut değildir.")
        print("Ana menüye dönmek için 'enter'e basın.")
        input()


def listele(liste:list):
    for i in liste:
        print("Kitap Adı: {} ----->>>>> Yazar Adı: {}".format(i[0],i[1]))

    print("Ana menüye dönmek için 'enter'e basın.")
    input()

while True:
    os.system("clear")
    print(menu)

    secim = input("İşleminizi seçiniz: ")

    if secim == "1":
        kitap_isim = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_isim,kitap_yazar)
        kitapEkle(kitap,kitapListe)

    elif secim == "2":
        kitap_isim = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_isim,kitap_yazar)
        kitapCikar(kitap,kitapListe)

    elif secim == "3":
        listele(kitapListe)

    elif secim == "q" or secim == "Q":
        print("Keyifli Okumalar...")
        quit()

    else:
        print("Hatalı giriş yaptımız.")
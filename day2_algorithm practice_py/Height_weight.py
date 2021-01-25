
i = int(input("1.luas persegi panjang \n2.luas bujur sangkar \nPilihan:"))


def luas_persegi_panjang():
    l = int(input("lebar: "))
    p = int(input("panjang: "))

    ls = l * p

    print (ls)

def luas_bujur_sangkar():
    l = int(input("sisi: "))
    print (l ** 2)

if i == 1:
    luas_persegi_panjang()
else:
    luas_bujur_sangkar()

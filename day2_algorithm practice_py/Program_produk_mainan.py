#Daffa aditya Rahman, 10,1A,11 ,10200031
#program mengihutung harga produk mainan
print ("            TOKO MAINAN ANAK")
print ("        ************************")
nama = input("masukan nama pembeli = ")
kode = input("masukan Kode mainan  = ")
while True:
    harga = input("masukan harga        = ")
    try:
        val = int(harga)
        if int(harga) < 0:
             print ("masukan angka positive!")
             continue
        break
    except ValueError:
        print("masukan angka!")

while True:
    jumlah = input("masukan jumlah       = ")
    try:
        val = int(jumlah)
        if int(jumlah) < 0:
             print ("masukan angka positive!")
             continue   
        break
    except ValueError:
        print("masukan angka!")

total = int(harga) * int(jumlah)

print ("=================================================")

print ("Nama Pembeli = ",nama)
print ("Kode Mainan  = ",kode)
print ("harga        = ",harga)
print ("Jumlah Beli  = ",jumlah)
print ("Total        = ",total)

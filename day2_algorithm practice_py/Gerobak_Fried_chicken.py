import datetime

    


print ("GEROBAK FRIED CHICKEN" "\n" "--------------------------------" "\n" "kode JenisPotong Harga" "\n" "D    Dada       RP.2500" "\n" "P    Paha        Rp.2000" "\n" "S    Sayap       RP.1500" "\n" "--------------------------------")

banyak_jenis = int(input("Banyak Jenis : "))
kode_potong = [] #input kode
banyak_potong = [] #banyak pesanan
jenis_potong = [] #jenis potongan
harga = [] #harga
jumlah = [] #jumlah
i = 0
while i < banyak_jenis:
  print("Jenis Ke - ", i+1)
  kode_potong.append(input("Kode Potong [D/P/S] : "))
  banyak_potong.append(int(input("Banyak Potong : ")))

  if kode_potong[i] == "D" or kode_potong[i] == "d":
    jenis_potong.append("Dada")
    harga.append("2500")
    jumlah.append(banyak_potong[i]*int("2500"))
  elif kode_potong[i] == "P" or kode_potong[i] == "p":
    jenis_potong.append("Paha")
    harga.append("2000")
    jumlah.append(banyak_potong[i]*int("2000"))
  elif kode_potong[i] == "S" or kode_potong[i] == "s":
    jenis_potong.append("Sayap")
    harga.append("1500")
    jumlah.append(banyak_potong[i]*int("1500"))
  else:
    jenis_potong.append("Kode Salah")
    harga.append("0")
    jumlah.append(banyak_potong[i]*int("0"))
  i = i + 1


print("       GEROBAK FRIED CHICKEN       ")
print("-----------------------------------")
print("No   Jenis   Harga   Banyak  Jumlah")
print("     Potong  Satuan  Potong  Harga ")
print("-----------------------------------")

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
  jumlah_bayar = jumlah_bayar + jumlah[a]
  print("%i    %s     %s      %i    %i" % (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
  a = a + 1
print("-----------------------------------")


pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("               Jumlah Bayar : Rp."'{:.0f}'.format(jumlah_bayar))
print("               Pajak 10%    : Rp."'{:.0f}'.format(pajak))
print("               Total Bayar  : Rp."'{:.0f}'.format(total_bayar))

x = datetime.datetime.now()

file = open("log.txt", "a")

file.write(x.strftime("%x :"))
file.write(str('{:.0f}'.format(total_bayar)))
file.write(" Ribu")
file.write("\n")



file.close()

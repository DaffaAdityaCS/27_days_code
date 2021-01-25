
def program_martabak():
    print("           *Selamat Datang di Toko Martabak Bersama*")
    print("=================================================================")
    print("Daftar Menu: ")
    print("1. Manis     2. Telur")
    print("Daftar Pilihan: ")
    print("1. Keju     Rp.15000    2. Telur  Rp.20000 \nToping Rp.2000 ")
    print("-----------------------------------------------------------------")
    
    balik_arr = []
    balik_arr.append(str(input("Memesan y/n: ")))
    
    
    while balik_arr[0] == 'y':
        balik_arr.clear()
        banyak_pesanan = int(input("Banyak Pesanan: "))
        kode_martabak = []
        jenis_martabak = []
        kode_toping = []
        topping = []
        harga = []
        harag_topping = []
        i = 0
        while i < banyak_pesanan:
            print("Pesanan Ke -", i+1)
            kode_martabak.append(int(input("Jenis martabak [1 atau 2]:")))
            

            if kode_martabak[i] == 1 :
                jenis_martabak.append("Manis")
                harga.append(15000)
            
            elif kode_martabak[i] == 2:
                jenis_martabak.append("Telur")
                harga.append(20000)

            else :
                jenis_martabak.append("tidak terdaftar")
                harga.append(0)
            i = i + 1

        n = 0
        while n < banyak_pesanan:
            print("Toping ke -", n + 1)
            kode_toping.append(input("kacang(k)/keju(k1)/susu(s)/saus(s1): "))

            if kode_toping[n] == "k" or kode_toping == "K":
                topping.append("kacang")
                harag_topping.append(2000)

            elif kode_toping[n] == "k1" or kode_toping == "K1":
                topping.append("keju")
                harag_topping.append(2000)
            
            elif kode_toping[n] == "s" or kode_toping == "S":
                topping.append("susu")
                harag_topping.append(2000)

            elif kode_toping[n] == "s1" or kode_toping == "S1":
                topping.append("saus")
                harag_topping.append(2000)

            else:
                topping.append("tidak Terdaftar")
                harag_topping.append(0)
            n = n + 1

        print(harga)
        print("    Toko Martabak Bersama ")
        print("------------------------------")
        print("No   Jenis   Harga   Topping     harga")
        print("------------------------------")

        jumlah_bayar = 0
        j = 0
        while j < banyak_pesanan:
            jumlah_bayar = jumlah_bayar + harga[j] + harag_topping[j]

            print((j+1, jenis_martabak[j], harga[j], topping[j], harag_topping[j] ))
            j = j + 1


        pajak = jumlah_bayar * 0.1
        total_bayar = jumlah_bayar + pajak 
        print("               Jumlah Bayar Rp.", jumlah_bayar)
        print("               Pajak 10% Rp", pajak)
        print("               Total Bayar Rp. ", total_bayar)
        print("     Terima Kasih Telah Berbelanja di Toko Kami ^_^")
        
        balik_arr.append(str(input("Memesan y/n: ")))
    return program_martabak
    



        
program_martabak()




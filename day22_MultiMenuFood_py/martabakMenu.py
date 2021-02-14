def martabak_program():
    print("             *Selamat Datang di Toko Martabak Bersama*")
    print("==================================================================")
    print("Daftar Menu: ")
    print("1A. Manis Keju          Rp.20000  |  2A. Telur Bebek 2    Rp.20000\n1B. Manis Coklat        Rp.20000  |  2B. Telur Bebek 3    Rp.25000\n1C. Manis Kacang        Rp.20000  |  2C. Telur Bebek 4    Rp.30000\n1D. Manis Blueberry     Rp.20000  |  2D. Telur Ayam 4     Rp.25000\n1E. Manis Strawberry    Rp.20000  |  2E. Telur Ayam 5     Rp.30000")
    print("------------------------------------------------------------------")
    print("Daftar Topping: ")
    print("1. Keju        Rp.2000\n2. Susu        Rp.2000\n3. Meses       Rp.2000\n4. Kacang      Rp.2000\n5. Saus        Rp.2000")
    print("__________________________________________________________________")
    
    ulang_arr = []
    ulang_arr.append(str(input("Membeli y/n: ")))

    while ulang_arr[0] == "y":
        ulang_arr.clear()
        banyak_pesanan = int(input("Banyak Pesanan: "))
        kode_martabak = []
        jenis_martabak = []
        kode_topping = []
        topping = []
        harga = []
        harga_topping = []
        i = 0
        while i < banyak_pesanan:
            print("Pesanan Ke-", i+1)
            kode_martabak.append(str(input("Pilih Martabak [1A/1B/1C/1D/1E atau 2A/2B/2C/2D/2E]: ")))
            
            if kode_martabak[i] == "1A" or kode_martabak[i] == "1a":
                jenis_martabak.append("Manis Keju")
                harga.append(20000)
            elif kode_martabak[i] == "1B" or kode_martabak[i] == "1b":
                jenis_martabak.append("Manis Coklat")
                harga.append(20000)
            elif kode_martabak[i] == "1C" or kode_martabak[i] == "1c":
                jenis_martabak.append("Manis Kacang")
                harga.append(20000)
            elif kode_martabak[i] == "1D" or kode_martabak[i] == "1d":
                jenis_martabak.append("Manis Blueberry")
                harga.append(20000)
            elif kode_martabak[i] == "1E" or kode_martabak[i] == "1e":
                jenis_martabak.append("Manis Strawberry")
                harga.append(20000)
            elif kode_martabak[i] == "2A" or kode_martabak[i] == "2a":
                jenis_martabak.append("Telur Bebek 2")
                harga.append(20000)
            elif kode_martabak[i] == "2B" or kode_martabak[i] == "2b":
                jenis_martabak.append("Telur Bebek 3")
                harga.append(25000)
            elif kode_martabak[i] == "2C" or kode_martabak[i] == "2c":
                jenis_martabak.append("Telur Bebek 4")
                harga.append(30000)
            elif kode_martabak[i] == "2D" or kode_martabak[i] == "2d":
                jenis_martabak.append("Telur Ayam 4")
                harga.append(25000)
            elif kode_martabak[i] == "2E" or kode_martabak[i] == "2e":
                jenis_martabak.append("Telur Ayam 5")
                harga.append(30000)
            else:
                jenis_martabak.append("Tidak dalam daftar")
                harga.append(0)
            i = i + 1

        n = 0
        while n < banyak_pesanan:
            print("Pilihan Ke-", n + 1)
            kode_topping.append(input("Jenis Topping [1/2/3/4/5]: "))

            if kode_topping[n] == "1":
                topping.append("Keju")
                harga_topping.append(2000)
            elif kode_topping[n] == "2":
                topping.append("Susu")
                harga_topping.append(2000)
            elif kode_topping[n] == "3":
                topping.append("Meses")
                harga_topping.append(2000)
            elif kode_topping[n] == "4":
                topping.append("Kacang")
                harga_topping.append(2000)
            elif kode_topping[n] == "5":
                topping.append("Saus")
                harga_topping.append(2000)
            else:
                topping.append("Tidak dalam daftar")
                harga_topping.append(0)
            n = n + 1


        print("__________________________________________________________________")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("             Toko Martabak Bersama ")
        print("-----------------------------------------------")
        print("No    Jenis       Topping   Harga")
        print("-----------------------------------------------")
        jumlah_bayar = 0 
        j = 0
        while j < banyak_pesanan:
            jumlah_bayar = jumlah_bayar[j] + jenis_martabak[j] + topping[j]
            print('%i   %s    %s     %i' % (j+1, jenis_martabak[j], topping[j], jumlah_bayar[j]))
            j = j + 1


        pajak = jumlah_bayar * 0.1
        total_bayar = jumlah_bayar + pajak 
        print("-----------------------------------------------")
        print("                 Jumlah Bayar   Rp.", jumlah_bayar)
        print("                 Pajak 10%      Rp.", pajak)
        print("                 Total Bayar    Rp.", total_bayar)
        print("-----------------------------------------------")

        bayar = int(input("Bayar Rp."))
        kembalian = bayar - total_bayar
        print("Kembalian Anda  Rp.", kembalian)
        print("Terima Kasih Telah Membeli di Toko Kami (^_^)")
        ulang_arr.append(str(input("Membeli y/n: ")))
    return martabak_program
        

martabak_program()
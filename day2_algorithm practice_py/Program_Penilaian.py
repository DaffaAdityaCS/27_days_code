print ("            PROGRAM MENHITUNG NILAI MATAKULIAH PRAKTEK")
print ("--------------------------------------------------------------------")

matakuliah = str(input("Masukan Nama Matakuliah: "))
while True:
    pertemuan = input("masukan Jumlah Pertemuan = ")
    try:
        val = int(pertemuan)
        if int(pertemuan) < 0:
             print ("masukan angka positive!")
             continue
        break
    except ValueError:
        print("masukan angka!")

while True:
    hadir = input("masukan Jumlah hadir = ")
    try:
        val = int(hadir)
        if int(hadir) < 0:
             print ("masukan angka positive!")
             continue
        break
    except ValueError:
        print("masukan angka!")

totalabsen = (int(hadir) * 100)/ int(pertemuan) 
print ("Nilai absen yang didapat dari perhitungan diatas adalah: "'{:.1f}'.format(totalabsen))

while True:
    tugas = input("masuka Nilai Tugas yang diberikan oleh dosen = ")
    try:
        val = int(tugas)
        if int(tugas) < 0:
             print ("masukan angka positive!")
             continue
        break
    except ValueError:
        print("masukan angka!")

while True:
    project = input("masukan Nilai Project yang diberikan oleh dosen = ")
    try:
        val = int(project)
        if int(project) < 0:
             print ("masukan angka positive!")
             continue
        break
    except ValueError:
        print("masukan angka!")
print("----------------------------------------------------------------------")


nilai_absen = 20 / 100 * int(totalabsen)
nilai_tugas = 25 / 100 * int(tugas)
nilai_project = 55 / 100 * int(project) 
total_nilai = nilai_absen + nilai_tugas + nilai_project
print ("----------------------------------------------------------------------")
print ("nilai absen (20%) anda adalah : "'{:.1f}'.format(nilai_absen))
print ("nilai Tugas (25%) anda adalah : "'{:.1f}'.format(nilai_tugas))
print ("nilai Project (55%) anda adalah : "'{:.1f}'.format(nilai_project))

print ("----------------------------------------------------------------------")

print("pada mata kuliah: ",matakuliah)
print("anda mendapatkan Total Nilai: ",total_nilai)
if total_nilai >= 80:
    print("Dengan Grade: A \nSelamat anda : lulus")
elif total_nilai > 70:
    print("Dengan Grade: B \nSelamat anda : lulus")
elif total_nilai > 60:
    print("dengan Grade: C \nSelamat anda : lulus")
elif total_nilai > 31:
    print("dengan Grade: D \nanda : Tidak lulus")
else:
    print("degan Grade: E \nanda : Tidak lulus")

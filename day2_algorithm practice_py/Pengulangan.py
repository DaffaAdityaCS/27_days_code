for i in range(2):
    print("data ke -" + str(i+1))
    nim = int(input("masukan NIM anda: "))
    uts = int(input("masukan Nilai UTS : "))
    uas = int(input("masukana nilai UAS: "))
    hasil = (uts + uas) / 2
    print ("NIM andalah %i nilai UTS anda %i nilai Uas anda %i Total nilai adalah %i" % (nim,uts,uas,hasil), "\n" "-------------------------------")

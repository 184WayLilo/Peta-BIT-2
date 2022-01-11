
RAM = int(input("Masukkan Jumlah Ram(GB): "))
Blok = int(input("Masukkan jumlah blok/unit: "))
Kaprog = int(input("Masukan kapasitas program(GB): "))


#konversi gb ke mbps
GB = 1024

#konversi ram gb ke mbps
KonRam = RAM * GB

#mencari ukuran 1 blok
Ublok = KonRam / Blok

#konversi program gb ke mbps
Konprog = Kaprog * GB

#menghitung blok yang terpakai
Blok1 = Konprog / Ublok

#menghitung blok yang tidak terpakai
Blok0 = Blok - Blok1


print("============Inputan Program============")
print("Kapasitas RAM: ",KonRam," MBps" )
print("Blok/unit: ",Ublok," KBps" )
print("Kapasitas Program 1: ",Konprog," MBps" )
print("============Output Program============")
print("Jumlah Blok Bernilai 1 = ", Blok1, "Unit")
print("Jumlah Blok Bernilai 0 = ", Blok0, "Unit")
print("Pengalokasian Blok Bernilai 1 = ", Blok1, " Terpakai pada program 1")
print("Pengalokasian Blok Bernilai 0 = ", Blok0, " Kapasitas blok yang tidak digunakan")
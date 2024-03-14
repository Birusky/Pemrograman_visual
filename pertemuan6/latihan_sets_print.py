# Membuat dua set
prodi_teknik = {"Teknik Informatika", "Teknik Elektro", "Teknik Mesin"}
prodi_sosial = {"Ilmu Komunikasi", "Manajemen", "Ilmu Hubungan Internasional"}

# Menampilkan tipe data set
print("Tipe data prodi_teknik adalah", type(prodi_teknik))
print("Tipe data prodi_sosial adalah", type(prodi_sosial))

# Menampilkan data set
print("Data prodi_teknik:", prodi_teknik)
print("Data prodi_sosial:", prodi_sosial)
print("--------------------------------------------")

# Iterasi melalui set
for prodi in prodi_teknik:
    print(prodi)

print("--------------------------------------------")

# Menampilkan jumlah elemen dalam set
print("Jumlah elemen dalam prodi_teknik:", len(prodi_teknik))

# Memeriksa keberadaan elemen dalam set
if "Teknik Elektro" in prodi_teknik:
    print("Yes, 'Teknik Elektro' is an item in prodi_teknik.")

# Menambahkan elemen ke dalam set
prodi_teknik.add("Teknik Sipil")
print("Set setelah menambahkan Teknik Sipil:", prodi_teknik)

prodi_teknik.update(["Teknik Lingkungan", "Teknik Industri", "Teknik Geologi"])
print("Set setelah update:", prodi_teknik)

# Menghapus elemen dari set (metode 1)
prodi_teknik.remove("Teknik Informatika")
print("Set setelah menghapus Teknik Informatika:", prodi_teknik)

# Menghapus elemen dari set (metode 2)
prodi_teknik.discard("Teknik Lingkungan")
print("Set setelah menghapus Teknik Lingkungan:", prodi_teknik)

# Menghapus elemen terakhir dari set
prodi_teknik.pop()
print("Set setelah melakukan pop:", prodi_teknik)

# Mengosongkan set
prodi_teknik.clear()
print("Set setelah di-clear:", prodi_teknik)

# Menghapus set
del prodi_teknik
print("--------------------------------------------")

# Gabungan dua set
set1 = {"Teknik Informatika", "Teknik Elektro", "Teknik Mesin"}
set2 = {"Ilmu Komunikasi", "Manajemen", "Ilmu Hubungan Internasional"}
set3 = set1.union(set2)
print("Union dari set1 dan set2:", set3)
print("--------------------------------------------")

# Set1 mengambil salinan semua elemen dari set2
set1 = {"Teknik Informatika", "Teknik Elektro", "Teknik Mesin"}
set2 = {"Ilmu Komunikasi", "Manajemen", "Ilmu Hubungan Internasional"}
set1.update(set2)
print("Set1 setelah update dari set2:", set1)

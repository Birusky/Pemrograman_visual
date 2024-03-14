# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
print("Apakah a lebih besar dari b?", a > b)

# Cek apakah b lebih besar dari a
print("Apakah b lebih besar dari a?", b > a)

# Cek apakah a sama dengan b
print("Apakah a sama dengan b?", a == b)

# Hitung PPN a jika lebih dari 10000
ppn_a = 0.12 * a if a > 10000 else 0
print("PPN a:", ppn_a)

# Hitung PPN b jika lebih dari 50000
ppn_b = 0.12 * b if b > 50000 else 0
print("PPN b:", ppn_b)

# Tambahkan kedua PPN dan cek dengan boolean
total_ppn = ppn_a + ppn_b
print("Apakah total PPN lebih dari 0?", total_ppn > 0)

# Hapus a dan b, cek dengan boolean
del a, b
print("Apakah a masih ada?", "a" in locals())
print("Apakah b masih ada?", "b" in locals())

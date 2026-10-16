nama = input("Masukkan nama siswa: ")

mapel = [
    "AGAMA", "PPKN", "BAHASA INDONESIA", "MATEMATIKA", "BAHASA INGGRIS",
    "IPAS", "KKA", "DPPLG", "SENI BUDAYA", "SEJARAH",
    "BAHASA JEPANG", "INFORMATIKA", "KEMINANGKABAUAN","BAHASA JERMAN"
]

nilai = []

for pelajaran in mapel:
    n = float(input(f"Masukkan nilai {pelajaran}: "))
    nilai.append(n)

average = sum(nilai) / len(nilai)
nilai_min = min(nilai)
nilai_max = max(nilai)

print("\n===== HASIL NILAI SEMESTER =====".upper())
print(f"NAMA: {nama.upper()}")
print(f"RATA-RATA: {average:.2f}")
print(f"NILAI TERENDAH: {nilai_min}")
print(f"NILAI TERTINGGI: {nilai_max}")
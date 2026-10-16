# Program Pemesanan Tiket Pesawat

print("=== PEMESANAN TIKET PESAWAT ===")

# Input nama
nama = input("Masukkan nama penumpang : ")

# Daftar tujuan
print("\nDaftar Tujuan:")
print("1. Jakarta")
print("2. Bandung")
print("3. Surabaya")
print("4. Bali")

pilihan = int(input("Pilih tujuan (1-4): "))

# Daftar kelas
print("\nKelas Tiket:")
print("1. Ekonomi")
print("2. Bisnis")
print("3. First Class")

kelas = int(input("Pilih kelas (1-3): "))

# Jadwal keberangkatan
print("\nJadwal Keberangkatan:")
print("1. 08:00 WIB")
print("2. 13:00 WIB")
print("3. 19:00 WIB")

jadwal = int(input("Pilih jadwal (1-3): "))

# Jumlah tiket
jumlah_tiket = int(input("Jumlah tiket: "))

# Menentukan tujuan
if pilihan == 1:
    tujuan = "Jakarta"
elif pilihan == 2:
    tujuan = "Bandung"
elif pilihan == 3:
    tujuan = "Surabaya"
elif pilihan == 4:
    tujuan = "Bali"
else:
    tujuan = "Tidak tersedia"

# Menentukan harga berdasarkan kelas
if kelas == 1:
    nama_kelas = "Ekonomi"

    if pilihan == 1:
        harga = 1000000
    elif pilihan == 2:
        harga = 800000
    elif pilihan == 3:
        harga = 1200000
    elif pilihan == 4:
        harga = 1500000
    else:
        harga = 0

elif kelas == 2:
    nama_kelas = "Bisnis"

    if pilihan == 1:
        harga = 2000000
    elif pilihan == 2:
        harga = 1800000
    elif pilihan == 3:
        harga = 2200000
    elif pilihan == 4:
        harga = 2500000
    else:
        harga = 0

elif kelas == 3:
    nama_kelas = "First Class"

    if pilihan == 1:
        harga = 3000000
    elif pilihan == 2:
        harga = 2800000
    elif pilihan == 3:
        harga = 3200000
    elif pilihan == 4:
        harga = 3500000
    else:
        harga = 0

else:
    nama_kelas = "Tidak tersedia"
    harga = 0

# Menentukan jadwal keberangkatan
if jadwal == 1:
    waktu = "08:00 WIB"
elif jadwal == 2:
    waktu = "13:00 WIB"
elif jadwal == 3:
    waktu = "19:00 WIB"
else:
    waktu = "Tidak tersedia"

# Perhitungan biaya
subtotal = harga * jumlah_tiket
pajak = subtotal * 0.1
total_bayar = subtotal + pajak

# Output struk
print("\n===== STRUK PEMESANAN =====")
print("Nama Penumpang :", nama)
print("Tujuan         :", tujuan)
print("Kelas          :", nama_kelas)
print("Keberangkatan  :", waktu)
print("Harga Tiket    : Rp", harga)
print("Jumlah Tiket   :", jumlah_tiket)
print("Subtotal       : Rp", subtotal)
print("Pajak 10%      : Rp", pajak)
print("Total Bayar    : Rp", total_bayar)
print("============================")
print("Terima kasih telah memesan tiket pesawat!")
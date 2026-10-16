import random

# ======================================
# DATA SOAL
# ======================================
soal = [
    {
        "negara": "Indonesia",
        "opsi": ["Jakarta", "Bangkok", "Tokyo", "Seoul"],
        "jawaban": "A"
    },
    {
        "negara": "Jepang",
        "opsi": ["Beijing", "Tokyo", "Manila", "Hanoi"],
        "jawaban": "B"
    },
    {
        "negara": "Thailand",
        "opsi": ["Bangkok", "Paris", "Roma", "Berlin"],
        "jawaban": "A"
    },
    {
        "negara": "Malaysia",
        "opsi": ["Jakarta", "Kuala Lumpur", "Doha", "Kairo"],
        "jawaban": "B"
    },
    {
        "negara": "Singapura",
        "opsi": ["Singapura", "Seoul", "Madrid", "Lisbon"],
        "jawaban": "A"
    },
    {
        "negara": "Filipina",
        "opsi": ["Manila", "Tokyo", "Canberra", "Ottawa"],
        "jawaban": "A"
    },
    {
        "negara": "Vietnam",
        "opsi": ["Hanoi", "Moskow", "Athena", "Lima"],
        "jawaban": "A"
    },
    {
        "negara": "Korea Selatan",
        "opsi": ["Seoul", "Pyongyang", "Dubai", "Riyadh"],
        "jawaban": "A"
    },
    {
        "negara": "China",
        "opsi": ["Shanghai", "Beijing", "Hongkong", "Taipei"],
        "jawaban": "B"
    },
    {
        "negara": "India",
        "opsi": ["Mumbai", "New Delhi", "Karachi", "Kathmandu"],
        "jawaban": "B"
    },
    {
        "negara": "Arab Saudi",
        "opsi": ["Mekkah", "Riyadh", "Doha", "Abu Dhabi"],
        "jawaban": "B"
    },
    {
        "negara": "Amerika Serikat",
        "opsi": ["New York", "Los Angeles", "Washington DC", "Chicago"],
        "jawaban": "C"
    },
    {
        "negara": "Inggris",
        "opsi": ["London", "Manchester", "Liverpool", "Birmingham"],
        "jawaban": "A"
    },
    {
        "negara": "Prancis",
        "opsi": ["Lyon", "Paris", "Marseille", "Nice"],
        "jawaban": "B"
    },
    {
        "negara": "Jerman",
        "opsi": ["Hamburg", "Munich", "Berlin", "Frankfurt"],
        "jawaban": "C"
    },
    {
        "negara": "Italia",
        "opsi": ["Roma", "Milan", "Napoli", "Turin"],
        "jawaban": "A"
    },
    {
        "negara": "Australia",
        "opsi": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "jawaban": "C"
    },
    {
        "negara": "Kanada",
        "opsi": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
        "jawaban": "B"
    },
    {
        "negara": "Brasil",
        "opsi": ["Rio de Janeiro", "Brasilia", "Sao Paulo", "Salvador"],
        "jawaban": "B"
    },
    {
        "negara": "Mesir",
        "opsi": ["Kairo", "Alexandria", "Giza", "Luxor"],
        "jawaban": "A"
    }
]

# ======================================
# HUKUMAN UNTUK YANG KALAH
# ======================================
hukuman = [
    "Menyanyi satu lagu.",
    "Joget selama 30 detik.",
    "Membacakan pantun lucu.",
    "Push up 10 kali.",
    "Menirukan suara hewan.",
    "Membuat semua pemain tertawa."
]

# ======================================
# TAMPILAN AWAL
# ======================================
print("====================================")
print(" GAME TEBAK IBU KOTA NEGARA ")
print("====================================")

jumlah_pemain = int(input("Masukkan jumlah pemain : "))

# Menyimpan skor pemain
data_skor = {}

# ======================================
# GAME DIMULAI
# ======================================
for pemain in range(jumlah_pemain):

    print("\n------------------------------------")
    nama = input(f"Masukkan nama pemain ke-{pemain+1} : ")
    print(f"Selamat bermain, {nama}!")
    print("------------------------------------")

    skor = 0

    # Acak soal
    random.shuffle(soal)

    # Menampilkan 20 soal
    for i in range(20):

        print(f"\nSoal {i+1}")
        print(f"Apa ibu kota dari {soal[i]['negara']}?")

        print("A.", soal[i]["opsi"][0])
        print("B.", soal[i]["opsi"][1])
        print("C.", soal[i]["opsi"][2])
        print("D.", soal[i]["opsi"][3])

        jawaban = input("Jawaban Anda (A/B/C/D) : ").upper()

        if jawaban == soal[i]["jawaban"]:
            print("Jawaban Benar!")
            skor += 5
        else:
            print("Jawaban Salah!")
            print("Jawaban yang benar adalah", soal[i]["jawaban"])

    # Simpan skor
    data_skor[nama] = skor

# ======================================
# PAPAN SCORE
# ======================================
print("\n====================================")
print("           PAPAN SCORE")
print("====================================")

# Mengurutkan skor tertinggi
ranking = sorted(data_skor.items(), key=lambda x: x[1], reverse=True)

for i, pemain in enumerate(ranking):
    print(f"{i+1}. {pemain[0]} = {pemain[1]} poin")

print("====================================")

# ======================================
# JUARA DAN YANG KALAH
# ======================================
juara = ranking[0]
kalah = ranking[-1]

print(f"\nJUARA : {juara[0]}")
print(f"SKOR TERTINGGI : {juara[1]} poin")

print(f"\nYANG KALAH : {kalah[0]}")
print(f"SKOR TERENDAH : {kalah[1]} poin")

# Hukuman random
hukuman_terpilih = random.choice(hukuman)

print("\n====================================")
print("             HUKUMAN")
print("====================================")
print(f"{kalah[0]} harus : {hukuman_terpilih}")
print("====================================")

print("\nTerima kasih telah bermain!")
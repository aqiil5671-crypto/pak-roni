
import datetime

# --- Fungsi menentukan predikat berdasarkan nilai ---
def hitung_predikat(nilai):
    if nilai >= 90:
        return "A (Sangat Baik)"
    elif nilai >= 80:
        return "B (Baik)"
    elif nilai >= 70:
        return "C (Cukup)"
    elif nilai >= 60:
        return "D (Kurang)"
    else:
        return "E (Sangat Kurang)"

# --- Input data siswa ---
def input_data_siswa():
    print("=== INPUT DATA SISWA ===")
    nama = input("Nama siswa     : ")
    nis = input("NIS            : ")
    kelas = input("Kelas          : ")
    semester = input("Semester       : ")
    tahun = input("Tahun Ajaran   : ")
    return {
        "nama": nama,
        "nis": nis,
        "kelas": kelas,
        "semester": semester,
        "tahun": tahun
    }

# --- Input nilai mata pelajaran lengkap ---
def input_nilai():
    print("\n=== INPUT NILAI ===")
    mata_pelajaran = [
        "Pendidikan Agama",
        "Pendidikan Pancasila",
        "Bahasa Indonesia",
        "Matematika",
        "Ilmu Pengetahuan Alam (IPA)",
        "Ilmu Pengetahuan Sosial (IPS)",
        "Bahasa Inggris",
        "Pendidikan Jasmani, Olahraga dan Kesehatan",
        "Seni Budaya",
        "Informatika"
    ]
    
    nilai_mapel = {}
    for mapel in mata_pelajaran:
        while True:
            try:
                nilai = float(input(f"Masukkan nilai {mapel}: "))
                nilai_mapel[mapel] = nilai
                break
            except ValueError:
                print("⚠️ Nilai harus berupa angka! Silakan coba lagi.")
    return nilai_mapel

# --- Membuat dan mencetak rapor ---
def buat_rapor(data_siswa, nilai_mapel):
    tanggal = datetime.date.today().strftime("%d-%m-%Y")
    total = sum(nilai_mapel.values())
    rata_rata = total / len(nilai_mapel)
    predikat = hitung_predikat(rata_rata)

    # Header rapor
    rapor = []
    rapor.append("===================================================")
    rapor.append("                 RAPOR SISWA")
    rapor.append("===================================================")
    rapor.append(f"Nama Siswa  : {data_siswa['nama']}")
    rapor.append(f"NIS         : {data_siswa['nis']}")
    rapor.append(f"Kelas       : {data_siswa['kelas']}")
    rapor.append(f"Semester    : {data_siswa['semester']}")
    rapor.append(f"Tahun Ajaran: {data_siswa['tahun']}")
    rapor.append("---------------------------------------------------")
    rapor.append(f"{'Mata Pelajaran':40} {'Nilai':>6} {'Predikat':>20}")
    rapor.append("---------------------------------------------------")

    # Daftar nilai tiap mapel
    for mapel, nilai in nilai_mapel.items():
        rapor.append(f"{mapel:<40} {nilai:>6} {hitung_predikat(nilai):>20}")

    rapor.append("---------------------------------------------------")
    rapor.append(f"Rata-rata Nilai : {rata_rata:.2f}")
    rapor.append(f"Predikat Umum   : {predikat}")
    rapor.append(f"Tanggal Cetak   : {tanggal}")
    rapor.append("===================================================")
    rapor.append("Guru Wali : ____________________________")
    rapor.append("Orang Tua : ____________________________")
    rapor.append("===================================================")

    hasil_rapor = "\n".join(rapor)

    # Tampilkan rapor di layar
    print("\n" + hasil_rapor)

# --- Program utama ---
if __name__ == "__main__":
    data_siswa = input_data_siswa()
    nilai_mapel = input_nilai()
    buat_rapor(data_siswa, nilai_mapel)
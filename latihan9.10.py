# mengkonversi huruf mutu menjadi angka mutu
def konversi_huruf_ke_angka(rangga_huruf):
    if rangga_huruf == 'A':
        return 4
    elif rangga_huruf == 'AB':
        return 3.5
    elif rangga_huruf == 'B':
        return 3
    elif rangga_huruf == 'BC':
        return 2.5
    elif rangga_huruf == 'C':
        return 2
    elif rangga_huruf == 'D':
        return 1
    elif rangga_huruf == 'E':
        return 0
    else:
        return None  # Jika yang diinput tidak valid

# menghitung IPS
def hitung_ips(rangga_angka_mutu):
    rangga_SKS = [2, 2, 2, 3, 4, 3, 4]  # SKS masing-masing mata kuliah
    rangga_total_sks = sum(rangga_SKS)
    rangga_total_nilai = sum([a * b for a, b in zip(rangga_angka_mutu, rangga_SKS)])
    return rangga_total_nilai / rangga_total_sks

# menentukan status kelulusan
def tentukan_status_kelulusan(rangga_IPS):
    if rangga_IPS >= 2.75:
        return "Tetap"
    elif 2.00 < rangga_IPS < 2.75:
        return "Percobaan"
    elif rangga_IPS <= 2.00:
        return "Tidak Lulus"

# Input data mahasiswa
nama_mahasiswa = input("Masukkan Nama Mahasiswa: ")
NIM_mahasiswa = input("Masukkan NIM Mahasiswa: ")

# Input huruf mutu untuk setiap mata kuliah
rangga_huruf_mutu_agama = input("Masukkan Huruf Mutu Pendidikan Agama: ")
rangga_huruf_mutu_pancasila = input("Masukkan Huruf Mutu Pendidikan Pancasila: ")
rangga_huruf_mutu_inggris = input("Masukkan Huruf Mutu Bahasa Inggris 1: ")
rangga_huruf_mutu_pdi = input("Masukkan Huruf Mutu Pengolahan Data dan Informasi: ")
rangga_huruf_mutu_ptik = input("Masukkan Huruf Mutu Pengantar TI dan Komunikasi: ")
rangga_huruf_mutu_diskrit = input("Masukkan Huruf Mutu Matematika Diskrit: ")
rangga_huruf_mutu_pemrograman = input("Masukkan Huruf Mutu Pemrograman Dasar: ")

# Konversi huruf mutu ke angka mutu
rangga_angka_mutu = [
    konversi_huruf_ke_angka(rangga_huruf_mutu_agama),
    konversi_huruf_ke_angka(rangga_huruf_mutu_pancasila),
    konversi_huruf_ke_angka(rangga_huruf_mutu_inggris),
    konversi_huruf_ke_angka(rangga_huruf_mutu_pdi),
    konversi_huruf_ke_angka(rangga_huruf_mutu_ptik),
    konversi_huruf_ke_angka(rangga_huruf_mutu_diskrit),
    konversi_huruf_ke_angka(rangga_huruf_mutu_pemrograman)
]

# Hitung IPS
rangga_IPS = hitung_ips(rangga_angka_mutu)

# Tentukan status kelulusan
rangga_status_kelulusan = tentukan_status_kelulusan(rangga_IPS)

# Tampilkan hasil
print("\n===========================")
print(f"Nama Mahasiswa: {nama_mahasiswa}")
print(f"NIM Mahasiswa: {NIM_mahasiswa}")
print(f"IPS: {IPS:.2f}")
print(f"Status Kelulusan: {rangga_status_kelulusan}")
print("===========================")
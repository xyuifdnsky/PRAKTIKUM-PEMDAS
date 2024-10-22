#Proses memasukkan variabel
rangga_nama = "Rangga"
rangga_umur = 18
rangga_program_studi = "Sistem Informasi"
rangga_jenis_kelamin = "Laki-laki"
rangga_tinggi = 170
rangga_kelas = "SI-3B"
lulus = False

#Mengubah nilai variabel
budi_nama = "Budi"
budi_umur = 22
budi_tinggi = 175
budi_kelas = "SI-3C"
lulus = True

#Menampilkan informasi
print("Nama:", rangga_nama)
print("Umur:", rangga_umur, "tahun")
print("Tinggi Badan:", rangga_tinggi, "cm") 
print("Program Studi:", rangga_program_studi)
print("Kelas:", rangga_kelas)
print("Jenis Kelamin:", rangga_jenis_kelamin)

#Menampilkan status kelulusan
if lulus:
    print("Status: Alumni")
else:
    print("Status: Mahasiswa aktif")
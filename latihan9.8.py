#Memasukkan variabel
jml_karyawan_rangga = int(input("Masukkan jumlah karyawan: "))
gaji_pokok_rangga = float(input("Masukkan gaji pokok: "))
pajak_rangga = float
tunjangan_rangga = float
jml_gaji_rangga = float

#Proses menghitung pajak, tunjangan, gaji, dan jumlah gaji
pajak_rangga = 0.1 * gaji_pokok_rangga
tunjangan_rangga = 0.2 * gaji_pokok_rangga
gaji_rangga = gaji_pokok_rangga + tunjangan_rangga + pajak_rangga
jml_gaji_rangga = gaji_rangga * jml_karyawan_rangga

#Menampilkan hasil detail tunnjangan, detail pajak dan detail gaji karyawan
print("Detail tunjangan perkaryawan: ", tunjangan_rangga)
print("Detail pajak karyawan:", pajak_rangga)
print("Detail Gaji ", jml_karyawan_rangga, "orang:", "Rp.", jml_gaji_rangga)
#Mendeklarasikan variabel 
harga_1_km_pertama_rangga = 4500  #Harga untuk 1 Km pertama
harga_km_setelahnya_rangga = 2000  #Harga per Km setelahnya

#Jarak diinputkan oleh user
jarak_rangga = float(input("Masukkan jarak: "))

#Proses menghitung jarak sewa
if jarak_rangga <= 1:
    total_sewa_rangga = harga_1_km_pertama_rangga
else:
    #Hitung sewa untuk 1 Km pertama dan Km seterusnya
    total_sewa_rangga = harga_1_km_pertama_rangga + (jarak_rangga - 1) * harga_km_setelahnya_rangga

#Menampilkan hasil total sewa
print("Total sewa angkutan:", "Rp.", total_sewa_rangga)
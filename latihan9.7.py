#Meminta input nilai a dan b dari user
rangga_a = int(input("Masukkan nilai a: "))
rangga_b = int(input("Masukkan nilai b: "))

#Proses menukar nilai a dan b 
rangga_a = rangga_a + rangga_b  #Menjumlahkan nilai a dan b
rangga_b = rangga_a - rangga_b  #Mengambil nilai dari a
rangga_a = rangga_a - rangga_b  #Mengambil nilai dari b

#Menampilkan hasil pertukaran nilai a dan b
print("Nilai a sekarang: ", rangga_a)
print("Nilai b sekarang: ", rangga_b)
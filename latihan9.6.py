#Meminta input nilai dari user
rangga_a = float(input("Masukkan panjang alas jajaran genjang: "))
rangga_t = float(input("Masukkan tinggi jajaran genjang: "))
rangga_b = float(input("Masukkan sisi miring jajaran genjang: "))

#Proses menghitung luas dan keliling
rangga_L = rangga_a * rangga_t   #Rumus Luas jajaran genjang
rangga_K = 2 * (rangga_a + rangga_b)  # Rumus Keliling jajaran genjang

#Menampilkan hasil keliling dan luas jajaran genjang
print("Luas jajaran genjang:", rangga_L, "cm")
print("Keliling jajaran genjang:", rangga_K, "cm")
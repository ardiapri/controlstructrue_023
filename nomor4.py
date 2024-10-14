# Fungsi untuk mencetak bilangan ganjil hingga n
def cetak_ganjil(n):
    print(f"Bilangan ganjil hingga {n}:")
    for i in range(1, n+1):
        if i % 2 != 0:  # Memeriksa jika bilangan ganjil
            print(i, end=" ")

# Input angka n dari pengguna
n = int(input("Masukkan angka batas maksimum (n): "))

# Panggil fungsi untuk mencetak bilangan ganjil
cetak_ganjil(n)

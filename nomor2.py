# Fungsi untuk menemukan angka terbesar dari tiga angka
def angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input tiga angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Temukan angka terbesar
terbesar = angka_terbesar(angka1, angka2, angka3)

# Tampilkan hasil
print(f"Angka terbesar dari {angka1}, {angka2}, dan {angka3} adalah: {terbesar}")

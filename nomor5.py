# Fungsi untuk mencetak pola angka
def pola_angka(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)  # Mencetak angka i, sebanyak i kali

# Input dari pengguna
n = int(input("Masukkan jumlah baris pola: "))

# Panggil fungsi untuk mencetak pola
pola_angka(n)

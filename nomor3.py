# Fungsi untuk mencetak deret Fibonacci hingga n angka
def fibonacci(n):
    # Inisialisasi dua angka pertama dalam deret Fibonacci
    a, b = 0, 1
    count = 0

    # Memeriksa jika n adalah bilangan negatif atau nol
    if n <= 0:
        print("Masukkan bilangan bulat positif.")
    elif n == 1:
        print(f"Deret Fibonacci hingga {n}:")
        print(a)
    else:
        print(f"Deret Fibonacci hingga {n}:")
        # Loop untuk mencetak deret Fibonacci
        while count < n:
            print(a, end=" ")  # Cetak angka Fibonacci
            # Update dua angka terakhir
            a, b = b, a + b
            count += 1

# Input angka n dari pengguna
n = int(input("Masukkan jumlah angka Fibonacci yang ingin dicetak: "))

# Panggil fungsi Fibonacci
fibonacci(n)

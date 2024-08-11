def is_palindrome(x):
    # Mengubah angka menjadi string
    x_str = str(x)
    # Memeriksa apakah string tersebut sama jika dibalik
    return x_str == x_str[::-1]

# Meminta input dari pengguna
x = int(input("Masukkan sebuah angka: "))

# Memanggil fungsi dan mencetak hasil
result = is_palindrome(x)
print("Output:", result)

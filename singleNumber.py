def singleNumber(nums):
    # Menggunakan operasi XOR untuk menemukan angka yang hanya muncul sekali
    unique_number = 0
    for num in nums:
        unique_number ^= num
    return unique_number

# Meminta input dari pengguna
nums = list(map(int, input("Masukkan angka-angka pada array nums, dipisahkan dengan spasi: ").split()))

# Memanggil fungsi dan mencetak hasil
result = singleNumber(nums)
print("Output:", result)
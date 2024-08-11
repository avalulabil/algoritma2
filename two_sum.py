def two_sum(nums, target):
    # Membuat dictionary untuk menyimpan angka dan indeksnya
    num_map = {}
    
    # Melakukan iterasi pada array nums
    for i, num in enumerate(nums):
        # Mencari angka yang dibutuhkan untuk mencapai target
        complement = target - num
        
        # Jika angka yang dibutuhkan sudah ada di dictionary
        if complement in num_map:
            # Kembalikan indeks dari angka yang sudah ditemukan dan indeks saat ini
            return [num_map[complement], i]
        
        # Jika angka belum ada di dictionary, tambahkan ke dalam dictionary
        num_map[num] = i

# Meminta input dari pengguna
nums = list(map(int, input("Masukkan angka-angka pada array nums, dipisahkan dengan spasi: ").split()))
target = int(input("Masukkan target angka: "))

# Memanggil fungsi dan mencetak hasil
result = two_sum(nums, target)
print("Output:", result)

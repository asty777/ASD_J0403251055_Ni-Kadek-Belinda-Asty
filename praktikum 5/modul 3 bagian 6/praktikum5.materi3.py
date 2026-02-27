# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 6 - Materi 3
# ==========================================================

# ==========================================================
# MATERI 6.3 - Rekursi pada List
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
   # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
   # Recursive case: elemen sekarang + jumlah elemen setelahny
    return data[index] + jumlah_list(data, index + 1)

print("Jumlah list =", jumlah_list([2, 4, 6, 8]))
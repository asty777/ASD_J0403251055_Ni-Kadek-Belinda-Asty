# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 6 - Materi 3
# ==========================================================

# ==========================================================
# MATERI 6.4 - KOnsep Dasar Backtracking
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
   # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
   # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    
   # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

biner(3)
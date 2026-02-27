# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 6 - Materi 4
# ==========================================================

# ==========================================================
# MATERI 6.5 - Backtracking dengan Pruning (Pemangkasan)
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih 0
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilih 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)


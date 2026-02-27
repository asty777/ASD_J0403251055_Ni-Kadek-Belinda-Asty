# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 6 - Materi 2
# ==========================================================

# ==========================================================
# MATERI 6.2 - Tracing Rekursi (Call Stack)
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)  # fase stacking (masuk ke stack)
    hitung(n - 1)      # recursive call
    print("Keluar:", n)  # fase unwinding (keluar dari stack)

hitung(3)

# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 7 - Latihan 2
# ==========================================================

# ==========================================================
# LATIHAN 7.2 - Tracing Rekursi
# ==========================================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# ==========================================================
#1. Output keluar yang ada pada program muncul terbalik karena fungsi tracking rekursi yang ada memiliki sistem yang
#  menumpuk yang dimana proagram yang masuk terakhir maka akan keluar lebih awal.
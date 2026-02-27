# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 6 - Materi 1
# ==========================================================

# ==========================================================
# MATERI 6.1 - Konsep Dasar Rekursif 
# Contoh Rekursi 1 : Faktorial
# ==========================================================

def faktorial(n):
   # Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    
    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)

print("Faktorial 5 =", faktorial(5))  # Output: 120

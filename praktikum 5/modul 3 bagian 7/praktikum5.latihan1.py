# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 7 - Latihan 1
# ==========================================================

# ==========================================================
# LATIHAN 7.1 - Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case:
    if n == 0:
        return 1
    
    # Recursive case:
    return a * pangkat(a, n - 1)

print("Hasil pangkat:", pangkat(2, 4))  # Output: 16

# ==========================================================
#1. alur program : program ini akan menghitung nilai 2 pangkat 4 dengan cara mengalikan angka secara berulang menggunakan rekursi
#2. base case : base case ada pada n == 0, yang dimana setiap angka yang dipangkatkan 0 hasilnya 1. Ini adalah kondisi agar program berhenti.
#3. recursive call : recursive call ada pada a * pangkat(a, n - 1), fungsi tersebut berfungsi untuk memanggil dirinya sendiri dengan nilai pangkat yang lebih kecil.

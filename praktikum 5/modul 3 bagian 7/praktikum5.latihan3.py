# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 7 - Latihan 3
# ==========================================================


# ==========================================================
# LATIHAN 7.3 - Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    # Base case:
    # Jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case:
    maks_sisa = cari_maks(data, index + 1)
    
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

#1. Alur program : program ini mencari nilai maksimum dari list dengan cara membandingkannya satu persatu 
#2. Base case : base case ada pada index == len(data) - 1, yang dimana ketika sudah mencapai elemen terakhir maka akan mengembalikan nilai tersebut sebagai nilai maksimum sementara.
#3. Recursive call : recursive call ada pada maks_sisa = cari_maks(data, index + 1), fungsi tersebut berfungsi untuk memanggil dirinya sendiri dengan index yang lebih besar untuk mencari nilai maksimum dari sisa list. Setelah mendapatkan nilai maksimum dari sisa list, program akan membandingkannya dengan elemen saat ini untuk menentukan mana yang lebih besar.
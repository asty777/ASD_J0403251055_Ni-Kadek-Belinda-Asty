# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 7 - Latihan 5
# ==========================================================

# ==========================================================
# Studi Kasus - Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        if angka not in hasil:
         buat_pin(panjang, hasil + angka)

buat_pin(3)

#Untuk mencegah angka muncul berulang kita dapat menambahkan kode yang berupa pengecekan sebelum membuat pin yaitu
# If angka not in hasil yang berfungsi mengecek apakah angka sudah ada di hasil atau belum jika sudah maka pin tidak akan dibuat dan 
# jika belum maka pin akan dibuat 

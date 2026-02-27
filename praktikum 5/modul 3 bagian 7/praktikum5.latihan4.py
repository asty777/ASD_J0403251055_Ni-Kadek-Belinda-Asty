# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Praktikum 5 - Bagian 7 - Latihan 4
# ==========================================================

# ==========================================================
# LATIHAN 7.4 - Kombinasi Huruf 
# ==========================================================

def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

#jumlah kombinasi dari huruf A dan B (AA, AB, BA, BB) didapat menggabungkan huruf sesuai dengan kombinasi n yang di inginkan pada program ini alurnya berjalan seperti ini : 
# karena kombinasi yang di inginkan maka n = 2 dan huruf yang ingin ditambahkan yaitu A maka kode berjalan seperti : 
# Kombinasi (n, hasil="" + A) = A
# Kombinasi (n, hasil="A" + A = AA) -> output pertama
# kombinasi (n, hasil ="A" + B = AB) -> output kedua
# kombinasi (n, hasil ="" + B = B) 
# kombinasi (n, hasil ="B" + A = BA ) -> output ketiga
# kombinasi (n, hasil ="B" + B = BB) --> output keempat


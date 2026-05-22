# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J0403251055
# Kelas : TPL A1
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban
# 1. Total bobot jalur A -> B -> D adalah 9
# 2. Total bobot jalur A -> C -> D adalah 3
# 3. Jalur terpendek adalah A -> C -> D
# 4. Karena jalur terpendek ditentukan oleh total bobot,
#    bukan jumlah edge. Meskipun edge sedikit,
#    bobotnya bisa lebih besar.
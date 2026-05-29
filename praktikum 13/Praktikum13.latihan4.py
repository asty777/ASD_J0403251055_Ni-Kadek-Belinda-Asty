# ==========================================================
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Studi Kasus Jaringan Kabel Antar Gedung | Menggunakan Algoritma Kruskal

# edge (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

edges.sort()

mst = []
total_biaya = 0
connected = set()

# Memilih edge dengan biaya terkecil dan cek apakah kedua gedung sudah terhubung (dalam cycle)
for biaya, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, biaya))
        total_biaya += biaya
        connected.add(u)
        connected.add(v)

# Menampilkan edge yang dipilih dan total biaya minimum
print("Edge yang dipilih:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_biaya)

# Jawaban:
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih:
#    GedungC-GedungD = 1
#    GedungA-GedungC = 2
#    GedungB-GedungD = 3
# 3. Total biaya minimum = 6.
# 4. MST cocok digunakan karena dapat menghubungkan
#    seluruh gedung dengan biaya pemasangan kabel minimum.
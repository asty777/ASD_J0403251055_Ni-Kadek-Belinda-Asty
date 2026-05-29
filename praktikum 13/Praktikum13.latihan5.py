# ==========================================================
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Kasus 1 : Jaringan Jalan Antar Kota | Menggunakan Algoritma Kruskal

# Daftar edge (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

edges.sort()

mst = []
total_bobot = 0
connected = set()

# Memilih edge dengan bobot terkecil dan cek apakah kedua kota sudah terhubung (dalam cycle)
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_bobot += weight
        connected.add(u)
        connected.add(v)

# Menampilkan edge yang dipilih dan total bobot minimum
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total_bobot)

# Jawaban:
# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota.
# 2. Algoritma yang digunakan adalah Kruskal karena lebih 
#    efisien untuk mencari MST dalam graf yang tidak berbobot.
# 3. Edge yang dipilih:
#    Bogor-Depok = 2
#    Depok-Jakarta = 3
#    Depok-Bandung = 4
# 4. Total bobot MST = 9.
# 5. Edge Bogor-Jakarta (5) dan Jakarta-Bandung (6)
#    tidak dipilih karena ada jalur lain yang lebih murah
#    untuk menghubungkan seluruh kota.
# ==========================================================
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A1`
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================


#Menggunakan Kruskal

# daftar edge
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# mengurutkan edge berdasarkan bobot terkecil
edges.sort()


mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban:
# 1. Edge pertama yang dipilih adalah C-D dengan bobot 1.
# 2. Karena Kruskal selalu memilih edge dengan bobot paling kecil
#    terlebih dahulu agar total bobot MST menjadi minimum.
# 3. Total bobot MST yang dihasilkan adalah 6.
# 4. Edge tertentu tidak dipilih karena dapat membentuk cycle
#    atau tidak diperlukan lagi setelah semua node terhubung.
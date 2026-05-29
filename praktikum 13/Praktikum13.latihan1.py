# ==========================================================
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge pada graph dan spanning tree, serta jumlah edge masing-masing
print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban:
# 1. Graph awal masih memiliki banyak edge dan dapat membentuk cycle,
#    sedangkan spanning tree hanya menggunakan edge yang diperlukan
#    untuk menghubungkan semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle menambah
#    edge yang tidak diperlukan dan membuat koneksi menjadi tidak efisien.
# 3. Jumlah edge spanning tree lebih sedikit karena spanning tree
#    selalu memiliki jumlah edge = jumlah node - 1.
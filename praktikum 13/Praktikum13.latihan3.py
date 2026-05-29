# ==========================================================
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

import heapq

#Prim
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    visited = set([start])
    edges = []
    # Menambahkan edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)
        # Memeriksa apakah node tujuan sudah dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge dari node tujuan ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

# Menampilkan hasil MST dan total bobot
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban:
# 1. Node awal yang digunakan adalah A.
# 2. Edge pertama yang dipilih adalah A-C dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan memilih edge
#    berbobot paling kecil yang menghubungkan node yang
#    sudah dikunjungi ke node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Kruskal memilih edge terkecil secara global,
#    sedangkan Prim membangun tree mulai dari satu node awal.
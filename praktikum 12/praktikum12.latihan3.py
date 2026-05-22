# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J0403251055
# Kelas : TPL A1
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Relaksasi edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Update jika ditemukan jarak lebih kecil
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban:
# 1. Bobot langsung dari A ke B adalah 5
# 2. Total bobot jalur A -> C -> B adalah 2
#    (4 + (-2))
# 3. Jalur A -> C -> B menghasilkan jarak lebih kecil
# 4. Karena Bellman-Ford dapat menghitung jalur
#    meskipun terdapat bobot negatif
# 5. Relaksasi edge adalah proses memperbarui
#    jarak menjadi lebih kecil jika ditemukan jalur lebih baik
# 6. Dijkstra hanya untuk bobot positif,
#    sedangkan Bellman-Ford bisa untuk bobot negatif
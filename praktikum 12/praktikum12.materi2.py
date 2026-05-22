# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J0403251055
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    # Node awal bernilai 0
    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:

            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak lebih kecil
                if distances[node] + weight < distances[neighbor]:

                    # Update jarak
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')


print("Hasil Shortest Path:")
print(hasil)

# ==========================================================
# Penjelasan
# ==========================================================
# Jalur langsung:
# A -> B = 5
#
# Jalur melalui C:
# A -> C -> B
# = 4 + (-2)
# = 2
#
# Karena hasil 2 lebih kecil dibandingkan 5,
# maka jalur terbaik menuju B adalah melalui C.
#
# ==========================================================
# Bellman-Ford
# ==========================================================
# Algoritma Bellman-Ford digunakan untuk mencari
# shortest path pada graph dengan bobot negatif.
#
# Bellman-Ford bekerja dengan melakukan relaksasi
# seluruh edge secara berulang-ulang.
#
# Relaksasi adalah proses memperbarui jarak
# jika ditemukan jalur yang lebih kecil.
#
# ==========================================================
# Perbandingan Dijkstra dan Bellman-Ford
# ==========================================================
#
# Dijkstra:
# - Tidak dapat menangani bobot negatif
# - Lebih cepat
# - Menggunakan pendekatan greedy
#
# Bellman-Ford:
# - Bisa menangani bobot negatif
# - Lebih lambat
# - Menggunakan relaksasi edge
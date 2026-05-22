# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J0403251055
# Kelas : TPL A1
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# graph
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi mencari jarak terpendek dari node awal
    ke seluruh node lainnya
    """

    # Semua jarak awal tak hingga
    distances = {node: float('inf') for node in graph}

    # Node awal bernilai 0
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak lebih besar
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# Jawaban:
# 1. Node awal yang digunakan adalah Bogor
# 2. Node dengan jarak paling kecil dari node awal adalah Depok
#    dengan jarak 2
# 3. Node dengan jarak paling besar dari node awal adalah Bandung
#    dengan jarak 8
# 4. Algoritma Dijkstra bekerja dengan memilih node
#    dengan jarak terkecil terlebih dahulu,
#    lalu memperbarui jarak ke node tetangga
#    hingga semua node mendapatkan jarak minimum
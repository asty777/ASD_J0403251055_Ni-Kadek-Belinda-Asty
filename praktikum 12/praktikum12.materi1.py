# ==========================================================
# Nama  : Ni Kadek Belinda Asty
# NIM   : J0403251055
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================


import heapq

#weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):

    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Menjalankan algoritma
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Hasil Shortest Path:")
print(hasil)

# ==========================================================
# Penjelasan
# ==========================================================
# Jarak dari A ke A = 0
# karena node awal ke dirinya sendiri tidak memerlukan perjalanan.
#
# Jarak dari A ke B = 4
# karena terdapat jalur langsung A -> B dengan bobot 4.
#
# Jarak dari A ke C = 2
# karena terdapat jalur langsung A -> C dengan bobot 2.
#
# Jarak dari A ke D = 3
# karena jalur terbaik adalah:
# A -> C -> D
# dengan total bobot:
# 2 + 1 = 3
#
# ==========================================================
# Kelemahan Algoritma Dijkstra
# ==========================================================
# Algoritma Dijkstra tidak cocok digunakan pada graph
# yang memiliki bobot negatif.
#
# Hal ini karena Dijkstra menggunakan pendekatan greedy,
# yaitu memilih jalur terbaik sementara dan menganggap
# jalur tersebut sudah optimal.
#
# Jika terdapat bobot negatif, maka bisa muncul jalur
# yang sebenarnya lebih pendek setelah proses sebelumnya selesai.

# Praktikum 3 - Konversi Matrix ke Adjacency List

# Adjacency matrix
matrix = [
    [0, 1, 1, 0],  # Node 0 terhubung ke 1 dan 2
    [1, 0, 1, 0],  # Node 1 terhubung ke 0 dan 2
    [1, 1, 0, 1],  # Node 2 terhubung ke 0, 1, dan 3
    [0, 0, 1, 0]   # Node 3 terhubung ke 2
]

adj_list = {}
for i in range(len(matrix)):

    neighbors = []

    for j in range(len(matrix[i])):

        if matrix[i][j] == 1:
            neighbors.append(j)

    adj_list[i] = neighbors

print("Adjacency List:\n")

# Menampilkan adjacency list
for node in adj_list:
    print(f"{node} -> {adj_list[node]}")
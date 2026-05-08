# Praktikum 1 - Membuat Adjacency Matrix

# Matrix 
matrix = [
    [0, 1, 1, 0],  # Node 0 terhubung ke node 1 dan 2
    [1, 0, 1, 0],  # Node 1 terhubung ke node 0 dan 2
    [1, 1, 0, 1],  # Node 2 terhubung ke node 0, 1, dan 3
    [0, 0, 1, 0]   # Node 3 terhubung ke node 2
]

# Menampilkan adjacency matrix
print("Adjacency Matrix:\n")

# menampilkan setiap baris pada matrix
for row in matrix:
    print(row)

print("\nArti setiap baris:\n")

for i in range(len(matrix)):
    hubungan = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            hubungan.append(str(j))
    print(f"Baris {i} artinya node {i} terhubung ke node {', '.join(hubungan)}")
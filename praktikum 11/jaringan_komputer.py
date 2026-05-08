# Praktikum 4 - Studi Kasus Jaringan Komputer

# Adjacency List
graph = {
    "Router": ["Switch", "Server"],
    "Switch": ["Router", "Server", "PC1", "PC2"],
    "Server": ["Router", "Switch"],
    "PC1": ["Switch", "PC2"],
    "PC2": ["Switch", "PC1"]
}

#node
nodes = ["Router", "Switch", "Server", "PC1", "PC2"]

# Adjacency Matrix
matrix = [
    [0,1,1,0,0],  # Router
    [1,0,1,1,1],  # Switch
    [1,1,0,0,0],  # Server
    [0,1,0,0,1],  # PC1
    [0,1,0,1,0]   # PC2
]

# Menampilkan adjacency list
print("Adjacency List:\n")

print("Router ->", graph["Router"])
print("Switch ->", graph["Switch"])
print("Server ->", graph["Server"])
print("PC1 ->", graph["PC1"])
print("PC2 ->", graph["PC2"])

# Menampilkan adjacency matrix
print("\nAdjacency Matrix:\n")

print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])

#node
print("\nNama Node:\n")

print("1. Router")
print("2. Switch")
print("3. Server")
print("4. PC1")
print("5. PC2")

# hubungan antar node
print("\nHubungan Antar Node:\n")

print("Router terhubung dengan Switch dan Server")
print("Switch terhubung dengan Router, Server, PC1, dan PC2")
print("Server terhubung dengan Router dan Switch")
print("PC1 terhubung dengan Switch dan PC2")
print("PC2 terhubung dengan Switch dan PC1")
print("Praktikum 1 - Membuat Adjacency List")

graph = {
    'A': ['B', 'C'],  # Node A terhubung ke B dan C
    'B': ['A', 'D'],  # Node B terhubung ke A dan D
    'C': ['A', 'D'],  # Node C terhubung ke A dan D
    'D': ['B', 'C']   # Node D terhubung ke B dan C
}

print("Adjacency List:\n")

# menampilkan adjacency list
for node in graph:

    print(f"{node} -> {graph[node]}")


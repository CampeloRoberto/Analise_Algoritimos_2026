# Implementação simples do algoritmo de Floyd-Warshall
# Objetivo: encontrar o menor caminho entre TODOS os pares de vértices

INF = float('inf')

# Matriz de adjacência do grafo
# INF significa que não existe ligação direta
grafo = [
    [0,   3, INF, 7],
    [8,   0,   2, INF],
    [5, INF,   0,   1],
    [2, INF, INF,   0]
]

n = len(grafo)

# Copia a matriz original
dist = [linha[:] for linha in grafo]

# Algoritmo de Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            # Verifica se passar pelo vértice k é melhor
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Exibe a matriz final de menores caminhos
print("Matriz de menores distâncias:\n")

for linha in dist:
    for valor in linha:
        if valor == INF:
            print("INF", end="\t")
        else:
            print(valor, end="\t")
    print()

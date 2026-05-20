"""Algoritmo de Prim para encontrar a Árvore Geradora Mínima (AGM).

Este módulo implementa o Algoritmo de Prim aplicado ao problema de
interligar polos tecnológicos com uma rede de fibra óptica, minimizando
o custo total de cabeamento.
"""

import heapq


def prim(grafo, inicio):
    """Encontra a Árvore Geradora Mínima usando o Algoritmo de Prim.

    Args:
        grafo (dict): Lista de adjacências no formato
            {vertice: [(vizinho, peso), ...]}.
        inicio (str): Vértice inicial para começar o algoritmo.

    Returns:
        tuple: Uma tupla contendo:
            - rota (list): Lista de arestas (origem, destino, peso) em
              ordem de inclusão na AGM.
            - custo_total (int): Soma dos pesos das arestas da AGM.
    """
    visitados = {inicio}
    rota = []
    custo_total = 0
    fila = []

    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, vizinho))

    while fila and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(fila)

        if destino in visitados:
            continue

        visitados.add(destino)
        rota.append((origem, destino, peso))
        custo_total += peso

        for vizinho, peso_vizinho in grafo[destino]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso_vizinho, destino, vizinho))

    return rota, custo_total


def exibir_resultado(rota, custo_total):
    """Exibe a rota dos cabos e o custo total de forma formatada.

    Args:
        rota (list): Lista de arestas da AGM.
        custo_total (int): Custo total da AGM em quilômetros.
    """
    separador = "=" * 50
    print(separador)
    print("ALGORITMO DE PRIM - REDE DE FIBRA ÓPTICA")
    print(separador)
    print("\nRota dos cabos a serem instalados (em ordem):\n")

    for i, (origem, destino, peso) in enumerate(rota, start=1):
        print(f"  {i}. {origem} --> {destino}  ({peso} km)")

    print(f"\nQuantidade total mínima de cabos: {custo_total} km")
    print(separador)


def main():
    """Função principal: define o grafo e executa o algoritmo."""
    grafo = {
        "A": [("B", 4), ("C", 4)],
        "B": [("A", 4), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 5), ("E", 6)],
        "D": [("B", 5), ("C", 5), ("E", 3), ("F", 4)],
        "E": [("C", 6), ("D", 3), ("F", 2)],
        "F": [("D", 4), ("E", 2)],
    }

    vertice_inicial = "A"
    rota, custo_total = prim(grafo, vertice_inicial)
    exibir_resultado(rota, custo_total)


if __name__ == "__main__":
    main()

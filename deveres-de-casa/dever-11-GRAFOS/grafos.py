import random
import heapq

NUM_NOS = 50
NUM_ARESTAS = 150


def gerar_grafo(num_nos, num_arestas):
    """
    Gera um grafo não-direcionado aleatório.

    Args:
        num_nos (int): Quantidade de nós.
        num_arestas (int): Quantidade de arestas.

    Returns:
        dict: Grafo em lista de adjacência.
    """

    grafo = {no: [] for no in range(1, num_nos + 1)}

    arestas_existentes = set()

    while len(arestas_existentes) < num_arestas * 2:
        origem = random.randint(1, num_nos)
        destino = random.randint(1, num_nos)

        if origem != destino and (origem, destino) not in arestas_existentes:
            peso = random.randint(1, 20)

            grafo[origem].append((destino, peso))
            grafo[destino].append((origem, peso))

            arestas_existentes.add((origem, destino))
            arestas_existentes.add((destino, origem))

    return grafo


def dijkstra(grafo, inicio, fim):
    """
    Executa o algoritmo de Dijkstra.

    Args:
        grafo (dict): Grafo em lista de adjacência.
        inicio (int): Nó inicial.
        fim (int): Nó final.

    Returns:
        tuple: Caminho mínimo e custo total.
    """

    fila_prioridade = [(0, inicio)]

    distancias = {
        no: float("inf")
        for no in grafo
    }

    distancias[inicio] = 0

    predecessores = {}

    while fila_prioridade:
        custo_atual, no_atual = heapq.heappop(fila_prioridade)

        if no_atual == fim:
            break

        for vizinho, peso in grafo[no_atual]:
            novo_custo = custo_atual + peso

            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo

                predecessores[vizinho] = no_atual

                heapq.heappush(
                    fila_prioridade,
                    (novo_custo, vizinho)
                )

    caminho = []
    atual = fim

    while atual != inicio:
        caminho.append(atual)

        if atual not in predecessores:
            return None, float("inf")

        atual = predecessores[atual]

    caminho.append(inicio)

    caminho.reverse()

    return caminho, distancias[fim]


def exibir_resultado(caminho, custo_total):
    """
    Exibe o caminho e o custo total.

    Args:
        caminho (list): Lista contendo o menor caminho.
        custo_total (int): Soma dos pesos do caminho.
    """

    print("\n=== MENOR CAMINHO ===")

    if caminho:
        rota = " -> ".join(map(str, caminho))

        print(f"Rota encontrada: {rota}")
        print(f"Custo total: {custo_total}")

    else:
        print("Não existe caminho entre os nós.")


def main():
    """
    Função principal do programa.
    """

    grafo = gerar_grafo(NUM_NOS, NUM_ARESTAS)

    inicio = 1
    fim = 50

    caminho, custo_total = dijkstra(grafo, inicio, fim)

    print("=== GRAFO GERADO ===")
    print(f"Quantidade de nós: {NUM_NOS}")
    print(f"Quantidade de arestas: {NUM_ARESTAS}")

    exibir_resultado(caminho, custo_total)


if __name__ == "__main__":
    main()

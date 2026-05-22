import time


class Grafo:
    """
    Classe responsável por representar um grafo
    e executar o algoritmo de Kruskal Máximo.
    """

    def __init__(self, vertices):
        self.v = vertices
        self.grafo = []

    def adicionar_aresta(self, origem, destino, peso):
        """
        Adiciona uma aresta ao grafo.

        Args:
            origem (int): Nó de origem.
            destino (int): Nó de destino.
            peso (int): Peso da aresta.
        """

        self.grafo.append([origem, destino, peso])

    def buscar_raiz(self, pai, vertice):
        """
        Busca a raiz de um vértice utilizando
        compressão de caminho.

        Args:
            pai (list): Lista de pais.
            vertice (int): Vértice analisado.

        Returns:
            int: Raiz do vértice.
        """

        if pai[vertice] == vertice:
            return vertice

        pai[vertice] = self.buscar_raiz(
            pai,
            pai[vertice]
        )

        return pai[vertice]

    def unir_redes(self, pai, rank, x, y):
        """
        Une dois conjuntos utilizando Union by Rank.

        Args:
            pai (list): Lista de pais.
            rank (list): Lista de ranks.
            x (int): Primeiro conjunto.
            y (int): Segundo conjunto.
        """

        raiz_x = self.buscar_raiz(pai, x)
        raiz_y = self.buscar_raiz(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y

        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x

        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def executar_kruskal_maximo(self):
        """
        Executa o algoritmo de Kruskal Máximo,
        encontrando o caminho mais caro sem ciclos.

        Returns:
            tuple:
                - Lista de arestas escolhidas.
                - Custo total.
        """

        resultado = []

        indice_aresta = 0
        arestas_escolhidas = 0

        custo_total = 0

        # Ordena do MAIOR para o MENOR peso
        self.grafo = sorted(
            self.grafo,
            key=lambda item: item[2],
            reverse=True
        )

        pai = []
        rank = []

        for vertice in range(self.v):
            pai.append(vertice)
            rank.append(0)

        while arestas_escolhidas < self.v - 1:
            origem, destino, peso = self.grafo[indice_aresta]

            indice_aresta += 1

            raiz_origem = self.buscar_raiz(pai, origem)
            raiz_destino = self.buscar_raiz(pai, destino)

            # Evita ciclos
            if raiz_origem != raiz_destino:
                arestas_escolhidas += 1

                resultado.append(
                    [origem, destino, peso]
                )

                custo_total += peso

                self.unir_redes(
                    pai,
                    rank,
                    raiz_origem,
                    raiz_destino
                )

        return resultado, custo_total


def main():
    """
    Função principal do programa.
    """

    grafo = Grafo(8)

    grafo.adicionar_aresta(4, 7, 1)
    grafo.adicionar_aresta(5, 6, 2)
    grafo.adicionar_aresta(4, 5, 3)
    grafo.adicionar_aresta(6, 7, 4)
    grafo.adicionar_aresta(0, 1, 5)
    grafo.adicionar_aresta(3, 7, 6)
    grafo.adicionar_aresta(2, 5, 7)
    grafo.adicionar_aresta(2, 6, 8)
    grafo.adicionar_aresta(1, 2, 9)
    grafo.adicionar_aresta(1, 6, 10)
    grafo.adicionar_aresta(1, 5, 11)
    grafo.adicionar_aresta(1, 7, 13)
    grafo.adicionar_aresta(1, 4, 14)
    grafo.adicionar_aresta(0, 4, 15)
    grafo.adicionar_aresta(0, 3, 16)
    grafo.adicionar_aresta(3, 6, 17)
    grafo.adicionar_aresta(0, 7, 18)

    inicio = time.perf_counter()

    caminho_final, custo_final = (
        grafo.executar_kruskal_maximo()
    )

    fim = time.perf_counter()

    tempo_execucao = (
        fim - inicio
    ) * 1000

    print(
        "\n--- RESULTADO DO "
        "KRUSKAL MÁXIMO ---"
    )

    print(
        "\nRotas escolhidas "
        "para a rede:"
    )

    for origem, destino, peso in caminho_final:
        print(
            f"Cidade {origem} -> "
            f"Cidade {destino} | "
            f"Custo: {peso}"
        )

    print(
        f"\nCusto Total Máximo: "
        f"{custo_final}"
    )

    print(
        f"Tempo de execução: "
        f"{tempo_execucao:.4f} ms"
    )


if __name__ == "__main__":
    main()

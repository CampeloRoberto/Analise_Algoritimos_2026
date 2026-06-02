from math import inf


class Grafo:
    def __init__(self):
        self.vertices = {"A", "B", "C", "D", "E"}
        self.arestas = [
            ("A", "B", 4),
            ("A", "C", 4),
            ("B", "C", 2),
            ("B", "D", 5),
            ("C", "D", 1),
            ("C", "E", 3),
            ("D", "C", -3),
            ("D", "E", 2),
            ("E", "D", 1)
        ]

    def bellman_ford(self, origem):
        distancia = {
            vertice: inf
            for vertice in self.vertices
        }

        predecessor = {
            vertice: None
            for vertice in self.vertices
        }

        distancia[origem] = 0

        print("\nTabela Inicial")
        self.exibir_tabela(distancia)

        quantidade_vertices = len(self.vertices)

        for iteracao in range(quantidade_vertices - 1):
            print(f"\nIteração {iteracao + 1}")
            houve_relaxamento = False

            for origem_aresta, destino, peso in self.arestas:

                if distancia[origem_aresta] == inf:
                    continue

                novo_custo = (
                    distancia[origem_aresta] + peso
                )

                if novo_custo < distancia[destino]:

                    antigo_valor = distancia[destino]

                    distancia[destino] = novo_custo

                    predecessor[destino] = origem_aresta

                    houve_relaxamento = True

                    print(
                        f"Relaxando "
                        f"{origem_aresta} -> {destino} "
                        f"({peso})"
                    )

                    print(
                        f"{origem_aresta}: "
                        f"{distancia[origem_aresta]} + "
                        f"{peso} < "
                        f"{antigo_valor}"
                    )

                    print(
                        f"Atualizar "
                        f"{destino} = "
                        f"{novo_custo}\n"
                    )

            self.exibir_tabela(distancia)

            if not houve_relaxamento:
                break

        print("\nVerificando ciclo negativo...")

        for origem_aresta, destino, peso in self.arestas:

            if (
                distancia[origem_aresta] != inf
                and distancia[origem_aresta] + peso
                < distancia[destino]
            ):
                print("\nCiclo negativo detectado!")
                return

        print("\nNenhum ciclo negativo encontrado.")

        print("\nDistâncias finais:")
        self.exibir_tabela(distancia)

        print("\nPredecessores:")
        for vertice in sorted(predecessor):
            print(
                f"{vertice}: "
                f"{predecessor[vertice]}"
            )

    @staticmethod
    def exibir_tabela(distancia):
        print(
            f"A={distancia['A']} | "
            f"B={distancia['B']} | "
            f"C={distancia['C']} | "
            f"D={distancia['D']} | "
            f"E={distancia['E']}"
        )


def main():
    grafo = Grafo()
    grafo.bellman_ford("A")


if __name__ == "__main__":
    main()

from itertools import permutations


def reduzir_para_tsp(grafo):
    """
    Converte uma instância de Ciclo Hamiltoniano
    para uma instância de Caixeiro Viajante.
    """
    n = len(grafo)

    tsp = [[2] * n for _ in range(n)]

    for i in range(n):
        tsp[i][i] = 0

        for j in range(n):
            if grafo[i][j] == 1:
                tsp[i][j] = 1

    return tsp, n


def resolver_tsp(matriz, limite):
    """
    Verifica se existe um ciclo de custo <= limite.
    """
    n = len(matriz)

    for caminho in permutations(range(1, n)):
        rota = (0,) + caminho

        custo = 0

        for i in range(n - 1):
            custo += matriz[rota[i]][rota[i + 1]]

        custo += matriz[rota[-1]][rota[0]]

        if custo <= limite:
            return True, rota, custo

    return False, None, None


def resolver_ciclo_hamiltoniano(grafo):
    """
    Resolve Ciclo Hamiltoniano utilizando um
    solucionador de TSP.
    """
    matriz_tsp, limite = reduzir_para_tsp(grafo)

    existe, rota, custo = resolver_tsp(
        matriz_tsp,
        limite
    )

    return existe, rota, custo


def main():
    grafo = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    existe, rota, custo = resolver_ciclo_hamiltoniano(
        grafo
    )

    if existe:
        print("Existe ciclo hamiltoniano.")
        print("Rota:", rota)
        print("Custo:", custo)
    else:
        print("Não existe ciclo hamiltoniano.")


if __name__ == "__main__":
    main()

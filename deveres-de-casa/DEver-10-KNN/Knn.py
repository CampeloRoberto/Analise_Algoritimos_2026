"""Classificação de câncer de mama com KNN.

Compara desempenho do KNeighborsClassifier variando K (1, 3, 5)
e a métrica de distância (Euclidiana e Manhattan) sobre o dataset
breast cancer do scikit-learn.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def carregar_dados():
    """Carrega o dataset e retorna atributos e rótulos."""
    cancer = load_breast_cancer()
    return cancer.data, cancer.target


def preparar_dados(x, y, tamanho_teste=0.2, random_state=42):
    """Divide os dados em treino/teste e aplica normalização."""
    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x,
        y,
        test_size=tamanho_teste,
        random_state=random_state,
    )

    scaler = StandardScaler()
    x_treino = scaler.fit_transform(x_treino)
    x_teste = scaler.transform(x_teste)

    return x_treino, x_teste, y_treino, y_teste


def avaliar_modelo(x_treino, x_teste, y_treino, y_teste, k, metrica):
    """Treina o KNN e imprime as métricas de avaliação."""
    modelo = KNeighborsClassifier(n_neighbors=k, metric=metrica)
    modelo.fit(x_treino, y_treino)
    previsoes = modelo.predict(x_teste)

    acuracia = accuracy_score(y_teste, previsoes)

    print(f"\nK = {k}")
    print(f"Acurácia: {acuracia:.4f}")
    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_teste, previsoes))
    print("\nRelatório de Classificação:")
    print(classification_report(y_teste, previsoes))

    return acuracia


def main():
    """Executa o pipeline completo de avaliação."""
    valores_k = [1, 3, 5]
    metricas = ["euclidean", "manhattan"]

    x, y = carregar_dados()
    print("Quantidade de registros:", x.shape[0])
    print("Quantidade de atributos:", x.shape[1])

    x_treino, x_teste, y_treino, y_teste = preparar_dados(x, y)
    print("\nDados separados com sucesso!")
    print("Treino:", x_treino.shape)
    print("Teste:", x_teste.shape)
    print("\nDados normalizados com StandardScaler!")

    resultados = []
    for metrica in metricas:
        print("\n========================================")
        print(f"DISTÂNCIA: {metrica.upper()}")
        print("========================================")
        for k in valores_k:
            acuracia = avaliar_modelo(
                x_treino, x_teste, y_treino, y_teste, k, metrica
            )
            resultados.append([k, metrica, acuracia])

    resultado_df = pd.DataFrame(
        resultados,
        columns=["K", "Métrica", "Acurácia"],
    )

    print("\n========================================")
    print("RESULTADOS FINAIS")
    print("========================================")
    print(resultado_df)

    melhor = resultado_df.loc[resultado_df["Acurácia"].idxmax()]
    print("\n========================================")
    print("MELHOR CONFIGURAÇÃO")
    print("========================================")
    print(melhor)


if __name__ == "__main__":
    main()

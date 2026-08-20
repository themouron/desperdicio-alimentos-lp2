"""Geração dos gráficos do histórico de desperdício."""

from pathlib import Path


PASTA_GRAFICOS = Path("graficos")

CORES_CLASSIFICACAO = {
    "Excelente": "green",
    "Bom": "blue",
    "Atenção": "orange",
    "Crítico": "red",
}


def gerar_grafico_barras(dados, pasta=PASTA_GRAFICOS):
    """Gera um gráfico do percentual de desperdício por alimento."""
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    cores = [
        CORES_CLASSIFICACAO.get(classificacao, "gray")
        for classificacao in dados["Classificação"]
    ]
    legenda = [
        Patch(color=cor, label=classificacao)
        for classificacao, cor in CORES_CLASSIFICACAO.items()
    ]
    plt.figure(figsize=(10, 6))
    plt.bar(dados["Alimento"], dados["Percentual de desperdício"], color=cores)
    plt.title("Alimento x percentual de desperdício")
    plt.xlabel("Alimento")
    plt.ylabel("Percentual de desperdício")
    plt.xticks(rotation=35, ha="right")
    plt.legend(handles=legenda)
    plt.tight_layout()
    caminho = Path(pasta) / "alimento_percentual.png"
    plt.savefig(caminho)
    plt.close()
    print(f"Gráfico gerado: {caminho}")


def gerar_grafico_pizza(dados, pasta=PASTA_GRAFICOS):
    """Gera um gráfico da participação de cada alimento no prejuízo total."""
    import matplotlib.pyplot as plt

    valores = dados.groupby("Alimento")["Valor desperdiçado"].sum()
    valores = valores[valores > 0].sort_values(ascending=False)
    if valores.empty:
        print("Não há valor desperdiçado para gerar o gráfico de pizza.")
        return

    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=valores.index, autopct="%1.1f%%", startangle=90)
    plt.title("Participação no desperdício total")
    plt.tight_layout()
    caminho = Path(pasta) / "participacao_desperdicio.png"
    plt.savefig(caminho)
    plt.close()
    print(f"Gráfico gerado: {caminho}")


def gerar_graficos(historico, pasta=PASTA_GRAFICOS):
    """Gera todos os gráficos disponíveis para o histórico informado."""
    if not historico:
        print("Não há dados para gerar gráficos.")
        return

    import pandas as pd

    Path(pasta).mkdir(parents=True, exist_ok=True)
    dados = pd.DataFrame(historico).sort_values(
        "Percentual de desperdício", ascending=False
    )
    gerar_grafico_barras(dados, pasta)
    gerar_grafico_pizza(dados, pasta)

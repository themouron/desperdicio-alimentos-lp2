"""Cadastro, regras e relatórios relacionados ao desperdício alimentar."""

from datetime import datetime

from src.dados import adicionar_registro
from src.graficos import gerar_graficos
from src.utils import ler_float, ler_opcao, ler_texto, mostrar_titulo


RECOMENDACOES = {
    "Excelente": "Manter o planejamento atual, pois o desperdício está muito baixo.",
    "Bom": (
        "Continuar acompanhando as sobras e fazer pequenos ajustes se necessário."
    ),
    "Atenção": (
        "Revisar a quantidade comprada e observar o consumo real nas próximas "
        "refeições."
    ),
    "Crítico": "Reduzir a quantidade comprada ou revisar o planejamento.",
}


def classificar_desperdicio(percentual):
    """Classifica o desperdício de acordo com o percentual calculado."""
    if percentual <= 5:
        return "Excelente"
    if percentual <= 10:
        return "Bom"
    if percentual <= 15:
        return "Atenção"
    return "Crítico"


def calcular_desperdicio(quantidade_comprada, quantidade_sobrou, preco):
    """Calcula consumo, percentual e valores financeiros de um registro."""
    percentual = quantidade_sobrou / quantidade_comprada * 100
    return {
        "Quantidade consumida": quantidade_comprada - quantidade_sobrou,
        "Percentual de desperdício": percentual,
        "Valor total comprado": quantidade_comprada * preco,
        "Valor desperdiçado": quantidade_sobrou * preco,
        "Classificação": classificar_desperdicio(percentual),
    }


def recomendar_por_classificacao(classificacao):
    """Retorna uma recomendação adequada à classificação."""
    return RECOMENDACOES.get(
        classificacao,
        "Analisar os dados e ajustar o planejamento de compras.",
    )


def mostrar_resumo_cadastro(registro):
    print("\nResumo do cadastro atual:")
    for chave, valor in registro.items():
        texto = f"{valor:.2f}" if isinstance(valor, float) else valor
        print(f"- {chave}: {texto}")


def cadastrar_desperdicio(historico):
    """Solicita e salva um ou mais registros de desperdício."""
    while True:
        print("\nCadastrar desperdício")
        alimento = ler_texto("Nome do alimento: ")
        unidade = ler_opcao(
            "Unidade (kg, litro ou unidade): ", ["kg", "litro", "unidade"]
        )
        quantidade_comprada = ler_float("Quantidade comprada: ")

        while True:
            quantidade_sobrou = ler_float(
                "Quantidade que sobrou: ", permitir_zero=True
            )
            if quantidade_sobrou <= quantidade_comprada:
                break
            print("A sobra não pode ser maior que a quantidade comprada.")

        preco = ler_float(f"Preço por {unidade}: ")
        calculos = calcular_desperdicio(
            quantidade_comprada, quantidade_sobrou, preco
        )
        registro = {
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Alimento": alimento,
            "Quantidade comprada": quantidade_comprada,
            "Quantidade sobrada": quantidade_sobrou,
            "Quantidade consumida": calculos["Quantidade consumida"],
            "Unidade": unidade,
            "Preço informado": preco,
            "Valor total comprado": calculos["Valor total comprado"],
            "Valor desperdiçado": calculos["Valor desperdiçado"],
            "Percentual de desperdício": calculos[
                "Percentual de desperdício"
            ],
            "Classificação": calculos["Classificação"],
        }
        adicionar_registro(registro, historico)
        print("\nCadastro salvo com sucesso.")

        while True:
            print("\n1 - Cadastrar outro alimento")
            print("2 - Ver resumo do cadastro atual")
            print("3 - Voltar ao menu de análise")
            opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3"])
            if opcao == "1":
                break
            if opcao == "2":
                mostrar_resumo_cadastro(registro)
            else:
                return


def mostrar_relatorio(historico):
    """Exibe registros, totais e rankings do histórico."""
    mostrar_titulo("RELATÓRIO GERAL")
    if not historico:
        print("Não existe histórico de desperdício cadastrado.")
        return

    import pandas as pd

    dados = pd.DataFrame(historico)
    for indice, registro in dados.iterrows():
        unidade = registro["Unidade"]
        mostrar_titulo(f"REGISTRO {indice + 1}")
        print(f"Data: {registro['Data']}")
        print(f"Alimento: {registro['Alimento']}")
        print(f"Unidade: {unidade}")
        print(
            f"\nQuantidade comprada: {registro['Quantidade comprada']:.2f} "
            f"{unidade}"
        )
        print(f"Quantidade sobrada: {registro['Quantidade sobrada']:.2f} {unidade}")
        print(f"Quantidade consumida: {registro['Quantidade consumida']:.2f} {unidade}")
        print(f"\nPreço informado: R$ {registro['Preço informado']:.2f} por {unidade}")
        print(f"Valor total comprado: R$ {registro['Valor total comprado']:.2f}")
        print(f"Valor desperdiçado: R$ {registro['Valor desperdiçado']:.2f}")
        print(f"\nDesperdício: {registro['Percentual de desperdício']:.2f}%")
        print(f"Classificação: {registro['Classificação']}")
        print("Recomendação:", recomendar_por_classificacao(registro["Classificação"]))

    mostrar_titulo("RESUMO FINAL")
    maior_percentual = dados.loc[dados["Percentual de desperdício"].idxmax()]
    maior_valor = dados.loc[dados["Valor desperdiçado"].idxmax()]
    print(f"- Total desperdiçado: R$ {dados['Valor desperdiçado'].sum():.2f}")
    print(f"- Média de desperdício: {dados['Percentual de desperdício'].mean():.2f}%")
    print(
        "- Maior desperdício percentual: "
        f"{maior_percentual['Alimento']} "
        f"({maior_percentual['Percentual de desperdício']:.2f}%)"
    )
    print(
        "- Maior desperdício em valor: "
        f"{maior_valor['Alimento']} (R$ {maior_valor['Valor desperdiçado']:.2f})"
    )

    rankings = [
        ("TOP 5 por valor", "Valor desperdiçado", "R$ {:.2f}"),
        ("TOP 5 por percentual", "Percentual de desperdício", "{:.2f}%"),
    ]
    for titulo, coluna, formato in rankings:
        print(f"\n{titulo}")
        ordenados = dados.sort_values(coluna, ascending=False).head(5)
        for posicao, (_, item) in enumerate(ordenados.iterrows(), start=1):
            print(f"{posicao} - {item['Alimento']}: {formato.format(item[coluna])}")


def analisar_desperdicio(historico):
    """Controla o submenu de análise de desperdício."""
    while True:
        mostrar_titulo("1 - ANALISAR DESPERDÍCIO")
        print("1 - Cadastrar desperdício")
        print("2 - Ver relatório geral")
        print("3 - Gerar gráficos")
        print("4 - Voltar ao menu principal")
        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3", "4"])
        if opcao == "1":
            cadastrar_desperdicio(historico)
        elif opcao == "2":
            mostrar_relatorio(historico)
        elif opcao == "3":
            gerar_graficos(historico)
        else:
            return

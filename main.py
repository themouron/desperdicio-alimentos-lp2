"""Ponto de entrada do Sistema de Controle de Desperdício Alimentar."""

from src.dados import carregar_historico
from src.desperdicio import analisar_desperdicio
from src.planejamento import planejar_compras
from src.utils import ler_opcao, mostrar_titulo


def mostrar_conscientizacao():
    """Apresenta orientações sobre a redução do desperdício."""
    mostrar_titulo("3 - CONSCIENTIZAÇÃO")
    print(
        "\nO desperdício de alimentos causa prejuízos econômicos, sociais e "
        "ambientais. Planejar a quantidade comprada e preparada ajuda a reduzir "
        "gastos e evita o descarte de alimentos próprios para consumo."
    )
    print(
        "\nEste sistema auxilia restaurantes, escolas, refeitórios e unidades "
        "de alimentação a analisar desperdícios e planejar suas compras."
    )
    ler_opcao("\n1 - Voltar ao menu principal: ", ["1"])


def mostrar_menu_principal():
    print("\nBem-vindo ao Sistema de Controle de Desperdício Alimentar\n")
    print("1 - Analisar desperdício")
    print("2 - Planejar compras")
    print("3 - Conscientização")
    print("4 - Sair")


def main():
    """Carrega o histórico e controla apenas o menu principal."""
    historico = carregar_historico()
    while True:
        mostrar_menu_principal()
        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3", "4"])
        if opcao == "1":
            analisar_desperdicio(historico)
        elif opcao == "2":
            planejar_compras()
        elif opcao == "3":
            mostrar_conscientizacao()
        else:
            print("Encerrando o sistema. Até logo!")
            return


if __name__ == "__main__":
    main()

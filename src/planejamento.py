"""Planejamento de compras e estimativas de consumo."""

from src.dados import ALIMENTOS, CATEGORIAS
from src.utils import ler_float, ler_inteiro, ler_opcao, mostrar_titulo


def escolher_alimento(categoria):
    """Exibe o catálogo de uma categoria e retorna o item escolhido."""
    itens = ALIMENTOS[categoria]
    while True:
        print(f"\nAlimentos - {categoria}")
        for indice, item in enumerate(itens, start=1):
            print(
                f"{indice} - {item['nome']} ({item['per_capita']} "
                f"{item['unidade_per_capita']} por pessoa)"
            )
        voltar = len(itens) + 1
        print(f"{voltar} - Voltar")
        opcao = ler_inteiro("Escolha uma opção: ")
        if 1 <= opcao <= len(itens):
            return itens[opcao - 1]
        if opcao == voltar:
            return None
        print("Opção inválida. Tente novamente.")


def estimar_consumo(item, pessoas):
    """Calcula a quantidade total e a converte para kg ou litros."""
    total_original = item["per_capita"] * pessoas
    unidade = "kg" if item["unidade_per_capita"] == "g" else "litros"
    return total_original, total_original / 1000, unidade


def consultar_estimativa(categoria):
    """Solicita um alimento e apresenta sua estimativa de consumo."""
    item = escolher_alimento(categoria)
    if item is None:
        return
    pessoas = ler_inteiro("Quantidade de pessoas: ")
    original, convertido, unidade = estimar_consumo(item, pessoas)
    print(f"\n{pessoas} pessoas")
    print(
        f"{item['nome']}: {item['per_capita']} "
        f"{item['unidade_per_capita']} por pessoa"
    )
    print(
        f"Total: {original:.2f} {item['unidade_per_capita']} = "
        f"{convertido:.2f} {unidade}"
    )


def estimar_refeicao_completa():
    """Monta uma refeição com várias categorias e calcula quantidades e custos."""
    mostrar_titulo("ESTIMAR REFEIÇÃO COMPLETA")
    pessoas = ler_inteiro("Quantidade de pessoas: ")
    itens_escolhidos = []

    for categoria in CATEGORIAS.values():
        pergunta = f"\nAdicionar item em {categoria}? (s/n): "
        if ler_opcao(pergunta, ["s", "n"]) == "n":
            continue
        while True:
            item = escolher_alimento(categoria)
            if item is not None:
                original, convertido, unidade = estimar_consumo(item, pessoas)
                itens_escolhidos.append(
                    {
                        "Item": item["nome"],
                        "Categoria": categoria,
                        "Per capita": (
                            f"{item['per_capita']} {item['unidade_per_capita']}"
                        ),
                        "Pessoas": pessoas,
                        "Total necessário": (
                            f"{original:.2f} {item['unidade_per_capita']} = "
                            f"{convertido:.2f} {unidade}"
                        ),
                        "Quantidade convertida": convertido,
                        "Unidade convertida": unidade,
                    }
                )
            pergunta = "Adicionar outro desta categoria? (s/n): "
            if ler_opcao(pergunta, ["s", "n"]) == "n":
                break

    if not itens_escolhidos:
        print("Nenhum item foi escolhido para a refeição completa.")
        return

    import pandas as pd

    dados = pd.DataFrame(itens_escolhidos)
    colunas = ["Item", "Categoria", "Per capita", "Pessoas", "Total necessário"]
    print("\nTabela da refeição completa:")
    print(dados[colunas].to_string(index=False))

    if ler_opcao("\nCalcular custo estimado? (s/n): ", ["s", "n"]) == "s":
        custo_total = 0
        print("\nCustos dos itens:")
        for item in itens_escolhidos:
            preco = ler_float(
                f"Preço por {item['Unidade convertida']} de {item['Item']}: "
            )
            custo = item["Quantidade convertida"] * preco
            custo_total += custo
            print(f"- Custo de {item['Item']}: R$ {custo:.2f}")
        print(f"\nCusto total da refeição: R$ {custo_total:.2f}")


def planejar_compras():
    """Controla o submenu de planejamento de compras."""
    while True:
        mostrar_titulo("2 - PLANEJAR COMPRAS")
        for numero, categoria in CATEGORIAS.items():
            print(f"{numero} - {categoria}")
        print("6 - Estimar refeição completa")
        print("7 - Voltar ao menu principal")
        opcoes = ["1", "2", "3", "4", "5", "6", "7"]
        opcao = ler_opcao("Escolha uma opção: ", opcoes)
        if opcao in CATEGORIAS:
            consultar_estimativa(CATEGORIAS[opcao])
        elif opcao == "6":
            estimar_refeicao_completa()
        else:
            return

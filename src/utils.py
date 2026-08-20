"""Funções de entrada e apresentação compartilhadas pelo sistema."""

SEPARADOR = "=" * 50


def mostrar_titulo(titulo):
    """Exibe um título com separadores."""
    print(f"\n{SEPARADOR}\n{titulo}\n{SEPARADOR}")


def ler_opcao(mensagem, opcoes_validas):
    """Lê uma opção válida sem diferenciar letras maiúsculas e minúsculas."""
    opcoes = {str(opcao).lower() for opcao in opcoes_validas}
    while True:
        opcao = input(mensagem).strip().lower()
        if opcao in opcoes:
            return opcao
        print("Opção inválida. Tente novamente.")


def ler_texto(mensagem):
    """Lê um texto que não pode estar vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada inválida. O texto não pode ficar vazio.")


def ler_float(mensagem, minimo=0, permitir_zero=False):
    """Lê um número decimal, aceitando vírgula como separador."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor > minimo or (permitir_zero and valor == minimo):
                return valor
            mensagem_erro = (
                "Digite um número válido."
                if permitir_zero
                else "Digite um número maior que zero."
            )
            print(mensagem_erro)
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_inteiro(mensagem, minimo=1):
    """Lê um número inteiro maior ou igual ao mínimo informado."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número inteiro maior ou igual a {minimo}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

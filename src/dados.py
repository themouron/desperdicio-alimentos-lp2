"""Catálogo de alimentos e persistência do histórico em JSON."""

import json
from pathlib import Path


PASTA_DADOS = Path("data")
ARQUIVO_HISTORICO = PASTA_DADOS / "historico.json"

CATEGORIAS = {
    "1": "Proteínas",
    "2": "Cereais, grãos e massas",
    "3": "Verduras e legumes",
    "4": "Frutas",
    "5": "Bebidas",
}


def criar_item(nome, categoria, per_capita, unidade="g"):
    """Cria um alimento para uso no planejamento de compras."""
    return {
        "nome": nome,
        "categoria": categoria,
        "per_capita": per_capita,
        "unidade_per_capita": unidade,
    }


def _criar_itens(categoria, itens, unidade="g"):
    """Converte pares de nome e quantidade em itens do catálogo."""
    return [
        criar_item(nome, categoria, quantidade, unidade)
        for nome, quantidade in itens
    ]


ALIMENTOS = {
    "Proteínas": _criar_itens(
        "Proteínas",
        [
            ("Filé de frango", 130),
            ("Frango com osso", 250),
            ("Carne bovina", 120),
            ("Carne moída", 120),
            ("Peixe", 120),
            ("Peixe em filé/pescada", 150),
            ("Ovo", 75),
            ("Linguiça", 90),
        ],
    ),
    "Cereais, grãos e massas": _criar_itens(
        "Cereais, grãos e massas",
        [
            ("Arroz tipo 1", 50),
            ("Arroz integral", 80),
            ("Feijão", 40),
            ("Lentilha", 40),
            ("Grão-de-bico", 40),
            ("Macarrão", 50),
            ("Massa fresca", 60),
            ("Farinha de mandioca", 35),
            ("Farofa temperada", 30),
            ("Milho verde", 175),
        ],
    ),
    "Verduras e legumes": _criar_itens(
        "Verduras e legumes",
        [
            ("Alface", 40),
            ("Abóbora", 100),
            ("Abobrinha", 100),
            ("Batata", 100),
            ("Batata doce", 100),
            ("Beterraba", 100),
            ("Brócolis", 100),
            ("Cenoura", 55),
            ("Chuchu", 80),
            ("Couve", 27),
            ("Couve-flor", 80),
            ("Pepino", 55),
            ("Pimentão", 10),
            ("Tomate", 80),
        ],
    ),
    "Frutas": _criar_itens(
        "Frutas",
        [
            ("Banana", 100),
            ("Maçã", 150),
            ("Laranja", 100),
            ("Mamão", 150),
            ("Melancia", 200),
            ("Melão", 150),
            ("Abacaxi", 150),
            ("Manga", 100),
            ("Pera", 110),
            ("Morango", 100),
        ],
    ),
    "Bebidas": _criar_itens(
        "Bebidas",
        [
            ("Suco de laranja", 200),
            ("Suco de melão", 200),
            ("Água de coco", 250),
            ("Leite", 200),
            ("Iogurte", 200),
        ],
        "mL",
    ),
}


def carregar_historico(caminho=ARQUIVO_HISTORICO):
    """Carrega os registros; devolve uma lista vazia quando o arquivo não existe."""
    caminho = Path(caminho)
    if not caminho.exists():
        return []
    try:
        with caminho.open(encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError) as erro:
        print(f"Não foi possível ler o histórico: {erro}")
        return []
    return dados if isinstance(dados, list) else []


def salvar_historico(historico, caminho=ARQUIVO_HISTORICO):
    """Grava todos os registros em JSON, criando a pasta de dados se necessário."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=2)


def adicionar_registro(registro, historico, caminho=ARQUIVO_HISTORICO):
    """Adiciona um registro à lista e persiste a alteração."""
    historico.append(registro)
    salvar_historico(historico, caminho)

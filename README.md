# Sistema de Controle de Desperdício Alimentar

Projeto desenvolvido em Python para a disciplina de Linguagem de Programação II da UFRRJ.

A ideia do sistema é registrar sobras de alimentos, calcular o desperdício e o prejuízo financeiro gerado, além de auxiliar no planejamento de compras de acordo com a quantidade de pessoas.

## Funcionalidades

- Cadastro dos alimentos comprados e das respectivas sobras;
- cálculo da quantidade consumida;
- cálculo do percentual de desperdício;
- cálculo do valor financeiro desperdiçado;
- classificação dos níveis de desperdício;
- recomendações com base nos resultados;
- ranking dos alimentos com maior desperdício;
- geração de gráficos;
- planejamento de compras por quantidade de pessoas;
- histórico dos registros entre execuções.

## Cálculos utilizados

O percentual de desperdício é calculado pela relação entre a quantidade que sobrou e a quantidade comprada:

```text
Percentual de desperdício = (Quantidade sobrada / Quantidade comprada) × 100
```

Para estimar o prejuízo financeiro:

```text
Valor desperdiçado = Quantidade sobrada × Preço por unidade
```

Com esses dados, o programa também calcula médias e gera rankings para facilitar a análise dos registros.

## Planejamento de compras

Além do registro de desperdício, o sistema possui uma função para estimar a quantidade de alimentos necessária para uma refeição.

O usuário informa o número de pessoas e escolhe os alimentos. A partir disso, o programa calcula uma estimativa da quantidade necessária e, caso os preços sejam informados, o custo aproximado da refeição.

### Referência dos valores per capita

Os valores de consumo per capita usados como base para o planejamento foram adaptados do **Manual de Per Capita para o Programa Nacional de Alimentação Escolar (PNAE)**, elaborado pela **Universidade Federal de Alfenas (UNIFAL-MG)**.

Foram utilizados valores de referência para grupos como proteínas, cereais, frutas, verduras, legumes e bebidas.

Esses valores são usados apenas como referência para as estimativas do projeto.

## Tecnologias

- Python
- Pandas
- Matplotlib
- JSON
- Unittest
- Git e GitHub

## Estrutura

```text
.
├── main.py
├── src/
│   ├── dados.py
│   ├── desperdicio.py
│   ├── planejamento.py
│   ├── graficos.py
│   └── utils.py
├── data/
├── graficos/
├── tests/
├── requirements.txt
└── README.md
```

O `main.py` funciona como ponto de entrada do programa e controla o menu principal.

Os outros arquivos foram separados de acordo com suas responsabilidades:

| Arquivo | Função |
|---|---|
| `dados.py` | Catálogo de alimentos e persistência dos dados |
| `desperdicio.py` | Cadastro, cálculos e análises de desperdício |
| `planejamento.py` | Planejamento de compras e estimativas |
| `graficos.py` | Geração dos gráficos |
| `utils.py` | Funções auxiliares e validações |

## Dados e histórico

O histórico dos registros é armazenado em:

```text
data/historico.json
```

Assim, os registros não são perdidos quando o programa é encerrado e podem ser utilizados posteriormente nas análises.

Os gráficos gerados pelo sistema são salvos na pasta:

```text
graficos/
```

## Como executar

É necessário ter Python 3.10 ou superior instalado.

Clone o repositório:

```bash
git clone https://github.com/themouron/desperdicio-alimentos-lp2.git
cd desperdicio-alimentos-lp2
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Testes

Os testes podem ser executados com:

```bash
python -m unittest discover -s tests -v
```

## Autor

**Daniel Mourão**

Bacharelado em Matemática - Universidade Federal Rural do Rio de Janeiro (UFRRJ)

Trabalho desenvolvido para a disciplina de **Linguagem de Programação II**  
Professor: **Robson Mariano da Silva**

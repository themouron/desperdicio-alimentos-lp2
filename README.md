# Sistema de Controle de Desperdício Alimentar

Trabalho de LP II em Python para registrar sobras, analisar o desperdício de
alimentos e planejar compras com base no consumo por pessoa.

## Funcionalidades

- cadastro de alimentos comprados e das respectivas sobras;
- cálculo de consumo, desperdício percentual e prejuízo financeiro;
- relatório com classificação, recomendações e rankings;
- gráficos em barras e pizza, salvos na pasta `graficos/`;
- estimativa de quantidades e custos de uma refeição completa.
- histórico preservado entre execuções no arquivo `data/historico.json`.

## Organização do projeto

```text
.
├── main.py                 # ponto de entrada e menu principal
├── src/
│   ├── dados.py            # catálogo e persistência em JSON
│   ├── desperdicio.py      # cadastro, cálculos, relatório e submenu
│   ├── planejamento.py     # estimativas e planejamento de compras
│   ├── graficos.py         # geração das imagens
│   └── utils.py            # validação de entradas e apresentação
├── data/                   # histórico criado durante o uso
├── graficos/               # imagens geradas pelo programa
├── tests/
└── requirements.txt
```

Cada módulo reúne uma responsabilidade do sistema. O arquivo `main.py` apenas
carrega o histórico e direciona as opções do menu principal.

## Como executar

É necessário ter Python 3.10 ou mais recente instalado.

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Autores

- Daniel Mourão
- William Leão

Professor Robson Mariano da Silva — LP II — 2026.

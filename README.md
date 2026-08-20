# 🍽️ Sistema de Controle de Desperdício Alimentar

Sistema desenvolvido em **Python** para registrar, analisar e visualizar dados relacionados ao desperdício de alimentos, além de auxiliar no planejamento de compras com base em estimativas de consumo per capita.

O projeto foi desenvolvido na disciplina de **Linguagem de Programação II (UFRRJ)** e busca aplicar programação e análise de dados a um problema real: o desperdício alimentar em restaurantes, escolas, refeitórios e outras unidades de alimentação.

---

## 🎯 Objetivo

Transformar registros de compra e sobra de alimentos em informações que possam auxiliar na identificação de desperdícios e no planejamento de refeições.

A partir dos dados informados pelo usuário, o sistema calcula indicadores como:

- Percentual de desperdício;
- quantidade efetivamente consumida;
- valor financeiro desperdiçado;
- média geral de desperdício;
- alimentos com maiores perdas;
- estimativa de consumo por número de pessoas;
- custo estimado de refeições.

---

## 📊 Funcionalidades

### 🔎 Análise de desperdício

- Registro de alimentos comprados e respectivas sobras;
- cálculo automático do percentual de desperdício;
- cálculo do valor financeiro perdido;
- classificação do nível de desperdício;
- recomendações de acordo com os resultados;
- ranking dos alimentos com maiores desperdícios;
- histórico preservado entre diferentes execuções.

### 📈 Visualização de dados

Utilizando **Pandas** e **Matplotlib**, o sistema processa os registros e gera visualizações para facilitar a interpretação dos resultados.

Os gráficos são armazenados automaticamente na pasta:

```text
graficos/
```

Entre as análises geradas estão:

- desperdício percentual por alimento;
- participação dos alimentos no valor total desperdiçado.

### 🛒 Planejamento de compras

O sistema permite estimar a quantidade necessária de alimentos de acordo com o número de pessoas de uma refeição.

É possível selecionar alimentos de diferentes categorias e obter automaticamente:

- consumo estimado por pessoa;
- quantidade total necessária;
- conversão das quantidades para quilogramas ou litros;
- estimativa opcional do custo da refeição.

---

## 📐 Metodologia dos cálculos

O percentual de desperdício é calculado a partir da relação entre a quantidade que sobrou e a quantidade inicialmente comprada:

```text
Percentual de desperdício = (Quantidade sobrada / Quantidade comprada) × 100
```

O valor financeiro correspondente ao desperdício é calculado por:

```text
Valor desperdiçado = Quantidade sobrada × Preço por unidade
```

A partir desses indicadores, o sistema permite comparar registros, gerar rankings e identificar os alimentos responsáveis pelos maiores níveis de perda.

---

## 📚 Referência dos dados

Para o módulo de **planejamento de compras**, foram utilizados como referência valores médios de consumo per capita apresentados no **Manual de Per Capita para o Programa Nacional de Alimentação Escolar (PNAE)**, elaborado pela **Universidade Federal de Alfenas (UNIFAL-MG)**.

Os valores foram adaptados para diferentes grupos alimentares utilizados pelo sistema, incluindo:

- proteínas;
- cereais, grãos e massas;
- verduras e legumes;
- frutas;
- bebidas.

O consumo per capita representa uma estimativa da quantidade média de determinado alimento necessária por pessoa e é utilizado pelo sistema para calcular as quantidades necessárias de acordo com o número de pessoas informado.

> **Nota:** os valores são utilizados como referência para fins acadêmicos e de estimativa. O sistema não substitui o planejamento realizado por profissionais de nutrição.

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)

Principais tecnologias e conceitos aplicados:

- **Python**
- **Pandas**
- **Matplotlib**
- **JSON**
- **Unittest**
- **Git / GitHub**
- Análise e manipulação de dados
- Visualização de dados

---

## 📁 Estrutura do projeto

```text
.
├── main.py
│
├── src/
│   ├── dados.py
│   ├── desperdicio.py
│   ├── planejamento.py
│   ├── graficos.py
│   └── utils.py
│
├── data/
├── graficos/
├── tests/
│
├── requirements.txt
└── README.md
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada e controle do menu principal |
| `dados.py` | Catálogo e persistência dos dados |
| `desperdicio.py` | Cadastro, cálculos, relatórios e análise |
| `planejamento.py` | Estimativas de consumo e planejamento de compras |
| `graficos.py` | Geração das visualizações |
| `utils.py` | Validação de entradas e funções auxiliares |

A separação em módulos mantém as diferentes responsabilidades do sistema organizadas e facilita sua manutenção e expansão.

---

## 💾 Persistência dos dados

Os registros realizados durante a utilização do sistema são preservados entre execuções no arquivo:

```text
data/historico.json
```

Dessa forma, os dados cadastrados anteriormente podem ser reutilizados para novas análises, relatórios e visualizações.

---

## 🔄 Fluxo do projeto

```text
Entrada de dados
      ↓
Registro do desperdício
      ↓
Processamento com Python / Pandas
      ↓
Cálculo dos indicadores
      ↓
Relatórios e rankings
      ↓
Visualizações com Matplotlib
      ↓
Apoio à tomada de decisão
```

Além da análise dos registros, o módulo de planejamento utiliza valores de consumo per capita para estimar as quantidades necessárias de alimentos de acordo com o número de pessoas.

---

## ▶️ Como executar

É necessário possuir **Python 3.10 ou superior** instalado.

### 1. Clone o repositório

```bash
git clone https://github.com/themouron/desperdicio-alimentos-lp2.git
cd desperdicio-alimentos-lp2
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o sistema

```bash
python main.py
```

---

## 🧪 Testes

O projeto possui testes automatizados para verificar funções importantes do sistema.

Execute com:

```bash
python -m unittest discover -s tests -v
```

---

## 🚀 Possíveis evoluções

Algumas possibilidades para evolução do projeto:

- armazenamento dos dados em **Excel ou banco de dados**;
- geração automatizada de relatórios;
- criação de dashboards para acompanhamento dos indicadores;
- análise histórica do desperdício;
- comparação entre diferentes períodos;
- novas métricas e visualizações;
- interface gráfica ou aplicação web.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como trabalho da disciplina de **Linguagem de Programação II**, utilizando conceitos de programação aplicados a um problema real.

O projeto também explora conceitos relacionados à **análise de dados**, utilizando registros históricos, indicadores, agregações e visualizações como ferramentas de apoio à tomada de decisão.

---

## 👨‍💻 Autor

**Daniel Mourão**

Bacharelado em Matemática — **Universidade Federal Rural do Rio de Janeiro (UFRRJ)**

**Disciplina:** Linguagem de Programação II  
**Professor:** Robson Mariano da Silva

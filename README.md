# Gráficos de Dados

Scripts Python para geração de gráficos a partir de arquivos CSV.
**Cada gráfico tem seu próprio script**, conforme solicitado.

## Estrutura do projeto

```
graficos/
├── dados/      # arquivos CSV de entrada
├── scripts/    # um script Python por gráfico
├── saida/      # imagens PNG geradas pelos scripts
└── README.md
```

## Scripts e gráficos

| Script | Arquivo de dados | Tipo de gráfico | O que mostra |
|--------|------------------|-----------------|--------------|
| `01_grafico_barras.py` | `dados_barras.csv` | Barras agrupadas | Vendas médias por categoria e região |
| `02_grafico_boxplot.py` | `dados_boxplot.csv` | Boxplot | Distribuição de salários por departamento |
| `03_grafico_dispersao.py` | `dados_dispersao.csv` | Dispersão | Relação altura × peso por sexo |
| `04_grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma | Distribuição de idades dos clientes |
| `05_grafico_frequencia.py` | `dados_frequencia.csv` | Barras horizontais | Frequência de chamados por tipo de atendimento |
| `06_grafico_linhas.py` | `dados_linhas.csv` | Linhas | Evolução das vendas diárias por loja |
| `07_grafico_pizza.py` | `dados_pizza.csv` | Pizza | Participação no faturamento por canal de venda |
| `08_grafico_regressao.py` | `dados_regressao.csv` | Regressão linear | Gasto mensal em função da renda (com reta, equação e R²) |
| `09_grafico_heatmap.py` | `dados_heatmap.csv` | Heatmap (mapa de calor) | Movimento de clientes por dia da semana e horário |

> Observação: `dados_regressao.csv` e `dados_regressao_1.csv` são idênticos.
> O script `08` usa `dados_regressao.csv`; para gerar a partir do outro,
> basta trocar a variável `NOME_CSV` no topo do script.

## Requisitos

- Python 3.9+
- Bibliotecas: `pandas`, `numpy`, `matplotlib`

Instalação das dependências:

```bash
pip install pandas numpy matplotlib
```

## Como executar

Cada script é independente. A partir da pasta `scripts/`:

```bash
cd scripts
python 01_grafico_barras.py
python 02_grafico_boxplot.py
# ... e assim por diante
```

Para rodar todos de uma vez (Linux/macOS):

```bash
cd scripts
for s in *.py; do python "$s"; done
```

Cada script lê o CSV correspondente em `../dados/` e salva o gráfico
em `../saida/` como arquivo PNG.

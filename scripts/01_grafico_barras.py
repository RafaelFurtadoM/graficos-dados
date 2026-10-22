"""
Gráfico de Barras — Vendas médias por categoria e região
Arquivo de dados: dados_barras.csv (colunas: categoria, regiao, vendas_medias)

Mostra as vendas médias de cada categoria de produto, agrupadas por região,
usando barras agrupadas (uma cor por região).
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Caminhos relativos ao local do script
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_barras.csv")
SAIDA = os.path.join(BASE, "saida", "01_grafico_barras.png")

# Leitura dos dados
df = pd.read_csv(CSV)

# Tabela pivô: linhas = categorias, colunas = regiões
pivot = df.pivot(index="categoria", columns="regiao", values="vendas_medias")
# Ordem lógica das regiões
ordem_regioes = ["Norte", "Sul", "Leste", "Oeste"]
pivot = pivot[[r for r in ordem_regioes if r in pivot.columns]]

categorias = pivot.index.tolist()
regioes = pivot.columns.tolist()

x = np.arange(len(categorias))
largura = 0.8 / len(regioes)
cores = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

fig, ax = plt.subplots(figsize=(11, 6))
for i, regiao in enumerate(regioes):
    desloc = (i - (len(regioes) - 1) / 2) * largura
    ax.bar(x + desloc, pivot[regiao].values, largura,
           label=regiao, color=cores[i % len(cores)], edgecolor="white")

ax.set_title("Vendas médias por categoria e região", fontsize=14, fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias (R$)")
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend(title="Região")
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

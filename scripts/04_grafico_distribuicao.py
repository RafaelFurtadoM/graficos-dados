"""
Histograma — Distribuição de idades dos clientes
Arquivo de dados: dados_distribuicao.csv (colunas: cliente_id, idade)

Mostra como as idades dos clientes se distribuem em faixas (bins). Inclui
uma linha vertical na média para referência.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_distribuicao.csv")
SAIDA = os.path.join(BASE, "saida", "04_grafico_distribuicao.png")

df = pd.read_csv(CSV)
idades = df["idade"]
media = idades.mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(idades, bins=15, color="#4C72B0", edgecolor="white", alpha=0.85)
ax.axvline(media, color="#C44E52", linestyle="--", linewidth=2,
           label=f"Média = {media:.1f} anos")

ax.set_title("Distribuição de idades dos clientes", fontsize=14, fontweight="bold")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Frequência (nº de clientes)")
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

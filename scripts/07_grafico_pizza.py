"""
Gráfico de Pizza — Faturamento por canal de venda
Arquivo de dados: dados_pizza.csv (colunas: canal_venda, faturamento)

Mostra a participação de cada canal de venda no faturamento total, em
percentual. A maior fatia é destacada (explode) para dar ênfase.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_pizza.csv")
SAIDA = os.path.join(BASE, "saida", "07_grafico_pizza.png")

df = pd.read_csv(CSV).sort_values("faturamento", ascending=False)

cores = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]

# Destaca a maior fatia
explode = [0.05 if i == 0 else 0 for i in range(len(df))]

fig, ax = plt.subplots(figsize=(9, 8))
wedges, textos, autotextos = ax.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    autopct=lambda p: f"{p:.1f}%\n(R$ {p/100*df['faturamento'].sum():,.0f})",
    startangle=90,
    counterclock=False,
    colors=cores[:len(df)],
    explode=explode,
    wedgeprops=dict(edgecolor="white", linewidth=2),
    textprops=dict(fontsize=10),
)
for autotexto in autotextos:
    autotexto.set_color("white")
    autotexto.set_fontweight("bold")
    autotexto.set_fontsize(9)

ax.set_title("Participação no faturamento por canal de venda",
             fontsize=14, fontweight="bold")
ax.axis("equal")  # círculo perfeito

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

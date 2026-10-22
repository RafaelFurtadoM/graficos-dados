"""
Boxplot — Distribuição de salários por departamento
Arquivo de dados: dados_boxplot.csv (colunas: departamento, salario)

Compara a distribuição salarial entre os departamentos. O boxplot evidencia
mediana, quartis e outliers (valores atípicos) de cada grupo.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_boxplot.csv")
SAIDA = os.path.join(BASE, "saida", "02_grafico_boxplot.png")

df = pd.read_csv(CSV)

# Ordena departamentos pela mediana salarial (do menor para o maior)
ordem = df.groupby("departamento")["salario"].median().sort_values().index.tolist()
dados = [df.loc[df["departamento"] == dep, "salario"].values for dep in ordem]

fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(dados, tick_labels=ordem, patch_artist=True, showmeans=True,
                medianprops=dict(color="#C44E52", linewidth=2),
                meanprops=dict(marker="D", markerfacecolor="white",
                               markeredgecolor="black", markersize=6),
                flierprops=dict(marker="o", markerfacecolor="#888888",
                                markersize=5, alpha=0.6))

cores = ["#4C72B0", "#55A868", "#DD8452", "#8172B3"]
for patch, cor in zip(bp["boxes"], cores):
    patch.set_facecolor(cor)
    patch.set_alpha(0.7)

ax.set_title("Distribuição de salários por departamento", fontsize=14, fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

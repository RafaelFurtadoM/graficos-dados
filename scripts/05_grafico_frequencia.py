"""
Gráfico de Frequência (barras horizontais) — Tipos de atendimento
Arquivo de dados: dados_frequencia.csv (colunas: id_chamado, tipo_atendimento)

Conta quantos chamados existem de cada tipo de atendimento e ordena do mais
frequente ao menos frequente. Os rótulos mostram a contagem de cada categoria.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_frequencia.csv")
SAIDA = os.path.join(BASE, "saida", "05_grafico_frequencia.png")

df = pd.read_csv(CSV)

# Contagem de frequência por tipo, ordenada
freq = df["tipo_atendimento"].value_counts().sort_values()

fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.barh(freq.index, freq.values, color="#55A868",
                 edgecolor="white", alpha=0.9)

# Rótulo de contagem ao final de cada barra
for barra, valor in zip(barras, freq.values):
    ax.text(valor + 1, barra.get_y() + barra.get_height() / 2,
            str(valor), va="center", fontsize=10)

ax.set_title("Frequência de chamados por tipo de atendimento",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Quantidade de chamados")
ax.set_ylabel("Tipo de atendimento")
ax.grid(axis="x", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)
ax.set_xlim(0, freq.max() * 1.1)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

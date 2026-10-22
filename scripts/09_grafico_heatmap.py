"""
Heatmap (mapa de calor) — Movimento de clientes por dia da semana e horário
Arquivo de dados: dados_heatmap.csv (colunas: dia_semana, horario, movimento_clientes)

Cada célula mostra o movimento de clientes em um cruzamento de dia da semana
(linhas) e horário (colunas). Cores mais quentes = maior movimento. O valor
numérico é anotado em cada célula.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_heatmap.csv")
SAIDA = os.path.join(BASE, "saida", "09_grafico_heatmap.png")

df = pd.read_csv(CSV)

# Ordem lógica dos dias (segunda a domingo) e dos horários
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
ordem_horarios = sorted(df["horario"].unique())

# Tabela cruzada: linhas = dias, colunas = horários, valores = movimento
pivot = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
pivot = pivot.reindex(index=ordem_dias, columns=ordem_horarios)

matriz = pivot.values

fig, ax = plt.subplots(figsize=(11, 7))
im = ax.imshow(matriz, cmap="YlOrRd", aspect="auto")

# Eixos
ax.set_xticks(np.arange(len(ordem_horarios)))
ax.set_xticklabels(ordem_horarios)
ax.set_yticks(np.arange(len(ordem_dias)))
ax.set_yticklabels(ordem_dias)

# Anota o valor em cada célula, com cor de texto contrastante
limite = np.nanmax(matriz) * 0.6
for i in range(len(ordem_dias)):
    for j in range(len(ordem_horarios)):
        valor = matriz[i, j]
        if not np.isnan(valor):
            cor = "white" if valor > limite else "black"
            ax.text(j, i, int(valor), ha="center", va="center",
                    color=cor, fontsize=9)

# Barra de cores
cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Movimento de clientes", rotation=270, labelpad=18)

ax.set_title("Movimento de clientes por dia da semana e horário",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

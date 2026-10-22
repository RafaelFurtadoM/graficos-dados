"""
Gráfico de Regressão Linear — Gasto mensal x Renda mensal
Arquivo de dados: dados_regressao.csv (colunas: renda_mensal, gasto_mensal)

Mostra os pontos observados (renda x gasto) com a reta de regressão linear
ajustada por mínimos quadrados. Exibe a equação da reta e o R² no gráfico.

Observação: dados_regressao.csv e dados_regressao_1.csv são idênticos.
Basta trocar o nome do arquivo na variável NOME_CSV para gerar o outro.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

NOME_CSV = "dados_regressao.csv"  # ou "dados_regressao_1.csv"

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", NOME_CSV)
SAIDA = os.path.join(BASE, "saida", "08_grafico_regressao.png")

df = pd.read_csv(CSV)
x = df["renda_mensal"].values
y = df["gasto_mensal"].values

# Ajuste linear por mínimos quadrados: y = a*x + b
a, b = np.polyfit(x, y, 1)
y_prev = a * x + b

# Coeficiente de determinação R²
ss_res = np.sum((y - y_prev) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot

# Linha de regressão suave
x_linha = np.linspace(x.min(), x.max(), 100)
y_linha = a * x_linha + b

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(x, y, color="#4C72B0", alpha=0.6, edgecolor="white", s=50,
           label="Observações")
ax.plot(x_linha, y_linha, color="#C44E52", linewidth=2.5,
        label=f"Regressão: y = {a:.3f}x + {b:.1f}\nR² = {r2:.3f}")

ax.set_title("Regressão linear — Gasto mensal em função da renda",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend(loc="upper left")
ax.grid(linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")
print(f"Equação: y = {a:.4f}x + {b:.2f} | R² = {r2:.4f}")

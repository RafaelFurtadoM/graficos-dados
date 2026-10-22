"""
Gráfico de Linhas — Evolução das vendas por loja ao longo do tempo
Arquivo de dados: dados_linhas.csv (colunas: data, vendas, loja)

Traça uma linha por loja mostrando a evolução diária das vendas no período.
Útil para comparar tendências entre as lojas.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_linhas.csv")
SAIDA = os.path.join(BASE, "saida", "06_grafico_linhas.png")

df = pd.read_csv(CSV, parse_dates=["data"])
df = df.sort_values("data")

cores = {"Loja A": "#4C72B0", "Loja B": "#DD8452"}

fig, ax = plt.subplots(figsize=(12, 6))
for loja, grupo in df.groupby("loja"):
    grupo = grupo.sort_values("data")
    ax.plot(grupo["data"], grupo["vendas"], label=loja,
            color=cores.get(loja, "#888888"), linewidth=1.8, marker="o",
            markersize=3)

ax.set_title("Evolução das vendas diárias por loja", fontsize=14, fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas (R$)")
ax.legend(title="Loja")
ax.grid(linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

# Eixo X com datas legíveis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
fig.autofmt_xdate(rotation=45)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

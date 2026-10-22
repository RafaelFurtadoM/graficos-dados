"""
Gráfico de Dispersão — Altura x Peso por sexo
Arquivo de dados: dados_dispersao.csv (colunas: altura_cm, peso_kg, sexo)

Mostra a relação entre altura e peso de cada indivíduo, com as cores
distinguindo o sexo. Útil para observar correlação e agrupamentos.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, "dados", "dados_dispersao.csv")
SAIDA = os.path.join(BASE, "saida", "03_grafico_dispersao.png")

df = pd.read_csv(CSV)

cores = {"Masculino": "#4C72B0", "Feminino": "#C44E52"}

fig, ax = plt.subplots(figsize=(9, 7))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"],
               label=sexo, color=cores.get(sexo, "#888888"),
               alpha=0.7, edgecolor="white", s=55)

ax.set_title("Relação entre altura e peso por sexo", fontsize=14, fontweight="bold")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
ax.grid(linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(SAIDA, dpi=150)
print(f"Gráfico salvo em: {SAIDA}")

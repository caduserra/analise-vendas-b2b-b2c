
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("vendas.csv")

# Receita total
df["receita"] = df["quantidade"] * df["preco_unitario"]

# Receita média por tipo de cliente
media_receita = df.groupby("tipo_cliente")["receita"].mean().sort_values(ascending=False)

# Plotar gráfico
plt.figure(figsize=(10, 6))
bars = plt.bar(media_receita.index, media_receita.values, width=0.6)
plt.title("Receita Média por Tipo de Cliente", fontsize=16)
plt.ylabel("Receita Média (R$)", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 100, f"R${yval:,.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.savefig("grafico_receita_media.png")
plt.show()

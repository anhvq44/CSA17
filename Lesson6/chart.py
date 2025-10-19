import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Lesson6/spotify.csv")
df.isna().sum()

df.tail()

plt.figure(figsize=(14, 6))
plt.plot(df["Monthly Listeners (Millions)"], marker="o", linestyle="-", linewidth=2)
plt.ylabel("Monthly Listeners (Millions)", fontsize="14")
plt.title("Biểu đồ đường số người nghe theo tháng")

plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
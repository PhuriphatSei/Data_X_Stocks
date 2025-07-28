import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_pe_roe_trend(df: pd.DataFrame, output_path="output/pe_roe_trend.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")

    ax = sns.scatterplot(
        data=df,
        x="ROE",
        y="PE",
        hue="Symbol",
        palette="Set2",
        s=100,
        edgecolor="black",
        legend=False
    )

    for _, row in df.iterrows():
        plt.text(
            row["ROE"] + 0.005,
            row["PE"] + 0.2,
            row["Symbol"].replace(".BK", ""),
            fontsize=9,
            weight="bold"
        )

    plt.title("📈 PE vs ROE (SET50 Stocks)", fontsize=14)
    plt.xlabel("ROE (Return on Equity)", fontsize=12)
    plt.ylabel("PE (Price to Earnings)", fontsize=12)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"✅ บันทึกกราฟ PE vs ROE ที่ {output_path}")

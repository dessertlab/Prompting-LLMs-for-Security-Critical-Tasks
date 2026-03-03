import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kendalltau

sheet_metrics = "performance by metric"
sheet_validation = "Validation"
metric_columns = ["ED", "METEOR", "BLEU-4", "rouge-l"]

# Funzione per mappare PASS/FAIL a 1/0
def map_pass_fail_to_bin(x):
    s = str(x).strip().upper()
    if s == "PASS":
        return 1
    if s == "FAIL":
        return 0
    return np.nan

# Config modelli
MODELS = [
    {
        "metrics_file": "VP Dataset GPT-4o performance analysis.xlsx",
        "validation_file": "VP Dataset GPT-4o.xlsx",
        "label": "GPT-4o",
        "short": "GPT",
    },
    {
        "metrics_file": "VP Dataset Llama-3_1 performance analysis.xlsx",
        "validation_file": "VP Dataset Llama-3_1.xlsx",
        "label": "Llama-3.1",
        "short": "Llama",
    },
    {
        "metrics_file": "VP Dataset Phi-3_5 performance analysis.xlsx",
        "validation_file": "VP Dataset Phi-3_5.xlsx",
        "label": "Phi-3.5",
        "short": "Phi",
    },
    {
        "metrics_file": "VP Dataset Qwen-2_5 performance analysis.xlsx",
        "validation_file": "VP Dataset Qwen-2_5.xlsx",
        "label": "Qwen-2_5",
        "short": "Qwen",
    },
]

# Colori per metrica
COLOR_BY_METRIC = {
    "ED": "#4C78A8",
    "METEOR": "#F58518",
    "BLEU-4": "#54A24B",
    "rouge-l": "#E45756",
}

# Costruzione dataset complessivo
rows = [] 
for M in MODELS:
    df_metrics = pd.read_excel(M["metrics_file"], sheet_name=sheet_metrics).rename(
        columns={"Unnamed: 0": "pattern"}
    )
    df_metrics["pattern"] = df_metrics["pattern"].str.strip()

    df_val = pd.read_excel(M["validation_file"], sheet_name=sheet_validation)

    patterns = [p for p in df_metrics["pattern"].tolist() if p in df_val.columns]

    rate_rows = []
    for p in patterns:
        col = df_val[p].map(map_pass_fail_to_bin)
        rate = col.mean(skipna=True)
        n = col.notna().sum()
        rate_rows.append({"pattern": p, "success_rate": rate, "n": n})
    df_rates = pd.DataFrame(rate_rows)

    df_join = df_metrics[df_metrics["pattern"].isin(patterns)].merge(df_rates, on="pattern", how="inner")
    df_join["model"] = M["short"]

    keep_cols = ["model", "pattern", "success_rate"] + [c for c in metric_columns if c in df_join.columns]
    rows.append(df_join[keep_cols])

df_all = pd.concat(rows, ignore_index=True)

print("\n=== Correlazioni di Kendall complessive (tutti i modelli) ===")
results = {}  
for m in metric_columns:
    if m in df_all.columns:
        x = pd.to_numeric(df_all[m], errors="coerce")
        y = pd.to_numeric(df_all["success_rate"], errors="coerce")
        mask = x.notna() & y.notna()
        x_, y_ = x[mask].values, y[mask].values
        n = len(x_)
        if n >= 2:
            tau, p = kendalltau(x_, y_)
            results[m] = tau
            print(f"{m:8s}  tau = {tau: .4f}   p = {p: .4g}   (n={n})")
        else:
            results[m] = np.nan
            print(f"{m:8s}  dati insufficienti (n < 2)")
    else:
        results[m] = np.nan
        print(f"{m:8s}  colonna non trovata nei file metriche")

output_pdf = "correlations_kendall.pdf"
metrics_presenti = [m for m in metric_columns if m in results]
y = [results[m] for m in metrics_presenti]
colors = [COLOR_BY_METRIC.get(m, None) for m in metrics_presenti]

plt.figure(figsize=(7, 4.5))
xpos = np.arange(len(metrics_presenti))
plt.bar(xpos, y, width=0.6, color=colors)
plt.axhline(0, linewidth=1, color="gray")

plt.xticks(xpos, metrics_presenti)
plt.ylabel("Correlazione (Kendall τ)")
plt.title("Correlazioni Kendall complessive (metriche vs success rate)")

plt.tight_layout()
plt.savefig(output_pdf, format="pdf")
plt.close()

print(f"\nGrafico complessivo salvato in: {output_pdf}")


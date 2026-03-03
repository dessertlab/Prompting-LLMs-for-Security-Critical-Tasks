import pandas as pd
import numpy as np
import os

def analyze_excel_performance(excel_path: str, metric_sheets: list, output_suffix=" performance analysis"):
    base_name = os.path.splitext(os.path.basename(excel_path))[0]
    output_excel_path = os.path.join(
        os.path.dirname(excel_path),
        f"{base_name}{output_suffix}.xlsx"
    )

    media_mediana_df = pd.DataFrame()
    devstd_df = pd.DataFrame()

    for sheet in metric_sheets:
        df = pd.read_excel(excel_path, sheet_name=sheet)

        try:
            start_col = df.columns.get_loc("Ground truth code") + 1
            end_col = df.columns.get_loc("Baseline") + 1
        except KeyError as e:
            raise ValueError(f"Colonna mancante nel foglio '{sheet}': {e}")

        metric_values = []
        std_values = []

        for col in df.columns[start_col:end_col]:
            col_data = pd.to_numeric(df[col], errors='coerce').dropna()
            if col_data.empty:
                metric_values.append(np.nan)
                std_values.append(np.nan)
                continue

            mean = col_data.mean()
            std = col_data.std()
            cv = std / mean if mean != 0 else np.inf

            value = mean if cv < 0.5 else col_data.median()
            metric_values.append(value)
            std_values.append(std)

        version_names = df.columns[start_col:end_col]
        media_mediana_df[sheet] = pd.Series(metric_values, index=version_names)
        devstd_df[sheet] = pd.Series(std_values, index=version_names)
       
    if "Baseline" in media_mediana_df.index:
        baseline_values = media_mediana_df.loc["Baseline"]
        media_row_means = media_mediana_df.mean(axis=1, skipna=True)
        baseline_mean = baseline_values.mean(skipna=True)
        media_mediana_df["Variazione percentuale"] = ((media_row_means - baseline_mean) / baseline_mean) * 100
    else:
        print("[!] La riga 'Baseline' non è presente: colonna 'Variazione percentuale' non calcolata.")

    media_mediana_df = media_mediana_df.round(3)
    devstd_df = devstd_df.round(3)

    with pd.ExcelWriter(output_excel_path) as writer:
        media_mediana_df.to_excel(writer, sheet_name="performance by metric")
        devstd_df.to_excel(writer, sheet_name="analisi dev std")

    print(f"[✓] File salvato: {output_excel_path}")
    return media_mediana_df, devstd_df, output_excel_path


metric_sheets = ["ED", "METEOR", "BLEU-4", "rouge-l"]
for i in range (1, 5):
    if i == 1:
        excel_path= "VP Dataset Llama-3_1.xlsx"
    elif i == 2:
        excel_path= "VP Dataset GPT-4o.xlsx"
    elif i == 3:
        excel_path= "VP Dataset Phi-3_5.xlsx"
    elif i == 4:
        excel_path= "VP Dataset_Qwen-2_5.xlsx"

    analyze_excel_performance(excel_path, metric_sheets)

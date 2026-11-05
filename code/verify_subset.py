from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    data_path = base / "data" / "heldout_row_group_R1.csv"
    sensitivity_path = base / "data" / "mask_sensitivity_GF.csv"
    output_dir = base / "outputs"
    output_dir.mkdir(exist_ok=True)

    data = pd.read_csv(data_path)
    sensitivity = pd.read_csv(sensitivity_path)

    expected_stages = ["返青期", "起身期", "拔节期", "孕穗期", "灌浆期"]
    stage_counts = data.groupby("stage").size().to_dict()
    if len(data) != 200:
        raise ValueError(f"expected 200 records, found {len(data)}")
    if data["plot_id"].nunique() != 40:
        raise ValueError("the held-out row group should contain 40 plots")
    if sorted(data["stage"].unique()) != sorted(expected_stages):
        raise ValueError("unexpected stage labels")
    if data["SPAD"].isna().any():
        raise ValueError("SPAD contains missing values")

    stage_summary = (
        data.groupby(["stage_order", "stage"], as_index=False)
        .agg(records=("SPAD", "size"), mean_SPAD=("SPAD", "mean"),
             sd_SPAD=("SPAD", "std"))
        .sort_values("stage_order")
    )
    result = {
        "records": int(len(data)),
        "plots": int(data["plot_id"].nunique()),
        "stage_counts": {str(k): int(v) for k, v in stage_counts.items()},
        "mean_SPAD_by_stage": [
            {k: (float(v) if isinstance(v, (int, float)) else v)
             for k, v in row.items()}
            for row in stage_summary.to_dict(orient="records")
        ],
        "sensitivity_rows": int(len(sensitivity)),
        "sensitivity_GF_RMSE_range": [
            float(sensitivity["RMSE_GF_S"].min()),
            float(sensitivity["RMSE_GF_S"].max()),
        ],
        "sensitivity_pooled_RMSE_range": [
            float(sensitivity["RMSE_all_S"].min()),
            float(sensitivity["RMSE_all_S"].max()),
        ],
    }
    (output_dir / "subset_summary.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

"""Utility functions for Saudi tourism demand and spending analysis."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


def year_to_numeric(value: object) -> float:
    """Convert year values such as '2025 H1' to numeric values such as 2025.5."""
    text = str(value).strip()
    match = re.search(r"(\d{4})", text)
    if not match:
        return np.nan
    year = float(match.group(1))
    if "H1" in text.upper():
        return year + 0.5
    return year


def clean_numeric_series(series: pd.Series) -> pd.Series:
    """Convert numeric columns stored as strings with commas into numeric dtype."""
    return pd.to_numeric(series.astype(str).str.replace(",", "", regex=False), errors="coerce")


def add_spend_per_tourist(df: pd.DataFrame) -> pd.DataFrame:
    """Add spending per tourist when visitors and spends columns are available."""
    data = df.copy()
    if {"VISITORS", "SPENDS"}.issubset(data.columns):
        data["SPEND_PER_TOURIST"] = data["SPENDS"] / data["VISITORS"].replace(0, np.nan)
    return data


def load_raw_datasets(data_dir: str | Path) -> Dict[str, pd.DataFrame]:
    """Load all raw CSV datasets from a folder."""
    data_path = Path(data_dir)
    datasets: Dict[str, pd.DataFrame] = {}
    for csv_file in data_path.glob("*.csv"):
        datasets[csv_file.stem] = pd.read_csv(csv_file)
    return datasets

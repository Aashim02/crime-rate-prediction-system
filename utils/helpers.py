from pathlib import Path

import pandas as pd


def ensure_parent_dir(file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)


def load_csv(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)


def save_csv(df: pd.DataFrame, file_path: Path) -> None:
    ensure_parent_dir(file_path)
    df.to_csv(file_path, index=False)

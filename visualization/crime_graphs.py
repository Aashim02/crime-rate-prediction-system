import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config.config import RAW_DATA_PATH
from visualization.heatmap_visualization import plot_location_crime_heatmap


def plot_crime_distribution(df: pd.DataFrame, show: bool = True) -> None:
    counts = df["crime_type"].value_counts()
    counts.plot(kind="bar", title="Crime Distribution")
    plt.xlabel("Crime Type")
    plt.ylabel("Count")
    plt.tight_layout()
    if show:
        plt.show()
    else:
        plt.close()


def plot_crime_trends(df: pd.DataFrame, show: bool = True) -> None:
    if "timestamp" not in df.columns:
        raise ValueError("timestamp column is required for trend plotting")

    tmp = df.copy()
    tmp["timestamp"] = pd.to_datetime(tmp["timestamp"])
    trend = tmp.groupby(tmp["timestamp"].dt.date).size()

    trend.plot(kind="line", marker="o", title="Crime Trends")
    plt.xlabel("Date")
    plt.ylabel("Incidents")
    plt.tight_layout()
    if show:
        plt.show()
    else:
        plt.close()


def plot_crime_hotspots(df: pd.DataFrame, show: bool = True) -> None:
    plot_location_crime_heatmap(df, show=show)


if __name__ == "__main__":
    frame = pd.read_csv(RAW_DATA_PATH)
    plot_crime_distribution(frame, show=False)
    print("Crime distribution graph generated")
    plot_crime_trends(frame, show=False)
    print("Crime type graph generated")
    plot_crime_hotspots(frame, show=False)
    print("Crime hotspot visualization generated")

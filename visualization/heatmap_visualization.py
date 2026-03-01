import matplotlib.pyplot as plt
import pandas as pd


def plot_location_crime_heatmap(df: pd.DataFrame, show: bool = True) -> None:
    pivot = pd.crosstab(df["location"], df["crime_type"])

    plt.figure(figsize=(8, 5))
    plt.imshow(pivot, aspect="auto")
    plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45, ha="right")
    plt.yticks(range(len(pivot.index)), pivot.index)
    plt.title("Crime Hotspots (Location vs Crime Type)")
    plt.colorbar(label="Incidents")
    plt.tight_layout()
    if show:
        plt.show()
    else:
        plt.close()

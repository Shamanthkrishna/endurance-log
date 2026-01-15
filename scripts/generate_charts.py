import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
DATA_PATH = Path("data/metrics.csv")
CHARTS_PATH = Path("charts")
CHARTS_PATH.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH, parse_dates=["datetime"])
df = df.sort_values("datetime")

# Convert pace mm:ss to minutes
def pace_to_minutes(p):
    if pd.isna(p):
        return None
    m, s = p.strip().split(":")
    return int(m) + int(s) / 60

df["pace_min"] = df["avg_pace"].apply(pace_to_minutes)

# Distance
plt.figure()
plt.plot(df["datetime"], df["distance_km"], marker="o")
plt.xticks(rotation=45)
plt.title("Distance per Session (km)")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "distance.png")
plt.close()

# Avg HR
plt.figure()
plt.plot(df["datetime"], df["avg_hr"], marker="o")
plt.xticks(rotation=45)
plt.title("Average Heart Rate (bpm)")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "avg_hr.png")
plt.close()

# Pace
plt.figure()
plt.plot(df["datetime"], df["pace_min"], marker="o")
plt.xticks(rotation=45)
plt.title("Average Pace (min/km)")
plt.tight_layout()
plt.savefig(CHARTS_PATH / "avg_pace.png")
plt.close()

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

# Create figure
fig, ax1 = plt.subplots(figsize=(12, 6))

# Distance (left axis)
ax1.plot(df["datetime"], df["distance_km"], color="tab:blue", marker="o", label="Distance (km)")
ax1.set_ylabel("Distance (km)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# HR (right axis)
ax2 = ax1.twinx()
ax2.plot(df["datetime"], df["avg_hr"], color="tab:red", marker="o", label="Avg HR (bpm)")
ax2.set_ylabel("Heart Rate (bpm)", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Pace (third axis)
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60))
ax3.plot(df["datetime"], df["pace_min"], color="tab:green", marker="o", label="Avg Pace (min/km)")
ax3.set_ylabel("Pace (min/km)", color="tab:green")
ax3.tick_params(axis="y", labelcolor="tab:green")

# X-axis
ax1.set_xlabel("Session Time")
plt.xticks(rotation=45)

# Title
plt.title("Session Metrics Overview")

# Legend (manual)
lines = ax1.get_lines() + ax2.get_lines() + ax3.get_lines()
labels = [line.get_label() for line in lines]
plt.legend(lines, labels, loc="upper left")

plt.tight_layout()
plt.savefig(CHARTS_PATH / "session_overview.png")
plt.close()

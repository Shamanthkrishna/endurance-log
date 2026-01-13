import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metrics.csv")

# Convert pace mm:ss to minutes
def pace_to_minutes(p):
    m, s = p.split(":")
    return int(m) + int(s)/60

df["pace_min"] = df["avg_pace"].apply(pace_to_minutes)

# Distance
plt.figure()
plt.plot(df["date"], df["distance_km"], marker="o")
plt.xticks(rotation=45)
plt.title("Distance per Day")
plt.tight_layout()
plt.savefig("charts/distance.png")
plt.close()

# Avg HR
plt.figure()
plt.plot(df["date"], df["avg_hr"], marker="o")
plt.xticks(rotation=45)
plt.title("Average Heart Rate")
plt.tight_layout()
plt.savefig("charts/avg_hr.png")
plt.close()

# Pace
plt.figure()
plt.plot(df["date"], df["pace_min"], marker="o")
plt.xticks(rotation=45)
plt.title("Average Pace (min/km)")
plt.tight_layout()
plt.savefig("charts/avg_pace.png")
plt.close()

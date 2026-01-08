import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("healthcare_analytics_data.csv")

# ---------- Basic summaries ----------
print("\nAverage TotalCost:", round(df["TotalCost"].mean(), 2))
print("Median TotalCost:", df["TotalCost"].median())

chronic_summary = df.groupby("ChronicCondition")[["Visits", "TotalCost"]].mean().round(2)
print("\nAverage Visits and TotalCost by ChronicCondition:")
print(chronic_summary)

insurance_summary = df.groupby("InsuranceType")[["Visits", "TotalCost"]].mean().round(2)
print("\nAverage Visits and TotalCost by InsuranceType:")
print(insurance_summary)

corr_visits_cost = df["Visits"].corr(df["TotalCost"])
print("\nCorrelation between Visits and TotalCost:", round(corr_visits_cost, 3))

corr_age_cost = df["Age"].corr(df["TotalCost"])
print("Correlation between Age and TotalCost:", round(corr_age_cost, 3))

# -------- Plot 1: Chronic vs Non-chronic (bar) --------
cost_by_chronic = df.groupby("ChronicCondition")["TotalCost"].mean()

plt.figure()
cost_by_chronic.plot(kind="bar")
plt.title("Average Total Healthcare Cost by Chronic Condition")
plt.xlabel("Chronic Condition")
plt.ylabel("Average Total Cost")
plt.tight_layout()
plt.savefig("avg_cost_by_chronic.png", dpi=200)
plt.close()

# -------- Plot 2: Visits vs TotalCost (scatter) --------
plt.figure()
plt.scatter(df["Visits"], df["TotalCost"])
plt.title("Healthcare Visits vs Total Cost")
plt.xlabel("Number of Visits")
plt.ylabel("Total Cost")
plt.tight_layout()
plt.savefig("visits_vs_totalcost.png", dpi=200)
plt.close()

# -------- Plot 3: Age vs TotalCost (scatter) --------
plt.figure()
plt.scatter(df["Age"], df["TotalCost"])
plt.title("Age vs Total Healthcare Cost")
plt.xlabel("Age")
plt.ylabel("Total Cost")
plt.tight_layout()
plt.savefig("age_vs_totalcost.png", dpi=200)
plt.close()

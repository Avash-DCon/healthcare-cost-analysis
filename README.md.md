# Healthcare Cost & Utilization Analysis (Python)

A small healthcare analytics project using Python to explore how patient visits, age, chronic conditions, and insurance type relate to total healthcare cost.

## What I did
- Loaded and inspected CSV data with pandas
- Compared average visits and total cost by:
  - ChronicCondition (Yes/No)
  - InsuranceType (Government/Private)
- Computed correlations:
  - Visits vs TotalCost
  - Age vs TotalCost
- Generated and saved plots with matplotlib

## Files
- `healthcare_analytics_data.csv` — dataset
- `analysis1.py` — analysis script
- `avg_cost_by_chronic.png` — bar chart
- `visits_vs_totalcost.png` — scatter plot
- `age_vs_totalcost.png` — scatter plot

## How to run
```bash
python3 -m pip install pandas matplotlib
python3 analysis1.py

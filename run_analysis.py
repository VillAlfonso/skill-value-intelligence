import sys, os
sys.path.insert(0, os.path.abspath("."))

from src.ingestion.job_market import load_job_data
from src.processing.extract_skills import extract_skills
from src.signals.demand_signal import compute_demand_signal
from src.signals.compensation_signal import compute_compensation_signal
from src.signals.momentum_signal import compute_momentum_signal
from src.models.skill_value_index import compute_skill_value_index

# Load data
df = load_job_data("data/raw/jobs.csv")
df["skills"] = df["description"].apply(extract_skills)

print("\n=== DATA ===")
print(df[["title", "skills"]])

# Signals
demand = compute_demand_signal(df)
comp = compute_compensation_signal(df)
momentum = compute_momentum_signal(df)
svi = compute_skill_value_index(demand, comp)

print("\n=== DEMAND ===")
print(demand)

print("\n=== COMPENSATION ===")
print(comp)

print("\n=== MOMENTUM ===")
print(momentum)

print("\n=== SKILL VALUE INDEX ===")
print(svi)

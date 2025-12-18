import pandas as pd

def compute_demand_signal(df: pd.DataFrame) -> pd.DataFrame:
    exploded = df.explode("skills")

    demand = (
        exploded
        .groupby(["skills"])
        .size()
        .reset_index(name="job_count")
        .sort_values("job_count", ascending=False)
    )

    return demand
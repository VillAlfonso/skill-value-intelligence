import pandas as pd

def compute_compensation_signal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes average salary signal per skill based on job postings.
    """

    # Drop rows with missing salary info
    salary_df = df.dropna(subset=["salary_min", "salary_max"]).copy()

    # Compute midpoint salary
    salary_df["salary_mid"] = (
        salary_df["salary_min"] + salary_df["salary_max"]
    ) / 2

    # Explode skills into separate rows
    exploded = salary_df.explode("skills")

    # Remove rows without skills
    exploded = exploded.dropna(subset=["skills"])

    # Aggregate salary signal per skill
    comp_signal = (
        exploded
        .groupby("skills")["salary_mid"]
        .mean()
        .reset_index()
        .rename(columns={"salary_mid": "avg_salary"})
        .sort_values("avg_salary", ascending=False)
    )

    return comp_signal

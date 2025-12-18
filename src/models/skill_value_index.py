import pandas as pd

def min_max_normalize(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())


def compute_skill_value_index(
    demand_df: pd.DataFrame,
    compensation_df: pd.DataFrame,
    demand_weight: float = 0.5,
    compensation_weight: float = 0.5
) -> pd.DataFrame:
    """
    Combines demand and compensation signals into a single Skill Value Index.
    """

    # Merge signals on skill name
    merged = pd.merge(
        demand_df,
        compensation_df,
        on="skills",
        how="inner"
    )

    # Normalize signals
    merged["demand_norm"] = min_max_normalize(merged["job_count"])
    merged["compensation_norm"] = min_max_normalize(merged["avg_salary"])

    # Compute Skill Value Index
    merged["skill_value_index"] = (
        demand_weight * merged["demand_norm"]
        + compensation_weight * merged["compensation_norm"]
    )

    # Sort by value
    merged = merged.sort_values(
        "skill_value_index",
        ascending=False
    )

    return merged

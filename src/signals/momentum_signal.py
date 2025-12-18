import pandas as pd

def compute_momentum_signal(
    df: pd.DataFrame,
    date_col: str = "date_posted",
    freq: str = "M"
) -> pd.DataFrame:
    """
    Computes momentum as sustained presence over time,
    not raw growth (which is unreliable for small datasets).
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    exploded = df.explode("skills").dropna(subset=["skills"])

    grouped = (
        exploded
        .groupby([pd.Grouper(key=date_col, freq=freq), "skills"])
        .size()
        .reset_index(name="count")
    )

    momentum = (
        grouped
        .groupby("skills")
        .agg(
            total_mentions=("count", "sum"),
            active_periods=("count", "count")
        )
        .assign(
            momentum=lambda x: x["total_mentions"] / x["active_periods"]
        )
        .reset_index()
        .sort_values("momentum", ascending=False)
    )

    return momentum

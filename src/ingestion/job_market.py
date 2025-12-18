# src/ingestion/job_market.py

import pandas as pd

def load_job_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    df = df.rename(columns={
        "job_title": "title",
        "job_description": "description"
    })

    df["source"] = "mock_dataset"

    return df[
        [
            "title",
            "company",
            "location",
            "description",
            "salary_min",
            "salary_max",
            "date_posted",
            "source"
        ]
    ]

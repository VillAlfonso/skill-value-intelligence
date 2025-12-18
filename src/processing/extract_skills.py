COMMON_SKILLS = [
    "python", "sql", "aws", "docker", "javascript",
    "machine learning", "excel", "pandas"
]

def extract_skills(text: str) -> list[str]:
    text = text.lower()
    return [skill for skill in COMMON_SKILLS if skill in text]

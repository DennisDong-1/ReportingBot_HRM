# ===========================================
# 📄 db.py
# Local HR dataset handler
# Loads and queries Kaggle HR dataset (CSV)
# ===========================================

import pandas as pd

# Path to your HR dataset
DATA_PATH = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    raise FileNotFoundError(f"❌ Dataset not found at {DATA_PATH}")

# Normalize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]


def get_employee_info(query: str) -> str:
    """
    Handles common HR-related queries.
    """
    query_lower = query.lower()

    # Average salary query
    if "average" in query_lower and ("salary" in query_lower or "income" in query_lower):
        avg_salary = df["monthly_income"].mean()
        return f"The average employee salary is ${avg_salary:.2f}."

    # Department distribution
    if "department" in query_lower:
        dept_counts = df["department"].value_counts().to_dict()
        return f"Department distribution: {dept_counts}"

    # Attrition rate
    if "attrition" in query_lower or "turnover" in query_lower:
        attrition_rate = (df["attrition"].value_counts(normalize=True).get("Yes", 0)) * 100
        return f"The employee attrition rate is approximately {attrition_rate:.1f}%."

    # Salary details
    if "salary" in query_lower or "income" in query_lower:
        min_salary = df["monthly_income"].min()
        max_salary = df["monthly_income"].max()
        return f"Salaries range from ${min_salary} to ${max_salary}."

    # General stats
    if "employee count" in query_lower or "how many employees" in query_lower:
        total = len(df)
        return f"There are {total} employees in the company."

    # Fallback
    return None

import plotly.express as px
import pandas as pd


def salary_chart():

    data = pd.DataFrame({
        "Level": ["Entry", "Mid", "Senior"],
        "Salary (LPA)": [8, 18, 35]
    })

    fig = px.bar(
        data,
        x="Level",
        y="Salary (LPA)",
        title="Average Salary by Experience Level"
    )

    return fig


def skill_chart():

    data = pd.DataFrame({
        "Skill": [
            "Python",
            "SQL",
            "Machine Learning",
            "Docker",
            "AWS"
        ],
        "Demand": [95, 80, 90, 75, 85]
    })

    fig = px.bar(
        data,
        x="Skill",
        y="Demand",
        title="Current Skill Demand"
    )

    return fig
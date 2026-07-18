from langchain_core.messages import SystemMessage, HumanMessage

from models.llm import llm
from models.prompts import CAREER_SYSTEM_PROMPT


def generate_market_analysis(target_role):

    prompt = f"""
You are an expert career market analyst.

Analyze the career market for:

{target_role}

Generate a report including:

1. Career Overview
2. Current Industry Demand
3. Future Growth
4. Average Salary (Entry, Mid, Senior)
5. Top Hiring Companies
6. Required Skills
7. Trending Technologies
8. Best Certifications
9. Challenges
10. Final Recommendation

Use headings and bullet points.
"""

    messages = [
        SystemMessage(content=CAREER_SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    return response.content
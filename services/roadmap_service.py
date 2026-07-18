from langchain_core.messages import SystemMessage, HumanMessage

from models.llm import llm
from models.prompts import CAREER_SYSTEM_PROMPT


def generate_career_roadmap(resume_text, target_role):

    prompt = f"""
You are an expert career mentor.

The student wants to become:

{target_role}

Resume:

{resume_text}

Generate a detailed roadmap including:

1. Current Profile Summary
2. Skills Already Possessed
3. Skills to Learn
4. 30-Day Plan
5. 90-Day Plan
6. 6-Month Roadmap
7. Best Projects to Build
8. Recommended Certifications
9. Interview Preparation Plan
10. Final Career Advice

Use headings and bullet points.
"""

    messages = [
        SystemMessage(content=CAREER_SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    return response.content
from langchain_core.messages import SystemMessage, HumanMessage
from models.llm import llm
from models.prompts import CAREER_SYSTEM_PROMPT


def analyze_resume(resume_text):

    prompt = f"""
Analyze the following resume.

Resume:
{resume_text}

Generate a professional report with:

1. Resume Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. Recommended Projects
6. Recommended Certifications
7. Career Roles Suitable
8. ATS Score (out of 100)
9. Improvement Suggestions

Use proper headings and bullet points.
"""

    messages = [
        SystemMessage(content=CAREER_SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    return response.content
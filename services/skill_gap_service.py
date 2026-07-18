from models.llm import llm


def analyze_skill_gap(resume_text, target_role):

    prompt = f"""
You are an expert Career Coach.

The user's target career is:

{target_role}

Analyze the following resume.

Provide:

1. Current Skills
2. Missing Skills for becoming a {target_role}
3. Strengths
4. Weaknesses
5. Recommended Certifications
6. Projects to Build
7. Learning Resources
8. Final Improvement Plan

Resume:

{resume_text}
"""

    response = llm.invoke(prompt)

    return response.content
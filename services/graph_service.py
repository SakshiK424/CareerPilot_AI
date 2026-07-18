from agents.career_agent import career_graph


def run_career_graph(resume_text, target_role):

    initial_state = {
        "resume_text": resume_text,
        "target_role": target_role,
        "resume_report": "",
        "market_report": "",
        "roadmap_report": ""
    }

    final_state = career_graph.invoke(initial_state)

    return final_state
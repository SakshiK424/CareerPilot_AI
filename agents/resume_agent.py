from services.career_service import analyze_resume


class ResumeAgent:

    def run(self, state):

        state["resume_report"] = analyze_resume(
            state["resume_text"]
        )

        return state
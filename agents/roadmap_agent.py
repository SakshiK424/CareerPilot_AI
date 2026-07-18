from services.roadmap_service import generate_career_roadmap


class RoadmapAgent:

    def run(self, state):

        state["roadmap_report"] = generate_career_roadmap(
            state["resume_text"],
            state["target_role"]
        )

        return state
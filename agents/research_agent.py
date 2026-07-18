from services.market_service import generate_market_analysis


class ResearchAgent:

    def run(self, state):

        state["market_report"] = generate_market_analysis(
            state["target_role"]
        )

        return state
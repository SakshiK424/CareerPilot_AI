from typing import TypedDict


class CareerState(TypedDict):
    resume_text: str
    target_role: str

    resume_report: str
    market_report: str
    roadmap_report: str
from langgraph.graph import StateGraph, END

from agents.state import CareerState
from agents.resume_agent import ResumeAgent
from agents.research_agent import ResearchAgent
from agents.roadmap_agent import RoadmapAgent


resume_agent = ResumeAgent()
research_agent = ResearchAgent()
roadmap_agent = RoadmapAgent()


def resume_node(state):
    return resume_agent.run(state)


def research_node(state):
    return research_agent.run(state)


def roadmap_node(state):
    return roadmap_agent.run(state)


builder = StateGraph(CareerState)

builder.add_node("resume", resume_node)
builder.add_node("research", research_node)
builder.add_node("roadmap", roadmap_node)

builder.set_entry_point("resume")

builder.add_edge("resume", "research")
builder.add_edge("research", "roadmap")
builder.add_edge("roadmap", END)

career_graph = builder.compile()
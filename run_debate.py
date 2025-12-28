from langgraph.graph import StateGraph, END

from nodes.user_input_node import user_input_node
from nodes.coordinator_node import coordinator_node
from nodes.agent_node import agent_a_node, agent_b_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node

state = {}

graph = StateGraph(dict)

graph.add_node("USER_INPUT", user_input_node)
graph.add_node("COORDINATOR", coordinator_node)
graph.add_node("AgentA", agent_a_node)
graph.add_node("AgentB", agent_b_node)
graph.add_node("MEMORY", memory_node)
graph.add_node("JUDGE", judge_node)

graph.set_entry_point("USER_INPUT")

graph.add_edge("USER_INPUT", "COORDINATOR")

graph.add_conditional_edges(
    "COORDINATOR",
    lambda s: s["_route"],
    {
        "AgentA": "AgentA",
        "AgentB": "AgentB",
        "JUDGE": "JUDGE"
    }
)

graph.add_edge("AgentA", "MEMORY")
graph.add_edge("AgentB", "MEMORY")
graph.add_edge("MEMORY", "COORDINATOR")

graph.add_edge("JUDGE", END)

app = graph.compile()

if __name__ == "__main__":
    app.invoke(state, {"recursion_limit": 100})
    print("\nDebate finished cleanly.")

from graphviz import Digraph

dot = Digraph(
    name="Multi-Agent Debate DAG",
    format="png",
    comment="ATG Multi-Agent Debate Workflow"
)

# Global graph styling
dot.attr(
    rankdir="TB",
    fontsize="12",
    fontname="Helvetica",
    labelloc="t",
    label="Multi-Agent Debate DAG (LangGraph)",
)

dot.attr("node", shape="box", style="rounded,filled", fontname="Helvetica")

# --- Nodes ---
dot.node("UserInput", "User Input\n(CLI)", fillcolor="#E3F2FD")
dot.node("Coordinator", "Coordinator\n(Round Controller)", fillcolor="#FFF3E0")

dot.node("AgentA", "Agent A\nScientist", fillcolor="#E8F5E9")
dot.node("AgentB", "Agent B\nPhilosopher", fillcolor="#E8F5E9")

dot.node("Memory", "Memory Node\n(Transcript + Checks)", fillcolor="#F3E5F5")

dot.node("Judge", "Judge Node\n(Summary + Winner)", fillcolor="#FFEBEE")
dot.node("END", "END", shape="oval", fillcolor="#CFD8DC")

# --- Edges ---
dot.edge("UserInput", "Coordinator", label="start")

dot.edge("Coordinator", "AgentA", label="AgentA turn")
dot.edge("Coordinator", "AgentB", label="AgentB turn")

dot.edge("AgentA", "Memory")
dot.edge("AgentB", "Memory")

dot.edge("Memory", "Coordinator", label="next round")

dot.edge("Coordinator", "Judge", label="after 8 rounds", color="red", penwidth="2")
dot.edge("Judge", "END", color="black", penwidth="2")

# --- Render ---
dot.render("dag", cleanup=True)
print("✅ DAG generated as dag.png")

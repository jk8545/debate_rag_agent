🧠 Multi-Agent Debate DAG using LangGraph

Role: Machine Learning Intern
Assignment: ATG Technical Assignment
Tech Stack: Python · LangGraph · Groq LLM · Graphviz · CLI
Deadline: 48 hours

📌 Overview

This project implements a multi-agent debate system using LangGraph, where two AI agents debate a given topic in a strictly controlled, turn-based manner.

The system enforces:

Exact round limits

Turn order correctness

Debate memory tracking

Repetition prevention

Final judgment with reasoning

The entire workflow is modeled as a Directed Acyclic Graph (DAG) and executed via a clean CLI interface, with full logging of every node and state transition.

🎯 Objectives Met

✔ Exactly 8 rounds (4 turns per agent, alternating)
✔ Strict turn control (no agent speaks out of turn)
✔ Memory preservation and incremental updates
✔ Repetition detection to avoid duplicated arguments
✔ Judge node producing summary + winner + justification
✔ Persistent logging of all events
✔ Graphviz DAG visualization
✔ Deterministic execution (optional seed)

🧩 System Architecture

The system is implemented as a LangGraph DAG, where each node represents a well-defined responsibility.

Core Nodes
Node	Responsibility
UserInputNode	Accepts and validates debate topic via CLI
CoordinatorNode	Enforces turn order and round count
AgentA (Scientist)	Produces structured, evidence-based arguments
AgentB (Philosopher)	Produces conceptual and ethical arguments
MemoryNode	Stores debate transcript and summary
JudgeNode	Reviews full debate and declares winner
LoggerNode	Logs every node input/output and state snapshot
🔁 Debate Flow (High Level)
UserInput
   ↓
Coordinator
   ↓
AgentA / AgentB (alternating)
   ↓
Memory
   ↓
Coordinator
   ↓
Judge (after 8 rounds)
   ↓
END

🧠 Memory Structure

The debate memory is stored in a structured JSON format:

{
  "turns": [
    {
      "round": 1,
      "agent": "Scientist",
      "text": "Argument text..."
    }
  ],
  "summary": "Running structured summary of the debate"
}


Each agent only receives relevant memory context, not the full state.

⚖️ Judge Logic

The JudgeNode:

Reads the full debate transcript

Checks logical progression and coherence

Produces:

A concise debate summary

Winner declaration (AgentA or AgentB)

A reasoned justification

Example output:

[Judge]
Winner: Scientist
Reason: Presented grounded, risk-based arguments aligned with public safety principles.

🖥️ CLI Usage
Run the debate
python run_debate.py


You will be prompted:

Enter topic for debate: Should AI be regulated like medicine?

Example Output
[Round 1] Scientist: ...
[Round 2] Philosopher: ...
...
[Round 8] Philosopher: ...

[Judge]
Summary of debate:
...

Winner: Scientist
Reason: ...

📝 Logging

All node executions, state transitions, memory updates, and the final verdict are logged to a persistent JSON log file:

logs/
 └── debate_log_YYYYMMDD_HHMMSS.json


Each log entry includes:

Timestamp

Node name

Input state

Output state

This makes the system fully auditable and debuggable.

🖼️ DAG Visualization

The debate workflow is visualized using Graphviz.

Generate the DAG:

python generate_dag.py


This produces:

dag.png


The diagram clearly shows:

Control flow

Agent alternation

Memory loop

Final termination

⚙️ Configuration (Optional)

You may configure:

Random seed (for deterministic behavior)

Persona prompts

Log file path

Example (optional):

python run_debate.py --seed 42 --log-path logs/

🧪 Testing & Validation

The system has been manually validated for:

✅ Turn enforcement

✅ Exact round count

✅ Memory updates after each turn

✅ Judge output correctness

✅ Clean termination

✅ Log file generation

📁 Project Structure
.
├── run_debate.py
├── generate_dag.py
├── nodes/
│   ├── user_input_node.py
│   ├── coordinator_node.py
│   ├── agent_node.py
│   ├── memory_node.py
│   ├── judge_node.py
│   └── logger_node.py
├── persona_templates/
│   ├── scientist.txt
│   └── philosopher.txt
├── logs/
│   └── debate_log_*.json
├── dag.png
└── README.md

🎥 Demo Video (Included)

The demo video shows:

CLI execution

Debate flow

Judge decision

Log file output

DAG visualization

🚀 Conclusion

This project demonstrates:

Controlled multi-agent orchestration

Clean DAG-based reasoning workflows

Strong separation of concerns

Robust state management and logging

It is designed to be extensible, auditable, and production-aligned, making it suitable as a foundation for more complex agent-based systems.
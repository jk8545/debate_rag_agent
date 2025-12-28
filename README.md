# DebateFlow 🎭⚡

A LangGraph-powered multi-agent debate system with memory, control, logging, and automated judgment.

DebateFlow simulates a structured AI debate between two expert personas — a Scientist and a Philosopher — using LangGraph DAGs and Groq LLMs. The system enforces strict turn control, preserves debate memory, logs every state transition, and concludes with an automated judge verdict.

Built as part of a Machine Learning Intern technical assignment, with emphasis on clarity, control, and correctness.


🌟 Features

## 🎯 Core Capabilities

- Dual-Agent Architecture
  - Scientist (evidence & risk-based) vs Philosopher (ethics & values-driven)

- Exactly 8 Rounds
  - 4 turns per agent, strictly alternating — programmatically enforced

- Memory-Aware Debate
  - Incremental transcript + structured summary updated after each round

- Automated Judge
  - Reviews full debate history and produces a final summary, winner declaration, and logical justification

- Full CLI Experience
  - Round-by-round output streamed to terminal and persistent JSON logging


## 🔧 Technical Highlights

- LangGraph DAG orchestration
- Groq LLM integration (fast, free tier)
- Hard turn enforcement and repetition detection
- Logical flow validation and deterministic seed option
- Persistent JSON Lines logging for auditing
- Graphviz DAG visualization


## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- A Groq API key (free tier available)

### Installation

```bash
# Clone the repository
git clone https://github.com/jk8545/debate_rag_agent.git
cd debate_rag_agent

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Run the Debate

```bash
python run_debate.py
```

You’ll be prompted:

```
Enter topic for debate:
```

Example:

```
Should AI be regulated like medicine?
```


## 🏗️ System Architecture

DebateFlow is implemented as a LangGraph DAG. Each node has a single responsibility; orchestration enforces a strict control loop so the debate always proceeds correctly and terminates after exactly 8 rounds.

### 🔄 High-level Debate Workflow

- UserInputNode — Accepts & validates topic
- CoordinatorNode — Controls turn order and stops debate after 8 rounds
- AgentA (Scientist) / AgentB (Philosopher) — Generate arguments according to persona prompts
- MemoryNode — Stores transcript and updates a structured summary
- JudgeNode — Evaluates debate and declares a winner
- LoggerNode — Logs every node input/output and state snapshot

Flow (simplified DAG):

UserInput
   ↓
Coordinator
   ↓
AgentA ↔ AgentB (alternating)
   ↓
Memory
   ↓
Coordinator
   ↓
Judge
   ↓
END

A visual DAG is generated using Graphviz:

```bash
python generate_dag.py
```

Output:

```
dag.png
```


## 🧠 Memory & State

Memory is stored as structured JSON and updated after each turn. Example memory snapshot:

```json
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
```

Each agent receives the relevant context needed for the next turn (not an unbounded dump of the full state).


## ⚖️ Judge Logic

The JudgeNode reads the full transcript and structured summaries, validates logical progression and coherence, then emits:

- Final summary
- Winner declaration (Scientist or Philosopher)
- Reasoned justification

Example judge output:

```
[Judge]
Winner: Scientist
Reason: Presented grounded, risk-based arguments aligned with public safety principles.
```


## 📁 Project Structure

```
debate_rag_agent/
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
│   └── debate_log_YYYYMMDD.json
├── run_debate.py
├── generate_dag.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```


## 🎭 Agent Personas

### 🔬 Scientist
- Focus: Evidence, risk analysis, empirical reasoning
- Style: Structured, data-driven, pragmatic
- Domains: Technology, safety, regulation, science

### 🧠 Philosopher
- Focus: Ethics, human values, societal impact
- Style: Nuanced, principled, reflective
- Domains: Morality, autonomy, long-term consequences


## 📊 Sample CLI Output

```
Enter topic for debate: Should AI be regulated like medicine?

[Round 1] Scientist: AI systems deployed in healthcare...
[Round 2] Philosopher: Ethical oversight must consider...
...
[Round 8] Philosopher: Historical precedent shows...

[Judge]
Winner: Scientist
Reason: Provided more concrete, risk-based arguments aligned with public safety.
```


## 🧾 Logging & Auditing

Every run produces a persistent JSON Lines log containing timestamps, node inputs & outputs, state transitions, debate transcript, memory snapshots, and the final verdict.

Example log entry (JSONL):

```json
{
  "timestamp": "2025-01-12T18:42:11",
  "event": "ROUND_OUTPUT",
  "agent": "Scientist",
  "round": 3,
  "text": "AI regulation must prioritize..."
}
```


## 🧪 Validation Rules

- Turn order enforcement
- Exactly 8 rounds
- Repetition detection
- Topic consistency checks
- Judge must run exactly once


## 🛠️ Built With

- LangGraph — DAG-based agent orchestration
- Groq LLM — Fast inference
- Python — Core implementation
- Graphviz — DAG visualization
- python-dotenv — Environment management


## 🎯 Use Cases

- Academic: Debate & argumentation analysis, AI ethics education
- Research: Multi-agent interaction modeling, LLM reasoning evaluation
- Practical: Policy debate simulation, ethical review workflows


## 📄 License

MIT License — free to use, modify, and distribute.


## 🙏 Acknowledgments

LangGraph Team — clean agent orchestration
Groq — blazing-fast LLM inference
Open-source community — tools that made this possible


## Contact

If you run into issues or want to contribute, open an issue or submit a PR.


---

Updated README to better reflect system architecture, workflow, and practical usage.

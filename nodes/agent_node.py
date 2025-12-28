import os
from groq import Groq
from dotenv import load_dotenv
from nodes.logger_node import log_event

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_persona(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

SCIENTIST = load_persona("persona_templates/scientist.txt")
PHILOSOPHER = load_persona("persona_templates/philosopher.txt")

def call_llm(prompt):
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()

def build_prompt(persona, state):
    last = state["turns"][-1]["text"] if state["turns"] else ""
    return f"""
{persona}

Debate topic:
{state["topic"]}

Opponent last argument:
{last}

Respond with a concise argument (3–4 sentences).
"""

def agent_a_node(state):
    text = call_llm(build_prompt(SCIENTIST, state))
    print(f'[Round {len(state["turns"])+1}] Scientist: {text}')

    state["last_agent_output"] = {
        "agent": "AgentA",
        "persona": "Scientist",
        "text": text
    }

    log_event("AGENT_A", state["last_agent_output"])
    return state

def agent_b_node(state):
    text = call_llm(build_prompt(PHILOSOPHER, state))
    print(f'[Round {len(state["turns"])+1}] Philosopher: {text}')

    state["last_agent_output"] = {
        "agent": "AgentB",
        "persona": "Philosopher",
        "text": text
    }

    log_event("AGENT_B", state["last_agent_output"])
    return state

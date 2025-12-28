from difflib import SequenceMatcher
from nodes.logger_node import log_event

def is_repeated(text, past):
    return any(SequenceMatcher(None, text, p["text"]).ratio() > 0.85 for p in past)

def memory_node(state):
    out = state["last_agent_output"]

    repeated = is_repeated(out["text"], state["turns"])

    entry = {
        "round": len(state["turns"]) + 1,
        "agent": out["persona"],
        "text": out["text"],
        "repeated": repeated
    }

    state["turns"].append(entry)
    state["summary"] += f'\nRound {entry["round"]} ({entry["agent"]}): {entry["text"]}'

    state["current_turn"] = "AgentB" if out["agent"] == "AgentA" else "AgentA"

    log_event("MEMORY_UPDATE", entry)
    return state

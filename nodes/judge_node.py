import os
from groq import Groq
from dotenv import load_dotenv
from nodes.logger_node import log_event

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def judge_node(state):
    prompt = f"""
Debate topic:
{state["topic"]}

Debate transcript:
{state["summary"]}

Decide the winner (Scientist or Philosopher) and justify logically.
"""

    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    verdict = resp.choices[0].message.content.strip()

    print("\n[Judge Verdict]")
    print(verdict)

    log_event("FINAL_VERDICT", verdict)
    return state

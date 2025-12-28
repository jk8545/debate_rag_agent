def user_input_node(state):
    topic = input("Enter topic for debate: ").strip()

    if len(topic) < 10:
        raise ValueError("Topic must be at least 10 characters")

    state.update({
        "topic": topic,
        "turns": [],
        "summary": "",
        "current_turn": "AgentA",
        "_route": None
    })

    return state

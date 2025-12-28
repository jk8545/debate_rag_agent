def coordinator_node(state):
    if len(state["turns"]) >= 8:
        state["_route"] = "JUDGE"
        return state

    state["_route"] = state["current_turn"]
    return state

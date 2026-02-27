from pprint import pprint

def simulate_approval(state):

    print("\n" + "-" * 70)
    print("STEP: SIMULATE APPROVAL (Deterministic)")
    print("-" * 70)

    print("\nSTATE BEFORE")
    pprint(state)

    print("\nSimulating approval decision...")
    state["approval_status"] = "approved"

    print("\nAPPROVAL STATUS SET TO: approved")

    print("\nSTATE AFTER")
    pprint(state)

    return state

print("tools/approval_tools.py now ready to be used")
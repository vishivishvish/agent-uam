######################################################################
# Importing Libraries
######################################################################

from pprint import pprint

######################################################################
# Simulate Approval Function Tool
######################################################################

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


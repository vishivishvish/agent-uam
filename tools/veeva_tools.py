from pprint import pprint

EXISTING_USERS = ["john.doe@company.com"]


def check_user_exists(state):

    print("\n" + "-" * 70)
    print("STEP: CHECK IF USER EXISTS (Veeva)")
    print("-" * 70)

    print("\nSTATE BEFORE")
    pprint(state)

    email = state["normalized"]["email"]
    print(f"\nChecking existence for email: {email}")

    state["user_exists"] = email in EXISTING_USERS

    if state["user_exists"]:
        print("User already exists in Veeva")
    else:
        print("User does NOT exist in Veeva")

    print("\nSTATE AFTER")
    pprint(state)

    return state


def create_user(state):

    print("\n" + "-" * 70)
    print("STEP: CREATE USER (Veeva Provisioning)")
    print("-" * 70)

    print("\nSTATE BEFORE")
    pprint(state)

    if state["user_exists"]:
        print("\nSkipping creation — user already exists")

        state["provisioning_result"] = {
            "message": "User already exists"
        }

        print("\nSTATE AFTER")
        pprint(state)

        return state

    print("\nCreating new Veeva user...")

    state["provisioning_result"] = {
        "username": "generated_user_123",
        "status": "ACTIVE",
        "system": "Veeva Vault"
    }

    print("User successfully created")

    print("\nSTATE AFTER")
    pprint(state)

    return state


def close_request(state):

    print("\n" + "-" * 70)
    print("STEP: CLOSE SERVICENOW REQUEST")
    print("-" * 70)

    print("\nSTATE BEFORE")
    pprint(state)

    if not state.get("provisioning_result"):
        print("\nNo provisioning result — nothing to close")
        return state

    print("\nUpdating ServiceNow status to Closed Complete")

    state["provisioning_result"]["servicenow_status"] = "Closed Complete"

    print("ServiceNow request closed")

    print("\nSTATE AFTER")
    pprint(state)

    return state


print("tools/veeva_tools.py now ready to be used")
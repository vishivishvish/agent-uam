EXISTING_USERS = ["john.doe@company.com"];

def check_user_exists(email):
    email = state["normalized"]["email"];
    state["user_exists"] = email in EXISTING_USERS;
    return state;

def create_user(state):

    if state["user_exists"]:
        state["provisioning_result"] = \
        {
            "message": "User already exists"
        };
        return state;

    state["provisioning_result"] = \
    {
        "username": "generated_user_123",
        "status": "ACTIVE",
        "system" : "Veeva Vault"
    };

    return state;

def close_request(state):

    if not state.get("provisioning_result"):
        return state;

    state["provisioning_result"]["servicenow_status"] = "Closed Complete";
    return state;
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
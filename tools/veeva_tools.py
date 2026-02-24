EXISTING_USERS = ["john.doe@company.com"];

def check_user_exists(email):
    email = state["normalized"]["email"];
    state["user_exists"] = email in EXISTING_USERS;
    return state;
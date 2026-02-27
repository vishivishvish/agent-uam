ROLE_MAPPING = \
{
    "UL Supplier External User": \
    {
        "approver_name": "Quality Platform Owner",
        "approver_email": "quality.owner@company.com"
    }
};

def resolve_approver(state):

    try:

        role = state["normalized"]["role"];
        approver = ROLE_MAPPING.get(role);

        if not approver:
            raise Exception(f"No approver found for role {role}");

        state["approver"] = approver;
        return state;

    except Exception as e:
        state["errors"] = str(e);
        return state;

print("tools/mapping_tools.py now ready to be used");
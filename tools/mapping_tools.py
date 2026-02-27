from pprint import pprint;

ROLE_MAPPING = \
{
    "UL Supplier External User": \
    {
        "approver_name": "Quality Platform Owner",
        "approver_email": "quality.owner@company.com"
    }
};

def resolve_approver(state):

    print("\n" + "-" * 70);
    print("STEP: RESOLVE APPROVER (Deterministic Mapping)");
    print("-" * 70);

    print("\nSTATE BEFORE");
    pprint(state);

    try:

        role = state["normalized"]["role"];
        print(f"\nLooking up approver for role: {role}")
        approver = ROLE_MAPPING.get(role);

        if not approver:
            raise Exception(f"No approver found for role {role}");

        print("\nAPPROVER FOUND");
        pprint(approver);

        state["approver"] = approver;

        print("\nSTATE AFTER");
        pprint(state);

        return state;

    except Exception as e:
        
        print("\nERROR IN APPROVER RESOLUTION");
        print(str(e));

        state["errors"] = str(e);
        return state;

print("tools/mapping_tools.py now ready to be used");
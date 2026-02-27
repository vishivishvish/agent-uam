import json;
from pprint import pprint;
from engine.llm_config import llm;

REQUIRED_FIELDS = \
[
    "request_number",
    "ritm_number",
    "email",
    "role",
    "environment",
    "country"
];

def validate_and_normalize_request(state):

    raw = state["raw_input"];

    prompt = \
    f"""
    You are an enterprise IAM automation validator.

    Extract and normalize the following required fields:
    {REQUIRED_FIELDS}

    """;

    prompt += \
    """
    If ANY required field is missing or null, return:

    {
    "valid": False,
    "missing_fields": [...] <- You have to provide the missing fields here
    }

    If ALL fields exist, then return:
    {
    "valid": True,
    "normalized":  {
                    ... <- You have to provide the normalized fields here
                   }
    }
    
    Return STRICT JSON only.

    """;

    prompt += \
    f"""
    Input:
    {raw}
    """

    print("Invoking LLM for Validation");

    response = llm.invoke(prompt);

    print("LLM Raw Response:");
    print(response.content);

    try:
        result = json.loads(response.content);
    except Exception as e:
        print("LLM Parse Error");
        print(str(e));
        state["errors"] = "LLM Validation parsing failed";
        return state;

    print("LLM Parsed Response:");
    pprint(result);

    if not result.get("valid"):
        print("Validation Failed");
        print("Missing fields:", result.get("missing_fields"));
        state["errors"] = f"Missing fields: {result.get()}";
        return state;

    print("Validation Successful");
    print("Normalized Output:");
    pprint(result["normalized"]);

    state["normalized"] = result["normalized"];

    print("State after Validation:");
    pprint(state);

    return state; 

print("tools/servicenow_tools.py now ready to be used");
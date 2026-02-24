import json;
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

    response = llm.invoke(prompt);

    try:
        result = json.loads(response.content);
    except:
        state["errors"] = "LLM Validation parsing failed";
        return state;

    if not result.get("valid"):
        state["errors"] = f"Missing fields: {result.get()}";
        return state;

    state["normalized"] = result["normalized"];
    return state; 

print("All good - tools/servicenow_tools.py now ready to be used");
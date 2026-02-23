def extract_request_details(state):
    
    try:
        
        raw = state["raw_input"];

        normalized = \
        {
            "request_number": raw["request_number"],
            "ritm_number": raw["ritm_number"],
            "email": raw["email"],
            "role": raw["role"],
            "environment": raw["environment"],
            "country": raw["country"]
        };

        state["normalized"] = normalized;
        return state;

    except Exception as e:
        state["errors"] = str(e);
        return state;

print("All good - tools/servicenow_tools.py now ready to be used");
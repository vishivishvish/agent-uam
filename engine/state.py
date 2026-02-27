from typing import TypedDict, Optional, Dict, Any

class AgentState(TypedDict):
    raw_input: Dict[str, Any]
    normalized: Optional[Dict[str, Any]]
    approver: Optional[Dict[str, Any]]
    approval_status: Optional[str]
    user_exists: Optional[bool]
    provisioning_result: Optional[Dict[str, Any]]
    errors: Optional[str]

print("engine/state.py now ready to be used");
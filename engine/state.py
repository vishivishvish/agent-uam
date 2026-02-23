from typing import TypedDict, Optional, Dict, Any;

class AgentState(TypedDict):
    raw_input: Dict[str, Any]
    normalized: Optional[Dict[str, Any]]
    approver: Optional[Dict[str, Any]]
    errors: Optional[str]

print("All good - engine/state.py ready to be used");
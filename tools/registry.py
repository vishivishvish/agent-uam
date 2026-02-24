from tools.servicenow_tools import validate_and_normalize_request;
from tools.mapping_tools import resolve_approver;
from tools.approval_tools import simulate_approval;
from tools.veeva_tools import check_user_exists, create_user, close_request;

TOOL_REGISTRY = \
{
    "validate_and_normalize_request": validate_and_normalize_request,
    "resolve_approver": resolve_approver,
    "simulate_approval": simulate_approval,
    "check_user_exists": check_user_exists,
    "create_user": create_user,
    "close_request": close_request  
};

print("All good - tools/registry.py now ready to be used");
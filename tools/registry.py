from tools.servicenow_tools import extract_request_details;
from tools.mapping_tools import resolve_approver;

TOOL_REGISTRY = \
{
    "extract_request_details": extract_request_details,
    "resolve_approver": resolve_approver
}

print("All good - tools/registry.py ready to be used");
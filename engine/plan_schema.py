######################################################################
# Importing Libraries
######################################################################

from typing import List, TypedDict;

######################################################################
# Class Definitions
######################################################################

class PlanStep(TypedDict):
    step: str


class ExecutionPlan(TypedDict):
    intent: str
    steps: List[PlanStep]
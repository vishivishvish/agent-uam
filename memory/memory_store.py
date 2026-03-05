######################################################################
# Importing Libraries
######################################################################

from datetime import datetime

######################################################################
# Memory File & Saving to Memory
######################################################################

MEMORY_FILE = "memory/memory.md"

def save_memory(plan, result):

    with open(MEMORY_FILE, "a") as f:
        f.write("\n---\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Intent: {plan['intent']}\n")
        f.write(f"Steps: {plan['steps']}\n")
        f.write(f"Result: SUCCESS\n")
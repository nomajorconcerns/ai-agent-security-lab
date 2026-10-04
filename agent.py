# A tiny "agent" with a permission list
ALLOWED_TOOLS = ["read_note"]

def run_tool(tool_name):
    if tool_name in ALLOWED_TOOLS:
        print("ALLOWED: agent used " + tool_name)
    else:
        print("BLOCKED: agent tried to use " + tool_name)

run_tool("read_note")
run_tool("delete_files")
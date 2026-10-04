from datetime import datetime

PERMISSIONS = {
    "reader_agent": ["read_note"],
    "admin_agent": ["read_note", "delete_files"],
}

def log(message):
    line = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + message
    print(line)
    with open("audit.log", "a") as f:
        f.write(line + "\n")

def run_tool(agent_name, tool_name):
    allowed = PERMISSIONS.get(agent_name, [])
    if tool_name in allowed:
        log("ALLOWED: " + agent_name + " used " + tool_name)
    else:
        log("BLOCKED: " + agent_name + " tried to use " + tool_name)

run_tool("reader_agent", "read_note")
run_tool("reader_agent", "delete_files")
run_tool("admin_agent", "delete_files")
run_tool("unknown_agent", "read_note")
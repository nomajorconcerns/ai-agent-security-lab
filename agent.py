from datetime import datetime

ALLOWED_TOOLS = ["read_note"]

def log(message):
    line = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + message
    print(line)
    with open("audit.log", "a") as f:
        f.write(line + "\n")

def run_tool(tool_name):
    if tool_name in ALLOWED_TOOLS:
        log("ALLOWED: agent used " + tool_name)
    else:
        log("BLOCKED: agent tried to use " + tool_name)

run_tool("read_note")
run_tool("delete_files")
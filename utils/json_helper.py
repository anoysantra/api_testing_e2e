#write a function to write a helper class to call the json reader insted of writing it again and again
import json

def json_helper_tool(json_file_path):
    with open(json_file_path) as f:
        payload_parameter = json.load(f)
        return payload_parameter
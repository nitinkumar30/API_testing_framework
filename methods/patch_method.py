from utils import send_patch_request

def patch_todo(todo_id, data):
    return send_patch_request(f"todos/{todo_id}", data)

# Example usage (can be tested independently)
if __name__ == "__main__":
    updated_fields = {"title": "Updated title"}
    patched_todo = patch_todo(1, updated_fields)
    print("PATCH:", patched_todo)

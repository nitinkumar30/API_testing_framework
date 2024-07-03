from utils import send_delete_request

def delete_todo(todo_id):
    return send_delete_request(f"todos/{todo_id}")

# Example usage (can be tested independently)
if __name__ == "__main__":
    delete_status = delete_todo(1)
    print("DELETE:", delete_status)

from utils import send_put_request

def update_todo(todo_id, data):
    return send_put_request(f"todos/{todo_id}", data)

# Example usage (can be tested independently)
if __name__ == "__main__":
    updated_todo = {"title": "Buy groceries and milk", "completed": True}
    updated = update_todo(1, updated_todo)
    print("PUT:", updated)

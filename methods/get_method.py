from utils import send_get_request

def get_todo(todo_id):
    return send_get_request(f"{todo_id}")

# Example usage (can be tested independently)
if __name__ == "__main__":
    todo = get_todo("todos/1")
    print("GET:", todo)

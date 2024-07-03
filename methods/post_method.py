from utils import send_post_request

def create_todo(data):
    return send_post_request("todos", data)

# Example usage (can be tested independently)
if __name__ == "__main__":
    new_todo = {"title": "Buy groceries", "completed": False}
    created_todo = create_todo(new_todo)
    print("POST:", created_todo)

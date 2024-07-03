from utils import send_head_request

def get_headers():
    return send_head_request("todos")

# Example usage (can be tested independently)
if __name__ == "__main__":
    headers = get_headers()
    print("HEADERS:", headers)

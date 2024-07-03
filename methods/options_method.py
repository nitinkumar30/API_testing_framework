import sys
from utils import send_options_request


def get_options(endpoint):
    return send_options_request(endpoint)


# Example usage (can be tested independently)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python options_method.py <endpoint>")
        sys.exit(1)

    endpoint = sys.argv[1]
    options = get_options(endpoint)
    print("Allowed Methods:", options)

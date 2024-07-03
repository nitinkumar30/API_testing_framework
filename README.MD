# 🌐 API Testing Project 🚀

## Introduction ℹ️
This project showcases API testing using Python, covering essential HTTP methods such as `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, and `HEAD`. Each method is implemented in its own file under the `methods` directory, promoting modularity and maintainability. The `requests` library is utilized for interacting with an example API (`jsonplaceholder.typicode.com`).

## Features ✨
- **Modular Structure**: Each HTTP method (`GET`, `POST`, etc.) is implemented in separate files (`get_method.py`, `post_method.py`, etc.) under the `methods` directory.
- **Configuration-driven**: Uses `config.json` to store base URL and endpoint details, providing flexibility in API configuration.
- **Command-line Interaction**: The `main.py` script allows dynamic interaction with APIs by accepting command-line arguments for specifying endpoints.

## Folder Structure 📁
```
.\
│
├── methods\
│   ├── delete_method.py
│   ├── get_method.py
│   ├── head_method.py
│   ├── options_method.py
│   ├── patch_method.py
│   ├── post_method.py
│   └── put_method.py
│
├── config.json
├── main.py
└── utils.py
```

## Methods Used 🛠️
- **GET Method** (`get_method.py`):
  - Retrieves data from the specified endpoint using `requests.get()`.

- **POST Method** (`post_method.py`):
  - Creates new data on the API endpoint using `requests.post()` with JSON payload.

- **PUT Method** (`put_method.py`):
  - Updates existing data on the API endpoint using `requests.put()` with JSON payload.

- **DELETE Method** (`delete_method.py`):
  - Deletes data from the API endpoint using `requests.delete()`.

- **PATCH Method** (`patch_method.py`):
  - Partially updates data on the API endpoint using `requests.patch()` with JSON payload.

- **OPTIONS Method** (`options_method.py`):
  - Retrieves the allowed HTTP methods for the specified endpoint using `requests.options()`.

- **HEAD Method** (`head_method.py`):
  - Retrieves the headers for the specified endpoint using `requests.head()`.

## Libraries/Modules Used 📚
- **requests**: Used to send HTTP requests (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD) to the API.
- **json**: Used for JSON serialization and deserialization.
- **sys**: Used in `main.py` for handling command-line arguments.

## Running the Project 🏃‍♂️
1. Ensure Python and the `requests` library are installed.
2. Modify `config.json` to specify your API base URL and endpoint details.
3. Use command-line to run specific method files under the `methods` directory (`python methods/get_method.py`, `python methods/post_method.py`, etc.) for individual testing.
4. Use `main.py` with a command-line argument (`python main.py <endpoint>`) to interact with multiple methods dynamically.

## Additional Notes 📝
- **Error Handling**: Implement robust error handling in each method for handling API responses and network errors.
- **Logging**: Consider integrating logging to track API requests and responses for debugging purposes.
- **Authentication**: Extend the project to include authentication methods like OAuth or API keys for secure API interactions.

## Author ✍️
[**Nitin Kumar**](https://www.linkedin.com/in/nitin30kumar/)

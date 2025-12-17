def login(username, password):
    if username == "" or password == "":
        return "Fields cannot be empty"

    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid credentials"

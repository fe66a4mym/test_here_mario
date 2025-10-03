import os

def write_google_token():
    """
    Reads the GOOGLE_TOKEN environment variable and writes it to token.txt.
    If the variable is not set, it writes a message indicating that.
    """
    token = os.getenv("GOOGLE_TOKEN")
    with open("token.txt", "w") as f:
        if token:
            f.write(token)
        else:
            f.write("GOOGLE_TOKEN environment variable is not set.")

if __name__ == "__main__":
    write_google_token()
from flask import Flask, request

app = Flask(__name__)

def scanPort(hostname, port):
  """Attempts to connect to a specific port on the given hostname."""
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.settimeout(0.5)  # Set a timeout to avoid hanging connections
      result = sock.connect_ex((hostname, port))
      if result == 0:
        return f"Port {port} is OPEN"
      else:
        return f"Port {port} is CLOSED"
  except Exception as e:
    return f"Error connecting to port {port}: {e}"

@app.route("/scan")
def scan():
  """Handles scan requests from the client-side."""
  hostname = request.args.get("host")
  port = int(request.args.get("port"))
  result = scanPort(hostname, port)
  return result

if __name__ == "__main__":
  app.run(debug=True)

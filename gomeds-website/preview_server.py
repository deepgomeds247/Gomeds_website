from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import socket, webbrowser

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

def get_free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

port = get_free_port()
url = f"http://127.0.0.1:{port}/"
print(f"GoMeds preview is running at {url}")
print("Press Ctrl+C in this window to stop the server.")
webbrowser.open(url)
try:
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
except KeyboardInterrupt:
    print("Preview server stopped.")

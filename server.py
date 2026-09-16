import http.server
import socketserver
import webbrowser
import os
import sys
import json
from backend.database import init_db
from backend.api_server import handle_api_request

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class RetinaXAIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def get_json_body(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                raw_data = self.rfile.read(content_length).decode('utf-8')
                return json.loads(raw_data)
        except Exception as e:
            print(f"Error reading JSON body: {e}")
        return {}

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/api/'):
            return handle_api_request(self, 'GET', self.path)
        if self.path == '/' or self.path == '':
            self.send_response(302)
            self.send_header('Location', '/login.html')
            self.end_headers()
            return
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/'):
            return handle_api_request(self, 'POST', self.path)
        self.send_error(404, "Endpoint not found")

    def do_PUT(self):
        if self.path.startswith('/api/'):
            return handle_api_request(self, 'PUT', self.path)
        self.send_error(404, "Endpoint not found")

    def do_DELETE(self):
        if self.path.startswith('/api/'):
            return handle_api_request(self, 'DELETE', self.path)
        self.send_error(404, "Endpoint not found")

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    print("=" * 65)
    print(" Initializing RetinaXAI SQLite Relational Database...")
    init_db()
    print(" SQLite Database initialized with users, patients & screenings.")
    print("=" * 65)

    # Allow socket address reuse so restart is instantaneous
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), RetinaXAIRequestHandler) as httpd:
        url = f"http://localhost:{PORT}/login.html"
        print(" RetinaXAI: Commercial Explainable AI Healthcare Suite")
        print(f" REST API & Web Server active at: {url}")
        print(" Demo Users:")
        print("   - ASHA Worker: asha@retinaxai.org / asha123")
        print("   - Doctor:      dr.varma@aiims.edu / doctor123")
        print("   - Patient:     patient@retinaxai.org / patient123")
        print("=" * 65)
        print(" Opening clinical portal in your web browser...")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()

if __name__ == "__main__":
    run_server()

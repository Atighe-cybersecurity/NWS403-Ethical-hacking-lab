
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

REQUEST_LOG = []

class LabHandler(BaseHTTPRequestHandler):

    def _is_rate_limited(self):
        now = time.time()
        REQUEST_LOG[:] = [t for t in REQUEST_LOG if now - t < 2.0]
        REQUEST_LOG.append(now)
        return len(REQUEST_LOG) > 8

    def do_HEAD(self):
        if self.path == "/internal/payroll_demo.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", "185")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self._is_rate_limited():
            print("[WARNING] High request rate detected! Safety control triggered.")
            self.send_response(429)
            self.end_headers()
            self.wfile.write(b"429 Too Many Requests - Slow down or pause testing.\n")
            return

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>HIMS Buea - NWS403 Lab Target (Synthetic)</h1>")

        elif self.path == "/robots.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"User-agent: *\nDisallow: /internal/\n")

        elif self.path == "/internal/payroll_demo.txt":
            print("[ALERT] Sensitive path accessed: /internal/payroll_demo.txt")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            data = (
                "# SYNTHETIC LAB DATA - STOP AFTER MINIMAL VERIFICATION\n"
                "EMP001, Jane Doe, 250000 XAF\n"
                "EMP002, John Smith, 310000 XAF\n"
                "EMP003, Alice Ngo, 280000 XAF\n"
            )
            self.wfile.write(data.encode())

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), LabHandler)
    print("NWS403 Lab Target running on http://127.0.0.1:8080 (Ctrl+C to stop)")
    server.serve_forever()

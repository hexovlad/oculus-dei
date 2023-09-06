import socket
import unittest
import http.server
import socketserver
import threading

from collector_modules.http_library.http_library import HttpRequest


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"GET received!")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"POST received!")

    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"DELETE received!")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Setting up the environment"""
        self.port = 49153
        self.endpoint = f"http://localhost:{self.port}"
        self.request_maker = HttpRequest(self.endpoint)  # Starting the HTTP library

        if not self.is_server_running("localhost", self.port):
            server_thread = threading.Thread(target=self.start_server)
            server_thread.daemon = True
            server_thread.start()

    @staticmethod
    def is_server_running(host, port) -> bool:
        """Checking if the server is running"""
        try:
            # Try to create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
            # If the connection succeeds, a server is running on the address
            return True
        except ConnectionRefusedError:
            # If the connection is refused, there is no server running on the address
            return False

    def start_server(self):
        """Starting the server"""
        with socketserver.TCPServer(
            ("localhost", self.port), MyHTTPRequestHandler
        ) as httpd:  # Creating the server to test the requests
            print(f"Serving at port {self.port}")
            httpd.serve_forever()

    def test_get_request(self):
        """Testing the GET request"""
        response = self.request_maker.do_get({})
        self.assertEqual(response.text, "GET received!")

    def test_post_request(self):
        """Testing the POST request"""
        response = self.request_maker.do_post({})
        self.assertEqual(response.text, "POST received!")

    def test_delete_request(self):
        """Testing the DELETE request"""
        response = self.request_maker.do_delete({})
        self.assertEqual(response.text, "DELETE received!")


if __name__ == "__main__":
    unittest.main()

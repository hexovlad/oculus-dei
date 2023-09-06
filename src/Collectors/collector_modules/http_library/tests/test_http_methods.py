import unittest
import http.server
import socketserver

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
        port = 8080
        endpoint = f"http://localhost:{port}"
        self.request_maker = HttpRequest(endpoint)  # Starting the HTTP library

        with socketserver.TCPServer(
            ("", port), MyHTTPRequestHandler
        ) as httpd:  # Creating the server to test the requests
            print(f"Serving at port {port}")
            httpd.serve_forever()

    def test_get_request(self):
        """Testing the GET request"""
        response = self.request_maker.do_get(None)
        self.assertEqual(response.text, "GET received!")

    def test_post_request(self):
        """Testing the POST request"""
        response = self.request_maker.do_post(None)
        self.assertEqual(response.text, "POST received!")

    def test_delete_request(self):
        """Testing the DELETE request"""
        response = self.request_maker.do_delete(None)
        self.assertEqual(response.text, "DELETE received!")


if __name__ == "__main__":
    unittest.main()

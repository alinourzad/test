#!/usr/bin/env python3

import http.server
import logging

class myHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        # print(self.method)
        # print(self.request.content)

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.warning("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        print(post_data.decode('utf-8'))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def main():
    print("starting on 80801....")
    http.server.HTTPServer(('', 8081), myHandler).serve_forever()

if __name__ == "__main__":
    main()
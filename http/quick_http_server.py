# Quick http server for local machine/intranet.
# Cancel after usage !!!

import http.server
import socketserver
import os

os.chdir('c:\\')
PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    
    httpd.serve_forever()

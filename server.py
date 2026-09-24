#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 3000

class CarouselHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/carousel-images':
            try:
                carousel_dir = Path(__file__).parent / 'img' / 'carousel'
                images = sorted([
                    f for f in os.listdir(carousel_dir)
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
                ])
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(images).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
                return
        
        super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), CarouselHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()

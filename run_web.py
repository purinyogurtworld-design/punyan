#!/usr/bin/env python3
"""Start this Web build on localhost; Python 3 only, no packages required."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import os,webbrowser
os.chdir(Path(__file__).resolve().parent)
class Handler(SimpleHTTPRequestHandler):
 extensions_map={**SimpleHTTPRequestHandler.extensions_map,'.wasm':'application/wasm','.pck':'application/octet-stream'}
 def end_headers(self):
  self.send_header('Cross-Origin-Opener-Policy','same-origin')
  self.send_header('Cross-Origin-Embedder-Policy','require-corp')
  self.send_header('Cache-Control','no-cache')
  super().end_headers()
server=ThreadingHTTPServer(('127.0.0.1',8080),Handler)
print('Punyan World: http://localhost:8080  (Ctrl+C to stop)')
webbrowser.open('http://localhost:8080')
try:server.serve_forever()
except KeyboardInterrupt:pass
finally:server.server_close()

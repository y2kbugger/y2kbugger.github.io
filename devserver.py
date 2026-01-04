#!/usr/bin/env python3
"""Dev server with browser live reload."""
import subprocess
import sys
from pathlib import Path
from livereload import Server

PORT = 8109
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'
THEME_PATH = 'themes/william-pelican'
SETTINGS = 'pelicanconf.py'

# Find pelican in the same venv as this script
PELICAN = str(Path(sys.executable).parent / 'pelican')

def build():
    subprocess.run([PELICAN, CONTENT_PATH, '-o', OUTPUT_PATH, '-s', SETTINGS], check=True)

if __name__ == '__main__':
    build()
    server = Server()
    server.watch(SETTINGS, build)
    server.watch(f'{CONTENT_PATH}/**/*.md', build)
    server.watch(f'{CONTENT_PATH}/**/*.rst', build)
    server.watch(f'{THEME_PATH}/templates/*.html', build)
    server.watch(f'{THEME_PATH}/static/**/*.css', build)
    server.watch(f'{THEME_PATH}/static/**/*.js', build)
    server.serve(port=PORT, root=OUTPUT_PATH)

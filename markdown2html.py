#!/usr/bin/python3
""" Converts Markdown to HTML """
import os
import sys


if len(sys.argv) < 3:
    sys.exit('Usage: ./markdown2html.py README.md README.html')
if not os.path.exists(sys.argv[1]):
    sys.exit(f'Missing {sys.argv[1]}')

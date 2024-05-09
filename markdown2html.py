#!/usr/bin/python3
""" Converts Markdown to HTML """
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    if not os.path.isfile(sys.argv[1]):
        sys.exit(f'Missing {sys.argv[1]}')

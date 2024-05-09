#!/usr/bin/python3
""" Converts Markdown to HTML """
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    if not os.path.isfile(sys.argv[1]):
        sys.exit(f'Missing {sys.argv[1]}')

    with open(sys.argv[1]) as md:
        with open(sys.argv[2], 'w') as html:
            for line in md:
                length = len(line)
                h = line.lstrip('#')
                h_lvl = length - len(h)

                if 1 <= h_lvl <= 6:
                    line = f'<h{h_lvl}>{h.strip()}</h{h_lvl}>\n'

                if length > 1:
                    html.write(line)

    exit(0)

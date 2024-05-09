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
            ul_start, ol_start, p_start = False, False, False
            for line in md:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                length = len(line)
                h = line.lstrip('#')
                h_lvl = length - len(h)
                ul = line.lstrip('-')
                ul_num = length - len(ul)
                ol = line.lstrip('*')
                ol_num = length - len(ol)

                if 1 <= h_lvl <= 6:
                    line = f'<h{h_lvl}>{h.strip()}</h{h_lvl}>\n'

                if ul_num:
                    if not ul_start:
                        html.write('<ul>\n')
                        ul_start = True
                    line = f'<li>{ul.strip()}</li>\n'
                if ul_start and not ul_num:
                    html.write('</ul>\n')
                    ul_start = False

                if ol_num:
                    if not ol_start:
                        html.write('<ol>\n')
                        ol_start = True
                    line = f'<li>{ol.strip()}</li>\n'
                if ol_start and not ol_num:
                    html.write('</ol>\n')
                    ol_start = False

                if not (h_lvl or ul_start or ol_start):
                    if not p_start and length > 1:
                        html.write('<p>\n')
                        p_start = True
                    elif length > 1:
                        html.write('<br />\n')
                    elif p_start:
                        html.write('</p>\n')
                        p_start = False

                if length > 1:
                    html.write(line)

            if ul_start:
                html.write('</ul>\n')
            if ol_start:
                html.write('</ol>\n')
            if p_start:
                html.write('</p>\n')
    exit(0)

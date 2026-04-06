# (c)AI[perplexity.ai+CoPilot] 
import argparse
import os
from urllib.parse import urlparse, parse_qs

parser = argparse.ArgumentParser(description='Convert plain-text URL list to clickable HTML.')
parser.add_argument('input_file', help='Path to input text file with one URL per line')
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

base_name = os.path.splitext(os.path.basename(args.input_file))[0]
output_file = f'{base_name}.html'

html = f"<!DOCTYPE html><html><head><title>Auto-generated from '{args.input_file}'</title>\n"
html += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
html += '<link rel="stylesheet" href="styles.css">\n'
html += '</head><body>\n'
html += '<table>\n'
html += '    <thead>\n'
html += '        <tr><th>On</th><th>Link</th></tr>\n'
html += '    </thead>\n'
html += '    <tbody>\n'
for url in urls:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    server = query.get('server', [''])[0]
    port = query.get('port', [''])[0]
    secret = query.get('secret', [''])[0]
    tg_link = f"tg://proxy?server={server}&port={port}&secret={secret}"
    html += f'        <tr><td><input type="checkbox" data-server="{server}"></td><td><a href="{tg_link}" target="_blank">{server}</a></td></tr>\n'
html += '    </tbody>\n'
html += '</table>\n'
html += '<script src="scripts.js"></script>\n'
html += '</body>\n'
html += '</html>'

with open(output_file, 'w') as f:
    f.write(html)

print(f'Generated {output_file} with {len(urls)} clickable links.')

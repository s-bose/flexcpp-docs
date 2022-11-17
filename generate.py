import os
import glob
from markdownify import markdownify as md

for file_path in glob.glob('manual/*.html'):
    print(file_path)
    fname = os.path.split(file_path)[-1]
    with open(file_path, 'r') as file:
        content = file.read()
    with open(f'docs/{fname.replace(".html", ".md")}', 'w') as file:
        file.write(md(content))

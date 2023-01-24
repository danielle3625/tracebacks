import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def syntax_highlight(code):
    return highlight(code, PythonLexer(), HtmlFormatter())


def make_output(filepaths, base_dir, output_dir):
    for src_path in filepaths:
        relpath = os.path.relpath(src_path, base_dir)
        outpath = os.path.join(output_dir, relpath)
        
        dest_path, _ = os.path.splitext(outpath)
        dest_path += ".html"
        
        parent_dir = os.path.dirname(dest_path)
        os.makedirs(parent_dir, exist_ok=True)
        
        with open(src_path, "r") as fin:
            contents = fin.read()
        
        syntax_highlight(contents)
        
        with open(dest_path, "w") as fout:
            fout.write(contents)

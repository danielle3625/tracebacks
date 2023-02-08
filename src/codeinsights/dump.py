import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from shutil import rmtree


def syntax_highlight(code):
    style = HtmlFormatter().get_style_defs('.highlight')
    result = f"<style>{style}</style>\n"
    result += highlight(code, PythonLexer(), HtmlFormatter())
    return result


def make_output(timing, base_dir, output_dir):

    rmtree(output_dir, ignore_errors=True)

    for src_path in timing.keys():
        relpath = os.path.relpath(src_path, base_dir)
        outpath = os.path.join(output_dir, relpath)
        
        dest_path, _ = os.path.splitext(outpath)
        dest_path += ".html"
        
        parent_dir = os.path.dirname(dest_path)
        os.makedirs(parent_dir, exist_ok=True)
        
        with open(src_path, "r") as fin:
            contents = fin.read()
        
        contents = syntax_highlight(contents)
        
        with open(dest_path, "w") as fout:
            fout.write(contents)

def split_html_lines(html):
    
    splat = html.split("\n")
    lines = {}
    for line in splat:
        lines[line] = syntax_highlight(html)
    return lines

    
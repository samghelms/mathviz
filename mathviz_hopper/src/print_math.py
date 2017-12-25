"""
Author: Sam Helms

Date: Nov 1

This module implements an interactive table that can display word embeddings.
It can also render mathematics using KaTeX.

"""
import shutil
import os
import json

from constants import print_math_template_path
from helpers import get_cur_path

def print_math(math_expression_lst, name = "math.html", out='html', formatter = lambda x: x):
    """
    Converts LaTeX math expressions into an html layout.
    Creates a html file in the directory where print_math is called
    by default. Displays math to jupyter notebook if "notebook" argument
    is specified.

    Args:
        math_expression_lst (list):  A list of LaTeX math (string) to be rendered by KaTeX
        out (string): {"html"|"notebook"}: HTML by default. Specifies output medium.
        formatter (function): function that cleans up the string for KaTeX. 
    Returns:
        A HTML file in the directory where this function is called, or displays
        HTML output in a notebook.
    """
    try: shutil.rmtree('viz')
    except: pass
    pth = get_cur_path()+print_math_template_path
    shutil.copytree(pth, 'viz')

    # clean_str = formatter(math_expression_lst)
    html_loc = None
    if out == "html":
        html_loc = pth+"standalone_index.html"

    if out == "notebook":  
        from IPython.display import display, HTML
        html_loc = pth+"notebook_index.html"

    html = open(html_loc).read()
    html = html.replace("__MATH_LIST__", json.dumps(math_expression_lst))

    if out == "notebook": 
        display(HTML(html))
    elif out == "html":
        with open(name, "w+") as out_f:
            out_f.write(html)


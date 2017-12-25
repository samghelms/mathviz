"""
Author: Sam Helms

Date: Nov 1

This module implements an interactive table that can display word embeddings.
It can also render mathematics using KaTeX.

"""
import shutil
import os
import sys
import threading
import re
from collections import MutableSequence

from helpers import find_free_port, construct_trie, get_cur_path
from bottle import Bottle, run
from server import Server


class MathList(MutableSequence):
    """
    This interface allows "pretty printing" of LaTeX text
    in list data structures.

    """

    def __init__(self, lst):
        """ 
        MathList Constructor

        todo:: share a port among lists. Or maybe close the server after serving from it?

        Args:
           lst (list):  A list of LaTeX math to be rendered by KaTeX

        Returns:
           A math list object

        Usage example
        >>> lst = ["\int x = y", "x + 6"]
        >>> MathList(lst)
        ... see nicely formatted math.

        """

        list.__init__(self, lst)
        self.server = None
        self.port = find_free_port()
        self.html_path = get_cur_path()+'/data/math_list/index.html'

    def __del__(self):
        """
        Class destructor

        """
        del self.server

    def shutdown(self):
        """
        Shuts the server down

        """

        del self.server

    def serve_table(self, public = False, port = None):
        """ 
        "prints" a javascript visualization that can be run in the browser locally
        (and initializes listening on a port to serve data to the viz.

        Args:
           public (boolean): indicates whether or not the table should be
                             visible on a public address.
           port (int): the port to serve the table on

        Returns:
           A webpage

        Usage example
        ... initialize index
        >>> t = Table(ind)
        >>> t.serve_table(public = true)
        ... starts serving the table to a public address

        """

        self._listen()


    def print_ipython(self):
        """ 
        Renders the javascript table to a jupyter/ipython notebook cell

        Usage example:
        
        >>> t = Table(ind)
        >>> t.print_ipython()
        ... renders the table to notebook cell

        """
        pass
        # from IPython.display import display, HTML
        # self._listen()
        # try: shutil.rmtree('viz')
        # except: None

        # shutil.copytree(self.html_path, 'viz')
        # pth = "viz/index.html"
        # html = open(pth).read()
        # html = html.replace("__SERVER_DATA__", '"http://localhost:'+str(self.port)+'"')
        # display(HTML(html))


# if __name__ == '__main__':
#     import pandas as pd
#     import numpy as np
#     from notebooks.utils import read_file, tokenize_latex
    # df = read_file("notebooks/data/1601/*")
    # df["processed"] = df["text"].apply(lambda x: tokenize_latex(x))
    # t = Table([], lambda x: True, [])
    # t.run_server()

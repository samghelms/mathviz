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

from helpers import find_free_port, construct_trie, get_cur_path
from bottle import Bottle, run
from server import Server


class Table:
    """
    This class creates a server and a sets up an interactive 
    javascript table for inspecting word embeddings.

    """

    def __init__(self, index, port = 8081):
        """ Table Constructor

        todo::make sure this is memory efficient

        Args:
           Index (Index):  An Index object with a valid .query method 
                           and a .columns attribute.

        Returns:
           A table object

        Usage example

        >>> Table(ind)

        """

        self.index = index
        self.server = None
        self.port = port if port else find_free_port()
        self.settings = index.columns
        self.docs = index.docs
        self._create_settings()
        self.html_path = get_cur_path()+'/data/table/'

        # set to true if we want to delete the viz directory
        self.cleanup_flag = False

    def __del__(self):
        """
        Class destructor

        """
        del self.server

        if self.cleanup_flag:
            shutil.rmtree('viz')

    def shutdown(self):
        """
        Shuts the server down

        """

        del self.server

    def _create_settings(self):
        """ 
        Creates the settings object that will be sent 
        to the frontend vizualization

        """

        self.settings = {
            "columns": [{"Header": s, "accessor": s} for s in self.settings],
            "port": self.port,
            "docs": construct_trie(self.docs)
        }

    def print_html(self):
        '''
        "prints" a javascript visualization that can be run in the browser
        (or TODO: a jupyter notebook cell) and initializes listening on a
        port to serve data to the viz.

        '''

        self._listen()

    def run_server(self):
        """ 
        Runs a server to handle queries to the index without creating the 
        javascript table.

        """
        app = build_app()
        run(app, host='localhost', port=self.port)

    def print_ipython(self):
        """ 
        Renders the javascript table to a jupyter/ipython notebook cell

        Usage example:
        
        >>> t = Table(ind)
        >>> t.print_ipython()
        ... renders the table to notebook cell

        """
        from IPython.display import display, HTML
        self._listen()
        try: shutil.rmtree('viz')
        except: None

        shutil.copytree(self.html_path, 'viz')
        pth = "viz/index.html"
        html = open(pth).read()
        display(HTML(html))

    def _listen(self):
        """
        Initializing listening on a socket to serve data to the javascript
        table.

        """
        self.server = Server(self)

    def _print_html(self):
        """
        Internal method to call the javascript/html table.
        
        """
        cur_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        shutil.copytree(cur_path+'webpage/template/', '')

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from notebooks.utils import read_file, tokenize_latex
    df = read_file("notebooks/data/1601/*")
    df["processed"] = df["text"].apply(lambda x: tokenize_latex(x))


    t = Table([], lambda x: True, [])
    t.run_server()

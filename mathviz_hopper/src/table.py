'''
Author: Sam Helms
Date: Nov 1

This class creates an html table that can display math
equations.

'''
import shutil
import os
import sys
import threading
import re

from helpers import find_free_port, construct_trie, get_cur_path
from bottle import Bottle, run
from server import Server


class Table:
    """This function does something.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> print public_fn_with_googley_docstring(name='foo', state=None)
    0

    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

    """
    '''
    @ param index: a lambda function that takes some input and returns k nearest neighbors
    @ param converter: converts values to the format needed by the index 
      (for example, it would convert a word to a vector)
    @ param docs: a vector (list) of documents mapping to the index parameters returned by
      the index function
    @ writes a visualization to disk
    '''
    def __init__(self, index, port = 8081):
        '''
        Constructor. Creates indices if passed data
        @ param 
            index: gensim index object (TODO: implement this for dataframes)
            data: any data you want to 
        '''
        # TODO: make this memory efficient
        self.index = index
        self.server = None
        self.port = port if port else find_free_port()
        self.settings = index.columns
        self.docs = index.docs
        self._create_settings()
        self.html_path = get_cur_path()+'/html/build/'

        # set to true if we want to delete the viz directory
        self.cleanup_flag = False

        # path for the jupyter notebook TODO: change this to work with a package
        # self.html_path = "/mathviz_hopper/src/html/build"

    def __del__(self):
        del self.server

        if self.cleanup_flag:
            shutil.rmtree('viz')

    def shutdown(self):
        del self.server

    def _create_settings(self):
        '''
        TODO: add this as another interface
        Creates an index (can be used to initialize the index if not
        passed in the consturctor)
        @ param 
            index: gensim index object (TODO: implement this for dataframes)
            words: list of strings representing words in the vocabulary
        '''
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
        # _print_html()
        self._listen()

    def run_server(self):
        '''
        "prints" a javascript visualization that can be run in the browser
        (or TODO: a jupyter notebook cell) and initializes listening on a
        port to serve data to the viz.
        '''
        # _print_html()
        # handler = TableRequestHandlerFactory(self.index, self.converter, self.docs, self.settings)
        # self.server = HTTPServer(('', self.port), handler)
        # self.server.serve_forever()
        app = build_app()
        run(app, host='localhost', port=self.port)

    def print_ipython(self):
        '''
        "prints" a javascript visualization to a jupyter/ipython notebook cell
        And initializes listening on a port to serve data to the viz.
        '''
        # _print_html()
        from IPython.display import display, HTML
        self._listen()
        try: shutil.rmtree('viz')
        except: None

        # TODO: assign this path intelligently
        shutil.copytree(self.html_path, 'viz')
        pth = "viz/index.html"
        html = open(pth).read()
        display(HTML(html))

    def _query(self, q):
        '''
        Wraps gensim's query functionality. 
        @ param q: a query string
        @ returns list of nearest neighbor strings and their distances
        '''

    def _listen(self):
        '''
        Initializing listening on a socket to serve data to the javascript
        table.
        '''
        # TODO: write a method to deal with socket conflicts
        self.server = Server(self)

        print 'listening'

    def _print_html(self):
        '''
        Creates an interactive table for viewing in the browser.
        '''
        cur_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        shutil.copytree(cur_path+'webpage/template/', '')

    def bundle(self):
        '''
        bundles the table and the model to a folder of javascript, html,
        and css files that can be shared via email, github pages, or some
        other service.
        '''

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from notebooks.utils import read_file, tokenize_latex
    df = read_file("notebooks/data/1601/*")
    df["processed"] = df["text"].apply(lambda x: tokenize_latex(x))


    t = Table([], lambda x: True, [])
    t.run_server()

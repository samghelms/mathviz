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

from IPython.display import display, HTML

from helpers import find_free_port, construct_trie, get_cur_path
from bottle import Bottle, run
from server import Server


class Table:
    '''
    @ param index: a lambda function that takes some input and returns k nearest neighbors
    @ param converter: converts values to the format needed by the index 
      (for example, it would convert a word to a vector)
    @ param docs: a vector (list) of documents mapping to the index parameters returned by
      the index function
    @ writes a visualization to disk
    '''
    def __init__(self, index, converter, docs, port = 8081):
        '''
        Constructor. Creates indices if passed data
        @ param 
            index: gensim index object (TODO: implement this for dataframes)
            words: list of strings representing words in the vocabulary
        '''
        # TODO: make this memory efficient
        self.index = index
        self.converter = converter
        self.docs = docs
        self.server = None
        self.port = port if port else find_free_port()
        print self.port
        self.settings = None
        self._create_settings()
        self.html_path = '/Users/sam/Documents/fall17/mathviz/mathviz_hopper/webpage/mathviz-js-components/build/'

        # set to true if we want to delete the viz directory
        self.cleanup_flag = False

        # path for the jupyter notebook TODO: change this to work with a package
        # self.html_path = "/mathviz_hopper/src/html/build"

    def __del__(self):
        self.server.shutdown()

        if self.cleanup_flag:
            shutil.rmtree('viz')

    def shutdown(self):
        self.server.shutdown()


    def _create_settings(self):
        '''
        TODO: add this as another interface
        Creates an index (can be used to initialize the index if not
        passed in the consturctor)
        @ param 
            index: gensim index object (TODO: implement this for dataframes)
            words: list of strings representing words in the vocabulary
        '''
        # {
        #                 "Header": "Word",
        #                 "accessor": "word"
        #             },
        #             {
        #                 "Header": "Similarity",
        #                 "accessor": "sim"
        #             }

        self.settings = {
            "columns": [{"Header": "Word","accessor": "word"}, {"Header": "Similarity","accessor": "sim"} ],
            "port": self.port,
            "docs": construct_trie(self.docs)
        }


    def _create_index(self, index, converter):
        '''
        TODO: add this as another interface
        Creates an index (can be used to initialize the index if not
        passed in the consturctor)
        @ param 
            index: gensim index object (TODO: implement this for dataframes)
            words: list of strings representing words in the vocabulary
        '''
        self.index = index
        self.converter = converter

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
        self._listen()
        try: shutil.rmtree('viz')
        except: None

        # TODO: assign this path intelligently
        base_path = get_cur_path()
        print base_path
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
    t = Table([], lambda x: True, [])
    t.run_server()

'''
Author: Sam Helms
Date: Nov 8

Playing around with ipython settings

'''
from IPython.display import display, HTML
from helpers import get_cur_path
import os
import re
import shutil

HTML_PATH = "/viz"

class Test:
    def __init__(self):
        print ("creating test instance")
        self.cur_path = os.path.dirname(os.path.abspath(__file__))
    def __del__(self):
        shutil.rmtree('viz')

    def print_html(self):
        '''
        "prints" a javascript visualization that can be run in the browser
        (or TODO: a jupyter notebook cell) and initializes listening on a
        port to serve data to the viz.
        '''
        # _print_html()
        # display = open("html/build/index.html").read()
        # print (display)
        try: shutil.rmtree('viz')
        except: None
        # shutil.copytree(self.cur_path+'/html/build/', 'viz')
        shutil.copytree('/Users/sam/Documents/fall17/mathviz/mathviz_hopper/webpage/mathviz-js-components/build/', 'viz')

        # with open("viz/settings.json")
        pth = "viz/index.html"
        html = open(pth).read()
        # # # html = re.sub("", "", html)
        # # # "./katex.css"
        # html = re.sub(r'(href=\"\.)', r'\1'+HTML_PATH, html)
        # html = re.sub(r'(src=\"\.)', r'\1'+HTML_PATH, html)

        # # "/Users/sam/Documents/fall17/mathviz/mathviz_hopper/webpage/mathviz-js-components/build"

        display(HTML(html))
        

    # def print(self):
    #   print("test")
    #   # return HTML("<div> hello world </div>")


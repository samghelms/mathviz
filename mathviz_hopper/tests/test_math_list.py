from mathviz_hopper.src.print_math import print_math
import os 

class TestPrintMath:
 
    def __init__(self):
        self.lst = None
 
    def test_print_html(self):
        lst = ["c = \\pm\\sqrt{a^2 + b^2}", "c = x"]
        print_math(lst, name = "math_test.html")
        with open("math_test.html", "r") as f:
            print f.read()
            assert False
        os.remove("math_test.html")
        
 
    # def test_query(self):
    #     print 'test_query()'
    #     print self.index.query("\\frac")
    #     assert "sum_{g=1}^" in json.dumps(self.index.query("\\frac"))
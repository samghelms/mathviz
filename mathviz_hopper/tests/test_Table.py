from mathviz_hopper.src.table import Table
from setup_test_data import Data

class TestTable:
 
    def __init__(self):
    	self.data = Data()
        self.table = None
 
    def test_init(self):
        print 'test_init()'
        # t = Table()
        assert 
 
    def test_strings_b_2(self):
        print 'test_strings_b_2()  <============================ actual test code'
        assert multiply('b',2) == 'bb'
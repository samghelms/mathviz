from mathviz_hopper.src.table import Table
from mathviz_hopper.src.indices import GensimMathIndex
from setup_test_data import Data

class TestTable:
 	"""
 	Unit tests for the table
 	"""
    def __init__(self):
    	self.data = Data()
    	self.index = GensimMathIndex(self.data.index, self.data.docs, self.data.dictionary)
        self.table = Table(self.index)
 
    def test_init(self):
        print 'test_init()'
        assert self.table.index
 
    def test_(self):
        print 'test_()'
        
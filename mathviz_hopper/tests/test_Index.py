from mathviz_hopper.src.indices import GensimMathIndex
from setup_test_data import Data

class TestGensimMathIndex:
 
    def __init__(self):
    	self.data = Data()
        self.index = GensimMathIndex(self.data.index, self.data.docs, self.data.dictionary)
 
    def test_init(self):
        print 'test_init()'
        assert self.index.columns == ["neighbor", "similarity_score"]
 
    def test_query(self):
        print 'test_query()'
        print index.query("\\frac")
        assert index.query("\\frac")
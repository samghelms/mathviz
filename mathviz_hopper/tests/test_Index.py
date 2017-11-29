from mathviz_hopper.src.indices import GensimMathIndex
from setup_test_data import Data
import json

class TestGensimMathIndex:
 
    def __init__(self):
    	self.data = Data()
        self.index = GensimMathIndex(self.data.index, self.data.docs, self.data.dictionary)
 
    def test_init(self):
        print 'test_init()'
        assert self.index.columns == ["neighbor", "similarity_score"]
 
    def test_query(self):
        print 'test_query()'
        print self.index.query("\\frac")
        assert "sum_{g=1}^" in json.dumps(self.index.query("\\frac"))
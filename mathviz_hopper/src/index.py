'''
Author: Sam Helms
Date: Nov 1

This class creates an index that can be served with the table class

'''

class Index:
    '''
    
    '''
    def __init__(self, lookup_function, columns, docs):
        '''
        Constructor.
        @ param 
            lookup_function: a function that can take a query of some sort
                             and return values based on it
        '''
        # TODO: make this memory efficient
        self.lookup_function = lookup_function
        self.columns = columns
        self.server = None
        self.docs = docs

    def query(self, query):
        return self.lookup_function(query)

    def __del__(self):
        None


class GensimIndex(Index):

    def __init__(self, index, docs, dictionary, transformer = None):
        self.index = index
        self.dictionary = dictionary
        self.docs = docs
        self.transformer = transformer

        lookup_function = _generate_lookup_function(index, docs)
        Index.__init__(self, lookup_function)


    def _convert_query(query):
        transformed = self.transformer(query) if self.transformer else query
        query = self.dictionary.doc2bow(transformed)
        sims = self.index[query]

        neighbors = sorted(sims, key=lambda item: -item[1])
        neighbors = {"neighbors":[{"neighbor": self.docs[n[0]], "similarity_score": float(n[1])} for n in neighbors]} if neighbors else {"neighbors": []}
        return neighbors

    def _generate_lookup_function(index, docs):
        return lambda x: _convert_query(x)


class NumpyIndex(Index):

    def __init__(self, index, docs):
        Index.__init__(self, lookup_function)

    def hatesDogs(self):
        return self.hates_dogs


if __name__ == '__main__':
    t = Table([], lambda x: True, [])
    t.run_server()

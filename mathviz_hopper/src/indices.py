'''
Author: Sam Helms
Date: Nov 1

This class creates an index that can be served with the table class

'''

class Index:
    '''
    
    '''
    def __init__(self, lookup_function, columns):
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

class GensimMathIndex(Index):
    """
    An index that allows querying gensim-based vector space models.
    You can use this as an example for how to create your own index.
    """
    def __init__(self, index, docs, dictionary):
        """ GensimMathIndex Constructor

        Args:
            index (gensim.similarities.docsim.Similarity):  
                A gensim index object
            docs (list):
                A list of the strings you are indexing, with the index corresponding
                to the gensim index.
            dictionary (gensim.corpora.dictionary.Dictionary):
                The same dictionary used to create the gensim index

        Returns:
           A table object

        Usage example:

        >>> gmi = GensimMathIndex(index, clean_docs, dictionary, tokenize_latex, ["neighbor", "similarity_score"])
        >>> q.query("\\frac")
        >>> {'neighbors': [{'neighbor': {'data': u'\\begin{aligned}\\min_{L,S}\\sum_{m=1}^{M}\\sum_{i=1}^{N_{m}}&\\frac{1}{2}[max(0,1-Y_{m}^{i}(Ls^{m})^{T}X_{m}^{i})]^{2}\\\\&+\\gamma\\|L\\|_{1}+\\lambda\\|L\\|^{2}_{F}\\\\\\end{aligned}',
            'fmt': 'math'},
            'similarity_score': {'data': 0.07059364020824432}},
            ...

        Passing to a Table:
        ...
        >>> t = Table(gmi)

        """
        self.index = index
        self.docs = docs
        self.dictionary = dictionary
        self.columns = ["neighbor", "similarity_score"]

        lookup_function = self._query
        Index.__init__(self, lookup_function, self.columns)

    def _tokenize_latex(exp):
        """
        Internal method to tokenize latex
        """
        tokens = []
        prevexp = ""
        while exp:
            t, exp = get_next_token(exp)
            if t.strip() != "":
                tokens.append(t)
            if prevexp == exp:
                break
            prevexp = exp
        return tokens

    def _convert_query(self, query):
        """
        Convert query into an indexable string.
        """
        query = self.dictionary.doc2bow(self._tokenize_latex(query))
        sims = self.index[query]
        neighbors = sorted(sims, key=lambda item: -item[1])
        neighbors = {"neighbors":[{self.columns[0]: {"data": self.docs[n[0]], "fmt": "math"}, self.columns[1]: {"data": float(n[1])}} for n in neighbors]} if neighbors else {"neighbors": []}
        return neighbors

    def _query(self, q):
        """
        Internal query method to pass to parent interface
        """
        return self._convert_query(q)


class NumpyIndex(Index):

    def __init__(self, index, docs):
        Index.__init__(self, lookup_function)

    def hatesDogs(self):
        return self.hates_dogs


if __name__ == '__main__':
    t = Table([], lambda x: True, [])
    t.run_server()

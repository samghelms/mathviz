"""
Collection of utilities for testing
"""
import pandas as pd
import numpy as np
from gensim import corpora
import re
from gensim import corpora, models, similarities, matutils
from gensim import similarities
import glob
import os

def read_file(file):
    df_li = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for f in glob.glob(dir_path+"/"+file):
        try:
            df_li.append(pd.read_json(f))
        except:
            print "error with: " + f
            
    return pd.concat(df_li).reset_index(0)

def get_next_token(string):
    '''
    "eats" up the string until it hits an ending character to get valid leaf expressions.
    For example, given \\Phi_{z}(L) = \\sum_{i=1}^{N} \\frac{1}{C_{i} \\times V_{\\rm max, i}},
    this function would pull out \\Phi, stopping at _
    @ string: str
    returns a tuple of (expression [ex: \\Phi], remaining_chars [ex: _{z}(L) = \\sum_{i=1}^{N}...])
    '''
    STOP_CHARS = "_ {}^ \n ,()="
    UNARY_CHARS = "^_"
    # ^ and _ are valid leaf expressions--just ones that should be handled on their own
    if string[0] in STOP_CHARS:
        return string[0], string[1:]
    
    expression = []
    for i, c in enumerate(string):
        if c in STOP_CHARS:
            break
        else:
            expression.append(c)
    
    return "".join(expression), string[i:]

def tokenize_latex(exp):
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

def get_processed_data():

    df = read_file("data/math.json")
    df["processed"] = df["text"].apply(lambda x: tokenize_latex(x))
    return df

def get_corpus_dict(df):
    equations = df["processed"].tolist()
    dictionary = corpora.Dictionary(equations)

    corpus = [dictionary.doc2bow(eq) for eq in equations]
    # our vector space model
    return corpus, dictionary

def get_tfidf_corpus(corpus):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return corpus_tfidf

def get_index(corpus_tfidf, dictionary):
    index = similarities.MatrixSimilarity(corpus_tfidf)
    return index

def get_docs(df):
    docs = ["".join(eq) for eq in df["processed"].tolist()]
    return docs

def clean_exp(exp):
    exp = re.sub("\\\\begin{equation[^}]*}","" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\end{equation[^}]*}","" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\begin{split[^}]*}","\\\\begin{aligned}" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\end{split[^}]*}","\\\\end{aligned}" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\begin{gather[^}]*}","\\\\begin{aligned}" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\end{gather[^}]*}","\\\\end{aligned}" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\begin{align[^}]*}","\\\\begin{aligned}" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\end{align[^}]*}","\\\\end{aligned}" ,exp, flags=re.IGNORECASE)
    exp = re.sub("\\\\label{[^}]*}","" ,exp , flags=re.IGNORECASE)
    exp = re.sub("\\\\n", "",exp, flags=re.IGNORECASE)
    exp = re.sub("\\$", "",exp , flags=re.IGNORECASE)
    return exp

def get_clean_docs(docs):
    clean_docs = map(clean_exp, docs)

class Data:
    def __init__(self):
        self.df = get_processed_data()
        self.corpus, self.dictionary = get_corpus_dict(self.df)
        self.corpus_tfidf = get_tfidf_corpus(self.corpus)
        self.index = get_index(self.corpus_tfidf, self.dictionary)
        self.docs = get_docs(self.df)
        self.clean_docs = get_clean_docs(self.docs)

if __name__ == '__main__':
    d = Data()
    print d.corpus
    print d.docs
import pandas as pd
import glob

def read_file(file):
    df_li = []
    for f in glob.glob(file):
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
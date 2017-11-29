import os
import sys
import socket 

def get_cur_path():
	return os.path.dirname(os.path.abspath(__file__))

def insert(st, trie):
    i = 0
    for s in st:
        if s not in trie.keys(): 
            trie[s] = {}
        if i == 20:
            break
        trie = trie[s]
        i+=1
        
    if i == 20: 
        trie[st[i:]] = {}
        trie = trie[st[i:]]
    trie["full_word"] = 1
        
    
def construct_trie(list_of_str):
    trie = {}
    for st in list_of_str:
        insert(st, trie)
    return trie
    
# https://stackoverflow.com/questions/2838244/get-open-tcp-port-in-python
def find_free_port():
    s = socket.socket()
    s.bind(('', 0))            # Bind to a free port provided by the host.
    return s.getsockname()[1]  # Return the port number assigned.
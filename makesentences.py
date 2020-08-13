import random

class Story:
    def __init__(self, art, adj, nouns, verb, pos, midart, plc):
        self.art = art
        self.adj = adj
        self.nouns = nouns
        self.verb = verb
        self.pos = pos
        self.midart = midart
        self.plc = plc
        
a = ['The', 'A']
b = ['blue', 'red', 'big']
c = ['cat', 'dog', 'snake']
d = ['runs', 'eats', 'drinks']
e = ['on', 'at', 'from']
f = ['the', 'a']
g = ['car', 'floor', 'table']

sent = Story(random.choice(a), random.choice(b), random.choice(c), random.choice(d), random.choice(e), random.choice(f), random.choice(g))
print(sent.art, sent.adj, sent.nouns, sent.verb, sent.pos, sent.midart, sent.plc)

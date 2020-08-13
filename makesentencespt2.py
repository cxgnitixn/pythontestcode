import random

adjectives = ['big', 'bad', 'bold', 'pretty','small', 'red', 'yellow', 'blue']
adjectives.append('beautiful')

articles = ['The', 'A']

nouns = ['dog','cat','fish']

verbs = ['runs', 'swims', 'eats']

print(random.choice(articles), random.choice(adjectives), random.choice(nouns), random.choice(verbs))
        

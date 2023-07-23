"""
from collections import Counter

votes = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie',
         'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']

vote_count = Counter(votes)

max_votes = max(vote_count.values())

lst= [i for i in vote_count.keys() if vote_count[i]==max_votes]
print(sorted(lst)[0])
"""
#method 2
from collections import Counter
def winner(inp1):
    votes = Counter(inp1)
    dict= {}
    for value in votes.values():
        dict[value]=[]
    for (key,value) in votes.items():
        dict[value].append(key)
    maxvote = sorted(dict.keys(),reverse=True)[0]
    if(len(dict[maxvote])>1):
        print(sorted(dict[maxvote])[0])
    else:
        print(dict[maxvote][0])
inp1 = ['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john','johnny']
winner(inp1)

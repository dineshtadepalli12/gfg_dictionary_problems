"""
#brute force method
st1 = "engineers rock"
pattern = "rs"
li = []
for i in pattern:
    li.append(i)
l1_indexing = []
l1_indexing.extend([j for i in li for j,k in enumerate(st1) if i ==k])
print(l1_indexing)
if(l1_indexing==sorted(l1_indexing)):
    print("In order and TRUE")
else:
    print("Not In order and FALSE")
"""
# Function to check if string follows order of
# characters defined by a pattern

from collections import OrderedDict
def checkorder(input,pattern):
    dict = OrderedDict.fromkeys(input)
    ptrlen = 0
    for key,value in dict.items():
        if (key==pattern[ptrlen]):
            ptrlen+=1
        if(ptrlen==len(pattern)):
            return 'True'
    return 'False'


if __name__ == "__main__":
    input = "engineers rock"
    pattern = "ei"
    print(checkorder(input,pattern))

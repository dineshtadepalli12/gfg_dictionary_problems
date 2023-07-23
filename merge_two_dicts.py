# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return (dict2.update(dict1))

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This returns None
print(Merge(dict1, dict2))
# changes made in dict2
print(dict2)
#or

def merge2(dic1,dic2):
    for i in dic2.keys():
        dic1[i] = dic2[i]
    return dic1
dic1 = {'a':4,'b':10}
dic2 = {'c':5,'d':12}
merge2(dic1,dic2)
print(dic1)
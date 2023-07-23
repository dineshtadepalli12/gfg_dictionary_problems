test_dict = {'month' : [1, 2, 3],'name' : ['Jan', 'Feb', 'March']}

x = list(test_dict.values())
print(x)
a = x[0]
b = x[1]
d = dict()
for i in range(len(a)):
    d[a[i]]=b[i]
print(d)

#or second method

from itertools import product

res = dict(zip(test_dict['month'],test_dict['name']))
print(res)
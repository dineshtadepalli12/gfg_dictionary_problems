"""
    first_dict = {'stock1': [1,2,3],'stock2':[4,5,6],'stock3':[7,8,9]}
    print(first_dict.keys())
    #fth = {'stock4': 25}
    first_dict.update({'stock4':[10,11,12]})
    print(first_dict)
"""
"""
first_dict = {'stock1': [1, 2, 3], 'stock2': [4, 5, 6], 'stock3': [7, 8, 9]}
popped_item = first_dict.pop('stock3')
print(popped_item)
print(first_dict)
print(first_dict.get('stock1'))
"""
"""
#method 1
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : ",test_dict)

#res = list(sorted({ele for val in test_dict.values() for ele in val}))

res1 = (sorted({val for ele in test_dict.values() for val in ele}))
print(res1)
print(type(res1))
"""

#method2
from itertools import chain

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
a = []
for val in test_dict.values():
    for i in val:
        if i not in a:
            a.append(i)
print(a)

#or

res = list({ele for val in test_dict.values() for ele in val})
print(res)




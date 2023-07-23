test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
res_list = list(test_dict.keys())+list(test_dict.values())
print(res_list)

#method 2 using chain
from itertools import chain
test_dict2 = {"Gfg" : 1, "is" :  3, "Best" : 2}
res_list2 = list(chain(test_dict2.keys(),test_dict2.values()))
print(res_list2)

#method 3 using extend

test_dict3 = {"Gfg": 1, "is": 3, "Best": 2}
print(f"the original dictionary is {str(test_dict3)}")
a = list(test_dict3.keys())
b = list(test_dict3.values())
a.extend(b)
print("The elements after inserting in order is:",a)

test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4],
             'Best':[21,14]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))
print(sorted(test_dict))
res = {}
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
print(res)

#method 2
"""
test_dict2 = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4],
             'Best':[21,14]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict2))

res2 = {key:sorted(test_dict2[key]) for key in sorted(test_dict2)}
print(res2)

"""
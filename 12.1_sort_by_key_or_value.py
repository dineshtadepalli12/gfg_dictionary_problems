
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

kes = list(myDict.keys())
kes.sort()
sorted_dict = {i:myDict[i] for i in kes}
print(f"The sorted dictionary is {sorted_dict}")


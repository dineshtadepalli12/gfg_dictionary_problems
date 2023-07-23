#Sort Dictionary By Value in Python

from collections import OrderedDict
import numpy as np

dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

keys = list(dict.keys())
values = list(dict.values())

sorted_value_index = np.argsort(values)

sorted_result = {keys[i]:values[i] for i in sorted_value_index}
print(sorted_result)
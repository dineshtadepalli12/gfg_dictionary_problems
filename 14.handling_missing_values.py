
country_code = {'India' : '0091',
                'Australia' : '0025',
               'Nepal' : '00977'}
print(country_code.get("Japan",'Not found'))

#method 2 using setting default value
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

country_code.setdefault('Japan',"Not found")
print(country_code['Japan'])

#method 3 using default dict

import collections
defd = collections.defaultdict(lambda : 'key not found')
defd['a'] = 1
defd['b'] = 2
defd['c']
print(defd['a'])
print(defd['c'])
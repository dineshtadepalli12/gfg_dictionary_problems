list1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(list1,key=lambda i:i['age']))
print(sorted(list1,key=lambda i :(i['age'],i['name']),reverse=True))

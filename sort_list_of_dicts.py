from operator import itemgetter

# Initializing list of dictionaries
list1 = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]

print("Using only age: ")
print(sorted(list1,key=itemgetter('age')))
print(sorted(list1,key=itemgetter('age','name')))
print(sorted(list1,key=itemgetter('age','name'),reverse=True))
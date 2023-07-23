dic = {'a': 100, 'b': 200, 'c': 300}
sum1=0
for value in dic.values():
    sum1+=value
print(sum1)

your_dict = {'a': 100, 'b':200, 'c':300}
a = []
for ele in your_dict:
    a.append(your_dict[ele])
print(sum(a))
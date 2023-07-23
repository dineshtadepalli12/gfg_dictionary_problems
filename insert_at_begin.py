from collections import OrderedDict

original_dict = {'nikhil':2,'akshat':1,}
inor = OrderedDict(original_dict)
inor.update({'manjeet':'3'})
inor.move_to_end('manjeet',last=False)
print(inor)
from collections import OrderedDict
def kthrepeating(input,k):
    dict = OrderedDict.fromkeys(input,0)
    print(dict)
    for ch in input:
        dict[ch]=dict[ch]+1
    nonrepeat = [key for key,value in dict.items() if value==1]
    if len(nonrepeat)<k:
        return (f"the non repeating characters are less than {k}")
    else:
        return nonrepeat[k-1]
if __name__=="__main__":
    input = "geeksforgeeks"
    k=3
    print(kthrepeating(input,3))
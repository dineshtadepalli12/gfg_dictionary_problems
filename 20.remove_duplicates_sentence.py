from collections import Counter
"""
def removedups(inp):
    a = x.split(" ")
    nl = []
    for i in a:
      if i not in nl:
         nl.append(i)
    print(" ".join(nl))
if __name__=="__main__":
    x = "Python is great and Java is also great"
    removedups(x)
"""

x = "Python is great and Java is also great"
a = x.split(" ")
cd = Counter(a)
s = " ".join(cd.keys())
print(s)
def allanagram(input):
    dict = {}
    for strval in input:
        key = "".join(sorted(strval))
        if key in dict.keys():
            dict[key].append(strval)
        else:
            dict[key]= []
            dict[key].append(strval)
    output=""
    for k,v in dict.items():
        output+= " ".join(v)+" "
    return output
if __name__ == "__main__":
    input=['cat', 'dog', 'tac', 'god', 'act']
    print (allanagram(input))
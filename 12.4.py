#sorting the keys and values in alphabetical order using the key

def dict():
    # Declaring the hash function
    key_value = {}
    # Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print(sorted(key_value.keys()))
    for i in sorted(key_value.keys()):
        print((i,key_value[i]), end=" ")
def main():
    dict()

if __name__=="__main__":
    main()
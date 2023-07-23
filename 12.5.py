#sorting a dictionary by its value

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

    print(sorted(key_value.items(),key=lambda kv:(kv[1],kv[0])))

def main():
    dict()

if __name__ == "__main__":
    main()
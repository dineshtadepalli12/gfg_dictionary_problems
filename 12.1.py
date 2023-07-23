#displaying the sorted keys in sorted order

def dict():
    key_value = {}
    key_value[2] = '56'
    key_value[1] = '2'
    key_value[4] = '12'
    key_value[5] = '24'
    key_value[6] = '18'
    key_value[3] = '323'

    res = list(i for i in sorted(key_value))
    print(res)

def main():
    dict()
if __name__=="__main__":
    main()
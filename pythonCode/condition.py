def main():
    a = int(input("input Number : "))
    # < > <= >= not and or 
    if a > 10:
        print(" a is bigger than 10")
    elif a > 5:
        print(" a is bigger than 5")
    elif a > 0:
        print(" a is bigger than 0")
    else:
        print(" a is less than 0")

    # and True True -> True
    #     False True -> False
    #     True  False -> False
    #     False False -> Fasle

    # or True True -> True
    #     False True -> True
    #     True  False -> True
    #     False False -> Fasle
    
    # not True -> False
    #     False -> True

    print('end of program')

if __name__ == '__main__':
    main()

def main():
    testvar = 3.141593
    print(testvar)
    testvar = "hello ros2"
    print(testvar)
    # indexing
    print(testvar[0]) # h
    print(testvar[3]) # l
    # slicing
    print(testvar[0:3]) # hel
    print(testvar[0:3:2]) # hl
    print(len(testvar)) # 10
    print(testvar.__len__()) # 10


if __name__ == '__main__':
    main()

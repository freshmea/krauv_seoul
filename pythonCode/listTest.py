from strMethod import A

def main():
    # define
    a = A('choi', 80)
    li1 = list()
    li1 = []
    li1 =[1,2,3,4,5,6,7, 'abc', 'def', a]

    # indexing
    print(li1[8])
    li1[-1].a()
    # slicing
    print(li1[3:8])
    # iterable
    for ele in li1:
        print(ele , end=' ')
    print()


if __name__ == '__main__':
    main()

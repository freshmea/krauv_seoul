def main():
    stringA = "abcdefghi"
    i = 0
    for s in stringA:
        print(s)
        print(i)
        i += 1
    for i in range(400):
        print(i, sep=' ', end=' ')
        if i % 20 == 0:
            print()

if __name__ == '__main__':
    main()

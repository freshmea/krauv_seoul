# function
class A:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def a(self):
        print('aaa')
    
    def b(self):
        print('bbb')

def main():
    a1 = A('choi', 80)
    a2 = A('kim', 76)
    a3 = A('jang', 54)
    a1.a()
    a2.a()
    a3.a()
    print(a1.name)

if __name__ == '__main__':
    main()

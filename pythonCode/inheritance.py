from strMethod import A

def func(a, b = 123, c = 'abc', *arg):
    print('function', a, b, c)
    for a in arg:
        print(a)

class A2(A):
    def __init__(self, name, weight, height, job = 'student'):
        # A.__init__(self)
        super().__init__(name, weight)
        self.height = height
        self.job = job

    def a(self):
        print('a2a2a2')

def main():
    a1 = A2('choi', 80, 172, 'teacher')
    a2 = A2('pack', 55, 160)
    a1.a()
    a1.b()
    print(a1.name)
    print(a1.job)
    func('hello', 456)
    func(1,2,3,4,5,6,7,8,9)

if __name__ == '__main__':
    main()

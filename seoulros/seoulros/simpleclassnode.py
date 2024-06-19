from rclpy.node import Node
import rclpy

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simplenode')
        self.create_timer(1, self.printtest)
        self.i = 0

    def printtest(self):
        print('ros test', self.i)
        self.i += 1

def main():
    rclpy.init()
    node = SimpleNode()
    rclpy.spin(node)


if __name__ == '__main__':
    main()

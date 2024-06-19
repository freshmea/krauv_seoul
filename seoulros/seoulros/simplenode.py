from rclpy import Node
import rclpy

i = 0

def printtest():
    print('ros test', i)
    i += 1

def main():
    rclpy.init()
    node = Node()
    node.create_timer(1, printtest)
    rclpy.spin(node)


if __name__ == '__main__':
    main()

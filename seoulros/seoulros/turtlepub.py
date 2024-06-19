import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePub(Node):
    def __init__(self):
        super().__init__('simplePub')
        self.create_timer(1, self.printtest)
        self.pub = self.create_publisher(String, "myMessage", 10)
        self.i = 0

    def printtest(self):
        msg = String()
        msg.data = 'ros test '+ str(self.i)
        self.pub.publish(msg)

        self.i += 1

def main():
    rclpy.init()
    node = SimplePub()
    rclpy.spin(node)


if __name__ == '__main__':
    main()

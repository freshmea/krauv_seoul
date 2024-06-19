import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TurtlePub(Node):
    def __init__(self):
        super().__init__('turtlePub')
        self.create_timer(1, self.printtest)
        self.pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.i = 0

    def printtest(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 1.0
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = TurtlePub()
    rclpy.spin(node)


if __name__ == '__main__':
    main()

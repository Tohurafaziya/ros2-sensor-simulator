import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub = self.create_publisher(Float32, 'sensor_data', 10)
        self.timer = self.create_timer(0.2, self.send)

    def send(self):
        msg = Float32()
        msg.data = random.uniform(0, 100)
        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main():
    rclpy.init()
    node = Publisher()
    rclpy.spin(node)
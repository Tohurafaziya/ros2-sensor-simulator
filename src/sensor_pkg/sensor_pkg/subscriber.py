
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'sensor_data',
            self.callback,
            10
        )

    def callback(self, msg):
        value = msg.data
        if value > 80:
            self.get_logger().warn(f'⚠ High value detected: {value}')
        else:
            self.get_logger().info(f'Received: {value}')


def main(args=None):   
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_pkg',
            executable='publisher',
            name='publisher'
        ),
        Node(
            package='sensor_pkg',
            executable='subscriber',
            name='subscriber'
        )
    ])
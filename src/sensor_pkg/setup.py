from setuptools import setup

package_name = 'sensor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='ROS2 sensor simulator',

    entry_points={
        'console_scripts': [
            'publisher = sensor_pkg.publisher:main',
            'subscriber = sensor_pkg.subscriber:main',
        ],
    },

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_launch.py']),
    ],
)
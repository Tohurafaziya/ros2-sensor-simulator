
FROM ros:humble

# Install required tools
RUN apt update && apt install -y \
    python3-pip \
    python3-colcon-common-extensions

# Workspace
WORKDIR /ros2_ws

# Copy ROS2 package
COPY src /ros2_ws/src

# Build workspace
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && cd /ros2_ws && colcon build --symlink-install"

CMD ["/bin/bash", "-lc", "source /opt/ros/humble/setup.bash && source /ros2_ws/install/setup.bash && ros2 launch sensor_pkg sensor_launch.py"]
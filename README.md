# Mani
This is a package for Mani.

## Packages List
* [hebi_description](https://github.com/iHaruruki/hebi_description.git)
* [hebi_msgs](https://github.com/iHaruruki/hebi_msgs.git)
* [hebi_ros2_examples](https://github.com/iHaruruki/hebi_ros2_examples.git)
* [hebi_hardware](https://github.com/iHaruruki/hebi_hardware.git)
* [hebi_bringup](https://github.com/iHaruruki/hebi_bringup.git)
* [hebi_moveit_configs](https://github.com/iHaruruki/hebi_moveit_configs.git)

## Setting up your Workspace
Run the following commands to set up and download the HEBI ROS 2 packages:
```bash
# Create the workspace directory
mkdir -p ~/hebi_ws/src
cd ~/hebi_ws/src

# Install HEBI C++ ROS API package
sudo apt-get install ros-$ROS_DISTRO-hebi-cpp-api

# Clone the HEBI description package
git clone -b ros2/humble https://github.com/iHaruruki/hebi_description.git

# Clone the HEBI messages package
git clone https://github.com/iHaruruki/hebi_msgs.git

# Clone this examples repository
git clone https://github.com/iHaruruki/hebi_ros2_examples.git

# Install hardware package
git clone https://github.com/iHaruruki/hebi_hardware.git

# Install bringup package
git clone -b humble https://github.com/iHaruruki/hebi_bringup.git

# Install ROS2 Control dependencies
sudo apt install ros-$ROS_DISTRO-ros2-control ros-$ROS_DISTRO-ros2-controllers -y

# Moveit2 package
git clone https://github.com/iHaruruki/hebi_moveit_configs.git
```
Install the necessary dependencies using `rosdep`:
```bash
cd ~/hebi_ws/
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```
Build the workspace and source it:
```bash
cd ~/hebi_ws
colcon build --symlink-install
source install/setup.bash
```
(Optional) Install `pip` dependencies for HRDF to URDF conversion script:

```bash
pip install -r src/hebi_ros2_examples/requirements.txt
```
## Standalone HEBI ROS2 API
**There are two ways to send angles:**
Example1:Using ros2 topic pub
Launching the Arm Node
```shell
ros2 launch hebi_ros2_examples arm.launch.py hebi_arm:=A-2085-06G
```
```shell
ros2 topic pub /joint_trajectory trajectory_msgs/JointTrajectory "{ 
  joint_names: [
    'Base','Shoulder','Elbow',
    'Wrist1','Wrist2','Wrist3'
  ],
  points: [
    { 
      positions:     [0.0,1.2,2.6,1.4,1.5,0.5],
      velocities:    [0.0,0.0,0.0,0.0,0.0,0.0],
      accelerations: [0.0,0.0,0.0,0.0,0.0,0.0],
      time_from_start: { sec: 5, nanosec: 0 }
    }
  ]
}"
```
Example2:Using Joy Stick
```shell
ros2 launch hebi_ros2_examples arm_joystick_teleop.launch.py hebi_arm:=A-2085-06G
```
## ROS2 Control

## Moveit2

## Additional Resources
* [HEBI Documentation](https://docs.hebi.us/)
* [ROS2 Control Documentation](https://docs.hebi.us/)
* [Moveit Documentation](https://moveit.ai/)
# Mani
This is a package for Mani.  
Mani is a dual-arm robot based on the Arm Kits from [HEBI robotics](https://www.hebirobotics.com/).

## Packages List
* [hebi_cpp_api_ros](https://github.com/iHaruruki/hebi_cpp_api_ros.git)
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
git clone -b ros2 https://github.com/HebiRobotics/hebi_cpp_api_ros.git

# Clone the HEBI description package
git clone -b ros2/humble https://github.com/HebiRobotics/hebi_description.git

# Clone the HEBI messages package
git clone https://github.com/HebiRobotics/hebi_msgs.git

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
## How to use
HEBI arms can be controlled with ROS 2 in three ways:

- [Standalone HEBI API](#standalone-hebi-ros2-api)
- [ROS 2 Control](#ros2-control)
- [MoveIt](#moveit)

The standalone HEBI API provides direct control via the HEBI C++ API, ROS 2 Control offers standardized interfaces, and MoveIt provides advanced motion planning capabilities.

### Standalone HEBI ROS2 API
**There are two ways to send angles:**    
#### Example1 : Using ros2 topic pub
Launching the Arm Node
```bash
ros2 launch hebi_ros2_examples arm.launch.py hebi_arm:=A-2085-06G generate_urdf:=false
```
```bash
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
#### Example2 : Using Joy Stick
```bash
ros2 launch hebi_ros2_examples arm_joystick_teleop.launch.py hebi_arm:=A-2085-06G generate_urdf:=false
```
### ROS2 Control
For ROS 2 control integration, you'll need the following three types of files:

- ROS2 Control Macro File - Defines hardware interfaces(`/hebi_description/urdf/kits/ros2_control/A-2085-06G.ros2_control.xacro`)
- Combined URDF File - Combines the macro with the existing URDF(`/hebi_description/urdf/kits/ros2_control/A-2095-06G.urdf.xacro`)
- Controller Parameter File - Configures controllers(`/hebi_bringup/config/A-2085-06G_controller.yaml`)
> [!TIP]  
> For standard HEBI kits, these files are already provided in the `hebi_bringup` and `hebi_description` packages.  

#### To launch the ROS 2 Control node with hardware
```bash
ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:=A-2085-06G use_mock_hardware:=false use_gripper:=true
```
#### Check Joint condition
```bash
ros2 topic echo /joint_states
```
#### Send gripper cosition
```bash
ros2 action send_goal /gripper_controller/gripper_cmd control_msgs/action/GripperCommand "{command: {position: 1.0, max_effort: 10.0}}"
```

### Moveit
#### Launch Robot Control(Use real hardware)
```bash
ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:=A-2085-06G use_mock_hardware:=false use_gripper:=true
```
#### Launch Moveit
```bash
ros2 launch hebi_bringup move_group.launch.py hebi_arm:=A-2085-06G use_sim_time:=false
```

## Additional Resources
HEBI Robotics
* [HEBI Documentation](https://docs.hebi.us/)

ROS 2 Control
* [ros2_control Documentation](https://control.ros.org/humble/index.html)

Moveit2
* [Moveit Documentation](https://moveit.ai/)

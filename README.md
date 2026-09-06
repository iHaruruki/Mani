# Mani
This is a package for Mani.  
Mani is a dual-arm robot based on the Arm Kits from [HEBI robotics](https://www.hebirobotics.com/).

## GitHub Project
**[Mani project](https://github.com/users/iHaruruki/projects/10)**  

> [!TIP] 
> **What is GitHub project?**  
> A project is an adaptable table, board, and roadmap that integrates with your issues and pull requests on GitHub to help you plan and track your work effectively at the user or organization level.

## 📦 Packages List
HEBI robotics official packages.

* [hebi_cpp_api_ros](https://github.com/HebiRobotics/hebi_cpp_api_ros.git)
* [hebi_description](https://github.com/HebiRobotics/hebi_description.git)
* [hebi_msgs](https://github.com/HebiRobotics/hebi_msgs.git)
* [hebi_ros2_examples](https://github.com/HebiRobotics/hebi_ros2_examples.git)
* [hebi_hardware](https://github.com/HebiRobotics/hebi_hardware.git)
* [hebi_bringup](https://github.com/HebiRobotics/hebi_bringup.git)
* [hebi_control](https://github.com/iHaruruki/hebi_control.git)
* [hebi_moveit_configs](https://github.com/HebiRobotics/hebi_moveit_configs.git)
* [mani_capture](https://github.com/bozznyskrtt/mani_capture.git)
* [auduio_data](https://github.com/iHaruruki/auduio_data.git)

## 🛠️ Setting up your Workspace
Run the following commands to set up and download the HEBI ROS 2 packages:
```bash
# Create the workspace directory
mkdir -p ~/hebi_ws/src
cd ~/hebi_ws/src

# Install HEBI C++ ROS API package
# git clone -b ros2 https://github.com/HebiRobotics/hebi_cpp_api_ros.git
sudo apt install ros-$ROS_DISTRO-hebi-cpp-api

# Clone the HEBI description package
git clone -b ros2/jazzy https://github.com/iHaruruki/hebi_description.git

# Clone the HEBI messages package
git clone https://github.com/iHaruruki/hebi_msgs.git

# Clone this examples repository
git clone https://github.com/iHaruruki/hebi_ros2_examples.git

# Install hardware package
git clone -b jazzy https://github.com/iHaruruki/hebi_hardware.git

# Install bringup package
git clone -b jazzy https://github.com/iHaruruki/hebi_bringup.git

# hebi_control
git clone https://github.com/iHaruruki/hebi_control.git

# Install ROS2 Control dependencies
sudo apt install ros-$ROS_DISTRO-ros2-control ros-$ROS_DISTRO-ros2-controllers -y

# Moveit2 package
git clone -b ros2 https://github.com/iHaruruki/hebi_moveit_configs.git

# Mani description
git clone https://github.com/iHaruruki/mani_description.git

# yolo_ros2
git clone https://github.com/iHaruruki/yolo_ros2.git
```

### Installing dependent packages and building
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

<!-- Creation of virtual environments
```bash
cd ~/hebi_ws
uv venv
source .venv/bin/activate
uv pip install hebi-py scipy numpy lxml

# (Optional) Install `pip` dependencies for HRDF to URDF conversion script:
# pip install -r src/hebi_ros2_examples/requirements.txt
```
> [!NOTE]
> Install `uv`  
> [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)
-->
### Setup Moveit2
```bash
sudo apt install ros-$ROS_DISTRO-moveit
```

### Setup CycloneDDS
```bash
sudo apt install ros-$ROS_DISTRO-rmw-cyclonedds-cpp
```
You may want to add `export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp` to your ~/.bashrc to source it automatically.
```bash
nano ~/.bashrc
```
```text
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

### Setup Depth Camera
Please check: [OrbbecSDK_ROS2_setup](https://github.com/iHaruruki/OrbbecSDK_ROS2_setup.git)

### Setup GPU
Please check: [egpu-ubuntu](https://github.com/iHaruruki/egpu-ubuntu.git)

## 🎮 Usage
HEBI arms can be controlled with ROS 2 in three ways:

<details>

<summary>Standalone HEBI ROS2 API</summary>

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

</details>

<details>

<summary>ROS2 Control</summary>

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

</details>

<details>

<summary>Moveit2</summary>

### Moveit2
#### Launch Robot Control(Use real hardware)
```bash
ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:=A-2085-06G use_mock_hardware:=false use_gripper:=true
```
#### Launch Moveit
```bash
ros2 launch hebi_bringup move_group.launch.py hebi_arm:=A-2085-06G use_sim_time:=false
```
> [!WARNING]
> Gripper opening and closing
> Movable range: 0 degrees to -90 degrees (0 [rad] to -1.570 [rad])  
> 可動範囲：0度 ～ -90度(0 [rad] ~ -1.570 [rad])

### Object Recognition and Automaic Approach
#### Launch Robot Control(Use real hardware)
```bash
ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:=A-2085-06G use_mock_hardware:=false use_gripper:=true
```
#### Launch Moveit
```bash
ros2 launch hebi_bringup move_group.launch.py hebi_arm:=A-2085-06G use_sim_time:=false
```
#### Run Depth Camera
```bash
ros2 launch orbbec_camera astra_stereo_u3.launch.py
```
#### Run `mani_description`
```bash
ros2 launch mani_description robot.launch.py
# If TF fails to start.
ros2 run tf2_ros static_transform_publisher 0.05 0.06 -0.065 0 0 0 base_link camera_link
```
#### Run YOLO node
```bash
ros2 launch yolo_bringup yolo.launch.py model:=yolo26m.pt device:="cuda:0" use_3d:=True
```
##### model
When using a teddy bear: `model:="yolo26m.pt"`
When using a handbell: `model:="/home/robot/camera_data/datasets_2/runs/detect/train/weights/best.pt"`

##### `device`
CPU mode: `device:="cpu"`  
GPU mode: `device:="cuda:0"`

#### Publish robot description
```bash
ros2 launch hebi_a-2085-06g_moveit_config move_group.launch.py
```
![png](/meida/robotdescription.png)

#### hebi_controll
```bash
ros2 launch hebi_control hebi_movers.launch.py
```

</details>

## Use Cases

### :bear: Terry Bear :bear:

This command makes Mani move and capture depth image.
```bash
ros2 launch mani_capture mani_capture.launch.py
```

This command does all the segmentation, prediction, subtraction,clustering, data cleaning and then reconstruct the 3d shapes using TSDF algorithm.
```bash
ros2 launch mani_capture mani_postprocess.launch.py
```

### :bell: Hand Bell :bell:
```bash
ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:=A-2085-06G use_mock_hardware:=false use_gripper:=true
```
```bash
ros2 launch orbbec_camera astra_stereo_u3.launch.py
```
```bash
ros2 run tf2_ros static_transform_publisher 0.05 0.06 -0.065 0 0 0 base_link camera_link
```
```bash
ros2 launch yolo_bringup yolo.launch.py model:=/home/robot/camera_data/datasets_2/runs/detect/train/weights/best.pt device:="cuda:0" use_3d:=True
```
```bash
ros2 launch hebi_a-2085-06g_moveit_config move_group.launch.py
```
```bash
ros2 launch hebi_control hebi_moversBell.launch.py
```
```bash
source ~/hebi_ws/src/auduio_data/.venv/bin/activate
ros2 run audio_data bell_ai.py check
```
```bash
source ~/hebi_ws/src/auduio_data/.venv/bin/activate
ros2 run audio_data bell_fsm.py
```
```bash
source ~/hebi_ws/src/auduio_data/.venv/bin/activate
ros2 run audio_data display_note.py
```


<!-- ## rosbsg 
### ros2 bag play
```bash
rviz2 -d ~/hebi_ws/src/hebi_description/rviz/hebi.rviz
```
```bash
rviz2 -d ~/hebi_ws/src/hebi_moveit_configs/hebi_a-2085-06g_moveit_config/config/moveit.rviz 
```
```bash
ros2 run yolo_ros2 object_detection_tf_node
```
```bash
ros2 bag play ~/ros2_ws/ros2_bag/rosbag2_xxxx_xx_xx-xx_xx_xx/
``` -->

## 👤 Authors

- **[iHaruruki](https://github.com/iHaruruki)**
- **[SatoAsumu](https://github.com/SatoAsumu)**
- **[KaitKuma](https://github.com/KaitKuma)**
- **[bozznyskrtt](https://github.com/bozznyskrtt)**
- **[KongkiatTen](https://github.com/KongkiatTen)**

## 📚 References
HEBI Robotics
* [HEBI Documentation](https://docs.hebi.us/)

ROS 2 Control
* [ros2_control Documentation](https://control.ros.org/jazzy/index.html)

Moveit2
* [Moveit Documentation](https://moveit.ai/)

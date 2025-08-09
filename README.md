# Mani
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
```
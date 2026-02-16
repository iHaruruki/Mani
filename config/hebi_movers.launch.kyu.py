from launch import LaunchDescription 
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hebi_a-2085-06g_moveit_config',
            executable='hebi_arm_mover1',
            name='hebi_arm_mover1',
            output='screen'
        ),
        
        Node(
            package='hebi_a-2085-06g_moveit_config',
            executable='hebi_arm_mover2',
            name='hebi_arm_mover2',
            output='screen'
        ),
        
        Node(
            package='hebi_control',
            executable='hebi_mover',
            name='hebi_sequence_manager',
            output='screen',
            emulate_tty=True,
        ),
        
        Node(
            package='hebi_a-2085-06g_moveit_config',
            executable='hebi_arm_mover3',
            name='hebi_arm_mover3',
            output='screen'
        ),
        
        Node(
            package='hebi_a-2085-06g_moveit_config',
            executable='hebi_j6_rotator',
            name='hebi_j6_rotator',
            output='screen',
            
            parameters=[
                robot_description,
                robot_description_semantic,
                kinematics_yaml,
            ]
        )
    ])

from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Ruta al archivo URDF
    urdf_file_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'urdf', 'RobotIndustrial.urdf'
    )
    # Ruta al archivo RVIZ
    rviz_config_file = os.path.join(
        os.path.dirname(__file__),
        '..', 'config', 'RobotIndustrial.rviz'
    )

    # Lectura del contenido del URDF
    with open(urdf_file_path, 'r') as urdf_file:
        robot_description = urdf_file.read()

    return LaunchDescription([
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        )
    ])

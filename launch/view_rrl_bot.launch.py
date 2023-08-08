from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.substitutions import Command
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    rfp_gz_intro_package_path = get_package_share_path('rfp_gz_intro')
    model_path = str(
        rfp_gz_intro_package_path / 'urdf/rrl_bot.urdf')
    rviz_config_path = str(
        rfp_gz_intro_package_path / 'rviz/rrl_bot.rviz')

    urdf_tutorial_package_path = get_package_share_path('urdf_tutorial')
    urdf_tutorial_display = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            str(urdf_tutorial_package_path / 'launch/display.launch.py')),
        launch_arguments={'gui': 'true', 'model': model_path,
                          'rvizconfig': rviz_config_path}.items()
    )

    return LaunchDescription([
        urdf_tutorial_display,
    ])

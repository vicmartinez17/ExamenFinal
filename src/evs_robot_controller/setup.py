from setuptools import setup

package_name = 'evs_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Robotics Lab - 2025-1',
    maintainer_email='vicppc7@gmail.com',
    description='Controlador de trayectoria para el EVS',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'square_trajectory = evs_robot_controller.square_trajectory:main',
        ],
    },
)

import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robousr/ROS2Dev/ExaFin_ws/install/evs_robot_controller'

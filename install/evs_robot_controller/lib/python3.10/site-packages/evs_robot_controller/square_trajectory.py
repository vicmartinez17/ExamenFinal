import rcply
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class SquareTrajectory(Node):
    def __init__(self):
        super().__init__('square_trajectory')
        self.publisher_ = self.create_publisher(Twist, '/cmed_vel', 10)
        self.timer = self.create_timer(1, self.publish_square_trajectory)
        self.step = 0

    def publish_square_trajectory(self):
        msg = Twist()

        # Movimientos en los cuatro lados del cuadrado
        if self.step < 4:
            msg.linear.x = 0.5 # Adelante
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2 # Giro de 90 grados

        self.publisher_publish(msg)



        #  Next step
        self.step += 1
        if self.step == 8:
            self.step = 0 # Reinicio de trayectoria

def main(args=None):
    rclpy.init(args=args)
    node = SquareTrajectory()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
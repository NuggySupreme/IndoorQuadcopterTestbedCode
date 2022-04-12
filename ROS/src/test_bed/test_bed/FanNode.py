import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FanNode(Node):

    def __init__(self):
        super().__init__('FanNode')
        self.subscription = self.create_subscription(
            String,
            'fans',
            self.listener_callback,
            20)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    fanNode = FanNode()

    rclpy.spin(fanNode)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    fanNode.destroy_node()
    rclpy.shutdown()
	
if __name__ == '__main__':
    main()
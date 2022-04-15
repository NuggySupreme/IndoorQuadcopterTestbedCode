import rclpy
from rclpy.node import Node
from bed_messages.msg import PSControl

class TurnOff(Node):
   def __init__(self):
      super().__init__('turn_off')
      self.pub = self.create_publisher(PSControl, 'ps_control_messages', 10)

      for i in range(4):
         msg = PSControl()
         msg.ps_num = i
         msg.voltage = 0.00
         msg.current = -1.00
         msg.turn_off = 1
         self.pub.publish(msg)

def main(args=None):
   rclpy.init(args=args)
   off = TurnOff()
   off.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()

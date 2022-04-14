import rclpy
from rclpy.node import Node
from bed_messages.msg import PSControl

class PSTester(Node):
   def __init__(self):
      super().__init__('ps_tester')
      self.publisher = self.create_publisher(PSControl, 'ps_control_messages', 10)
      timer_period = 2 #seconds
      self.timer = self.create_timer(timer_period, self.timer_callback)
      self.i = 0.00

   def timer_callback(self):
      msg = PSControl()
      msg.ps_num = 3
      #msg.voltage = self.i % 13
      msg.voltage = 0.00
      print(msg.voltage)
      msg.current = -1.00
      self.i += 1
      self.publisher.publish(msg)

def main(args=None):
   rclpy.init(args=args)
   ps_tester = PSTester()
   rclpy.spin(ps_tester)
   ps_tester.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()

import rospy #ROS Python library
import sys #Needed for command line arguments
from fan_driver import FanDriver #Get object that represents fan regulator IC

if len(sys.argv < 2):
    print("Usage: rosrun exampletestcode fan_driver.py <fan num>") #usage command
    quit()
    
if __name__ == "__main__":
    rospy.init_node("fan_driver_" + sys.argv[0]) #name node so fans are different

    rospy.Subscriber("fan_speed_" + sys.argv[0])
    fan = FanDriver(max_speed = 4000) #create fan with different max rpm from default
    rospy.on_shutdown(fan.stop) #function to execute when node is stopped

    rospy.loginfo("Fan driver" + sys.argv[0] + "is now started, ready to get commands.") #logger info for debugging
    rospy.spin() #continuously run until node is stopped

#!/usr/bin/python

from std_msgs.msg import String
import rospy

class test_network_conn(object):
	def __init__(self):
		self.pub = rospy.Publisher("/test_publisher", String, queue_size = 1)
		self.string = "Teste"

	def publish_string(self):
		string = self.string
		self.pub.publish(string)

def main():
	rospy.init_node("Publish_string")
	test_net = test_network_conn()
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		test_net.publish_string()
		rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"	
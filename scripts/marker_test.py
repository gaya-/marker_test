#!/usr/bin/env python
# insert BSD license here

import rospy
from visualization_msgs.msg import Marker
import time

if __name__ == '__main__':
    try:
        pub = rospy.Publisher('visualization_marker', Marker, queue_size=1)
        rospy.init_node('publish_marker')
        time.sleep(1)

        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = 10
        marker.action = 0
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.color.r = 0.6
        marker.color.g = 0.3
        marker.color.b = 0.1
        marker.color.a = 1.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 1.0
        marker.mesh_resource = "package://marker_test/resource/box.dae"
        pub.publish(marker)

    except rospy.ROSInterruptException:
        pass

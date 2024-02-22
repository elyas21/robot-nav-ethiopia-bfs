from move_r.path import path_finder
import rclpy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3
from math import atan2, pi, sqrt

def odom_callback(msg, cmd_vel_publisher, linear_speed, angular_speed, goals, stop_threshold):
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y
    target_point = goals[0]

    print(f"Current Position: x={current_x}, y={current_y}")
    print(f' goal is ${target_point}')
    if not goals:
        # No more goals to reach, stop the robot
        twist_msg = Twist()
        twist_msg.linear = Vector3(x=0.0)
        twist_msg.angular = Vector3(z=0.0)
        cmd_vel_publisher.publish(twist_msg)
        print("All goals reached. Stopping.")
        return

    distance_to_target = sqrt((target_point['x'] - current_x)**2 + (target_point['y'] - current_y)**2)

    if distance_to_target < stop_threshold:
        # Remove the reached goal from the list
        goals.pop(0)
        print(f"Goal reached. Remaining goals: {goals}")
        return

    angle_to_target = atan2(target_point['y'] - current_y, target_point['x'] - current_x)
    current_orientation_z = msg.pose.pose.orientation.z
    current_orientation_w = msg.pose.pose.orientation.w
    current_yaw = 2.0 * atan2(current_orientation_z, current_orientation_w)
    angle_difference = angle_to_target - current_yaw

    if angle_difference > pi:
        angle_difference -= 2.0 * pi
    elif angle_difference < -pi:
        angle_difference += 2.0 * pi

    twist_msg = Twist()
    twist_msg.linear = Vector3(x=round(linear_speed, 2))
    twist_msg.angular = Vector3(z=round(angular_speed * angle_difference, 2))

    cmd_vel_publisher.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('move_robot')

    cmd_vel_publisher = node.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)

    linear_speed = float(input('insert linear speed: '))
    angular_speed = float(input('insert angular speed: '))

    # goals = [{'x': 4.0, 'y': 4.5}, {'x': 6.0, 'y': 3.0} , {'x': 0.0, 'y': 0.0}]  # Add more goals as needed
    goals = path_finder('Addis_Abeba' , 'Harar')
    stop_threshold = float(input('stop threshold: '))

    subscription = node.create_subscription(
        Odometry,
        'odom',  # replace 'odom_topic' with the actual odometry topic name
        lambda msg: odom_callback(msg, cmd_vel_publisher, linear_speed, angular_speed, goals, stop_threshold),
        10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Shutting down")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
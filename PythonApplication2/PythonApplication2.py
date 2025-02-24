from djitellopy import Tello
import easytello
import time
import cv2
import math
import random

tello = Tello()
tello.connect()
print("bat: ",tello.get_battery(), "%")
print("heat: ",tello.get_temperature(), "degrees")
print('presha: ',tello.get_barometer(), "Pa")

tello.takeoff()
#drawing an X and doing a flip
"""time.sleep(1)
tello.go_xyz_speed(0,40,50,20)
tello.go_xyz_speed(0,-80,-100,20) #go past 0,0,0 by the same distance
tello.go_xyz_speed(0,40,50,20)#now on its 0,0,0
time.sleep(0.5)
tello.go_xyz_speed(0,-40,50,20)
tello.go_xyz_speed(0,80,-100,20)
tello.go_xyz_speed(0,-40,50,20)#back to 0,0,0
time.sleep(0.5)"""
#tello.flip_back()

#code with waypoints for drone to go to
"""
time.sleep(1)  # Give the drone time to stabilize

    # Define the flight path as a list of waypoints (x, y, z) relative to takeoff point
flight_path = [
        (0, 40, 50),   # Move forward 50cm, up 50cm
        (50, 40, 50),  # Move right 50cm
        (0, -50, 50), # Move back
        (0, -50, 50),  # Move left 50cm
        (0, 0, -60),    # Descend 60cm
        (0, 0, 0)      # Descend to the ground (relative to the last point)
]

for waypoint in flight_path:
        x, y, z = waypoint
        print(f"Moving to waypoint: {waypoint}")

        # Use go_xyz_speed for more precise movement to waypoints
        tello.go_xyz_speed(x, y, z, 50)  # Speed 50 cm/s. Adjust as needed.

        time.sleep(1.2)  # Allow time to reach the waypoint"""

#draw a circle
"""time.sleep(1)

radius = 50 # Smaller radius (adjust as needed)
speed = 30    # Speed (adjust as needed)
num_segments = 36  # Number of segments (adjust as needed)
for i in range(num_segments + 1):
        angle = (360 * i / num_segments) * math.pi / 180
        x = int(radius * math.cos(angle))
        z = int(radius * math.sin(angle))  # Circle along the z-axis
        y = 0  # y is constant (no horizontal movement)

        tello.go_xyz_speed(x, y, z, speed)
        time.sleep(0.5)"""

#flip for correct answer
math_questions = [
        "( 2 * 5 ) + (-2.5 * 3.2 ) + 8 = ?",
        "2 * 5 = ?",
        "(20 / 2 ) + ( 4 * 5)- ( 2 * 5 ) = ?",
        "15 - 5 = ?",
        "0.01 * 10 ** 3  = ?",
        "100 / 10 = ?",
        "( 2 * 2 * 2) + (12 / 2) + (18 / 3) - (4 * 2)= ?",
        "16.4 - 5.9-0.5 = ?",
        "3 * 3 + 1 = ?", 
        "25 / 2.5 = ?"
]
time.sleep(2)
while True:
   user_input = input("Press Enter for a question (or 'land' to land) or press esc: ").lower()

   if user_input == " land ":
            break

   if cv2.waitKey(1) == 27:
          break

   if user_input == "": # If the user just presses enter
            random_question = random.choice(math_questions)
            attempt = 0
            while attempt < 3:
                print(random_question)
                time.sleep(4)
                if cv2.waitKey(1) == 27:
                    break
                try:
                  ans = int(input("waiting for your answer :"))
                  if ans == 10:
                    tello.flip_forward()

































































                  if ans != 10:
                    tello.flip_back()
                    break

                except  ValueError:
                  print("Invalid input. Press Enter or type 'land'.")
                  attempt +=1

            if attempt == 3:
                  print(" ...drone is landing ")
                  tello.land()
   print("Drone is hovering. Waiting for input...")
   time.sleep(2)

#rotate left and right
"""tello.rotate_counter_clockwise(90)
tello.rotate_clockwise(180)
tello.rotate_counter_clockwise(90)"""

#bouncing 
"""tello.move_up(60)
tello.move_down(60)
tello.move_up(40)
tello.move_down(40)
tello.move_up(30)
tello.move_down(30)
tello.move_up(10)"""

tello.land()


































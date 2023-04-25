# nexus_controller
The python-based framework for the real-world and Gazebo simulations of the control of the Nexus 4WD Mecanum wheel robot movement and simultaneous localization of a stationary landmark.

### Installation
Create a catkin workspace by following the ROS noetic catkin setup tutorials. Especially [the first videos in this playlist](https://www.youtube.com/playlist?list=PLLSegLrePWgIbIrA4iehUQ-impvIXdd9Q) are helpful.

### Running the code
To control either the real-world or run a Gazebo simulation, the following script and associated inputs (flags) can be used. If no inputs are provided the default value will be used. For movement, options include forward, backward, right, left, and circle. None of the inputs need to be invoked with "", the code will handle this. Additionally, when using the distance-only estimator, the chosen trajectory will be dynamically optimized based on the current position, instead of using the inputted movement.
```
FLAGS:
  simulation: bool | default = True           | simulate or control a real-world Nexus 4WD
  estimator: str   | default = WSR            | choose distance-only (DO) or WSR estimator
  name: str        | default = "nexus_car"    | the name of the robot as seen in Gazebo
  port: str        | default = "/dev/ttyUSB0" | USB port connected to the real-world Nexus 4WD
  velmag: float    | default = 0.1            | magnitude of the velocity in meters/second
  timestep: float  | default = 0.05           | the time step between consecutive loop iterations
  move: str        | default = "circle"       | movement of the robot, distance based on velmag
  runtime: float   | default = 10.0           | the time of runnning the program in seconds
```
Option 1: directly invoking python from the scripts directory
```
cd ~/catkin_ws/src/nexus_controller/
python3 main.py 
python3 main.py -simulation True -name nexus_car -port /dev/ttyUSB0 -velmag 0.1 -timestep 0.05 -move circle -runtime 10.0
```
Option 2: using rosrun
```
rosrun nexus_controller main.py
rosrun nexus_controller main.py -simulation True -name nexus_car -port /dev/ttyUSB0 -velmag 0.1 -timestep 0.05 -move circle -runtime 10.0
```

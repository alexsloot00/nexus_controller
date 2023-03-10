#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 23-03-2023
"""

import sys, time, argparse
from distance_only_estimator import DistanceOnlyEstimator
from wsr_estimator import WSREstimator
from landmark import Landmark
from create_nexus_car import create_a_nexus_car
from helper_functions import parse_simulation_argument
from terminal_functions import start_roscore


def main() -> None:
    """Run the Nexus robot landmark localization."""
    # parsing optional arguments from shell
    parser = argparse.ArgumentParser(description="Add optional parameters")
    parser.add_argument(
        "-simulation",
        "--simulation",
        help="choose: True/False, i.e. -simulation False",
        required=False,
        default="True",
    )
    parser.add_argument(
        "-name",
        "--name",
        help="choose: a name, i.e. -name nexus_car",
        required=False,
        default="nexus_car",
    )
    parser.add_argument(
        "-port",
        "--port",
        help="choose: a port, i.e. -port /dev/ttyUSB0",
        required=False,
        default="/dev/ttyUSB0",
    )
    parser.add_argument(
        "-velmag",
        "--velmag",
        help="Choose velocity magnitude: i.e. -velmag 0.1",
        required=False,
        default=0.1,
    )
    parser.add_argument(
        "-timestep",
        "--timestep",
        help="Choose a timestep in seconds: i.e. -timestep 0.05",
        required=False,
        default=0.05,
    )
    parser.add_argument(
        "-move",
        "--move",
        help="Choose: circle, forward, backward right, left: i.e. -move circle",
        required=False,
        default="circle",
    )

    argument = parser.parse_args()
    simulation = parse_simulation_argument(argument.simulation)
    name = argument.name
    port = argument.port
    velocity_magnitude = argument.velmag
    time_step = argument.timestep
    move = argument.move

    # start a rosmaster (does not work on ssh access)
    # start_roscore()

    # create an instance of the nexus car
    nexus_car = create_a_nexus_car(
        simulation=simulation,
        name=name,
        port=port,
        velocity_magnitude=velocity_magnitude,
        time_step=time_step,
        move=move,
    )

    # create a landmark, initialize on robot position (0,0)
    landmark = Landmark(theta=-1.6, simulation=simulation)
    landmark.initialize(0, 0)

    # choose an estimator and assign to the nexus_car
    # estimator = DistanceOnlyEstimator(landmark)
    estimator = WSREstimator(landmark)
    nexus_car.give_DO_estimator(estimator)

    # choose what to do
    # nexus_car.move_square()
    time.sleep(5)
    nexus_car.start()

    # stop the system
    # nexus_car.stop()
    sys.exit()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 23-03-2023
"""

import math
from landmark import Landmark
from typing import List


class WSREstimator:
    def __init__(self, landmark: Landmark) -> None:
        """Initializer, needs a landmark object."""
        self.landmark = landmark

    def do_iteration(
        self,
        robot_x: float,
        robot_y: float,
        time_step: float,
        u: List[float],
        w: List[float],
    ):
        pass

    def measure(self, robot_x: float, robot_y: float) -> None:
        """Measure distance to landmark."""
        pass

    def calculate(
        self,
        robot_x: float,
        robot_y: float,
        time_step: float,
        u: List[float],
        w: List[float],
    ) -> None:
        """Calculate the predicted robot and landmark positions."""
        pass

    def process_data(self) -> None:
        """Process the measured data into useable inputs."""
        pass

    def predict(
        self,
        robot_x: float,
        robot_y: float,
        time_step: float,
        u: List[float],
        w: List[float],
    ) -> None:
        """Predict where the robot and landmark are using past estimate and new measurement."""
        pass

    def decide_movement(
        self, robot_x: float, robot_y: float, magnitude: float, time_passed: float
    ) -> List[float]:
        """Decide how to act based on the prediction"""
        circle_radius = 0.3  # meters
        # angle based on 10 seconds total time
        angle = time_passed / 10 * math.radians(360)
        w = 1  # derivative of angle increase
        xdot = -circle_radius * w * math.sin(angle)
        ydot = circle_radius * w * math.cos(angle)
        return [xdot, ydot]

    def update(self) -> None:
        """Update the landmark and robot position estimations"""
        pass

    def print(self) -> None:
        print("printing")


def test(time_passed):
    circle_radius = 1  # meters
    # angle based on 10 seconds total time
    angle = time_passed / 10 * math.radians(360)
    w = 1  # derivative of angle increase
    xdot = -circle_radius * w * math.sin(angle)
    ydot = circle_radius * w * math.cos(angle)
    return [xdot, ydot]


if __name__ == "__main__":
    a = test(0)
    print(a)
    a = test(2.5)
    print(a)
    a = test(5)
    print(a)
    a = test(7.5)
    print(a)
    a = test(10)
    print(a)

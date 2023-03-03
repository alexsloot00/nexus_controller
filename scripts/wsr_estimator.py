#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 23-03-2023
"""

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

    def decide_movement(self, robot_x: float, robot_y: float, magnitude: float) -> None:
        """Decide how to act based on the prediction"""
        return [0, 0]

    def update(self) -> None:
        """Update the landmark and robot position estimations"""
        pass

    def print(self) -> None:
        print("printing")

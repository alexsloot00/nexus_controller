#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 23-03-2023
"""


class WSREstimator:
    def __init__(self) -> None:
        pass

    def do_iteration(self):
        pass

    def measure(self):
        """Measure distance to landmark."""
        pass

    def calculate(self):
        """Calculate the predicted robot and landmark positions."""
        pass

    def process_data(self):
        """Process the measured data into useable inputs."""
        pass

    def predict(self):
        """Predict where the robot and landmark are using past estimate and new measurement."""
        pass

    def decide_movement(self):
        """Decide how to act based on the prediction"""
        return [0, 0]

    def update(self):
        """Update the landmark and robot position estimations"""
        pass

    def print(self):
        print("printing")

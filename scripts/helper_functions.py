#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 23-03-2023
"""
import math


def map_to_two_pi(value: float) -> float:
    """Maps a value in radians to [-pi, pi]."""
    if value > 2 * math.pi:
        return value - 2 * math.pi
    elif value < -2 * math.pi:
        return value + 2 * math.pi
    else:
        return value


def parse_simulation_argument(strbool: str) -> bool:
    strbool = strbool.lower()
    if strbool == "false":
        return False
    elif strbool == "true":
        return True
    else:
        print(
            "WARNING: simulation is not a valid input, choose 'True' or 'False'. Now using simulation=True."
        )

#!/usr/bin/env python3
"""
Author: Alex Sloot
University of Groningen
Last modified: 02-03-2023
"""
import sys, math
from multiprocessing.sharedctypes import Value


def map_to_two_pi(value: float) -> float:
    """Maps a value in radians to [-pi, pi]."""
    if value > 2 * math.pi:
        return value - 2 * math.pi
    elif value < -2 * math.pi:
        return value + 2 * math.pi
    else:
        return value


def parse_bool_argument(strbool: str) -> bool:
    """Converts the boolean string input to a boolean value."""
    strbool = strbool.lower()
    if strbool == "false":
        return False
    elif strbool == "true":
        return True
    else:
        print("WARNING: simulation is not a valid input, choose 'True' or 'False'!")
        sys.exit()


def parse_float_argument(strfloat: str) -> float:
    """Converts the string inputs to float values."""
    try:
        a = float(strfloat)
        return a
    except ValueError:
        print(f"ERROR: '{strfloat}' is not a valid input!")
        sys.exit()

import numpy
import sys

def say_hi(name = None):
    if name:
        return f"Hey {name}! It's so nice meeting you!"
    else:
        return "Please introduce yourself..."

    
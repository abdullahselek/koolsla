#!/usr/bin/env python

import re

from colorama import init
from termcolor import colored

init()  # Termcolor support for win32

# Colors for output texts
red = 'red'
green = 'green'
yellow = 'yellow'
blue = 'blue'


def print_red(message: str):
    """Print out red colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, red))


def print_green(message: str):
    """Print out green colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, green))


def print_yellow(message: str):
    """Print out yellow colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, yellow))


def print_blue(message: str):
    """Print out blue colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, blue))
  

def print_dish(name: str, dish_id: int, color: str):
    """Print out dish name and id with given color.
    Args:
      name (str): Dish name.
      dish_id (int): ID.
      color (str): Color name.
    """

    print(colored('* Name : ' + name + ' - ID : ' + str(dish_id), color))

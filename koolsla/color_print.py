#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from colorama import init
from termcolor import colored

init()  # Termcolor support for win32

# Colors for output texts
red = 'red'
green = 'green'
yellow = 'yellow'
blue = 'blue'

def print_red(message):
    """Print out red colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, red))

def print_green(message):
    """Print out green colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, green))

def print_yellow(message):
    """Print out yellow colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, yellow))


def print_blue(message):
    """Print out blue colored text.
    Args:
      message (str): Text.
    """

    print(colored(message, blue))
  
def print_dish(name, dish_id, color):
    """Print out dish name and id with given color.
    Args:
      name (str): Dish name.
      dish_id (int): ID.
    """

    print(colored('* Name : ' + name + ' - ID : ' + str(dish_id), color))

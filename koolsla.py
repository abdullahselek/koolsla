#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from koolsla import (
    __version__,
    recommender,
    data
)

help_message = '''
  Food recommendation tool with Machine learning.

  Usage
    $ python koolsla.py [<options> ...]

  Options
    --help, -h              Display help message
    --dish, -d <int>        Input dish ID [Can be any integer 0-424508]
    --list, -l              List available dish titles
    --recommend, -r <int>   Number of recommendations [Can be any integer 1-30]
    --version, -v           Display installed version

  Examples
    $ python koolsla.py --help
    $ python koolsla.py --dish 25
    $ python koolsla.py -d 25 --recommend 3
'''

koolsla_version = __version__

@click.command(add_help_option=False)
@click.option('-d', '--dish', default=25, help='Input dish ID')
@click.option(
    '-r', '--recommend', default=3, help='Number of dish recommendations')
@click.option(
    '-v',
    '--version',
    is_flag=True,
    default=False,
    help='Display installed version')
@click.option(
    '-h', '--help', is_flag=True, default=False, help='Display help message')
@click.option(
    '-l', '--list', is_flag=True, default=False, help='List dish titles')

def main(dish, recommend, version, help, list):
    if (help):
        print(help_message)
        sys.exit(0)
    else:
        if (version):
            print('koolsla' +  ' ' + koolsla_version)
        else:
            if (list):
                listLength = click.prompt('Number of dishes to list', type=int)
                data.list_of_dishes(length=listLength)
            else:
                recommender.recommend(dish_id=dish, recommendation_count=recommend)

if __name__ == '__main__':
    main()

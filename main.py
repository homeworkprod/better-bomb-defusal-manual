#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run the Better Bomb Defusal Manual

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from argparse import ArgumentParser
from importlib import import_module

from bombdefusalmanual.ui.console import ConsoleUI
from bombdefusalmanual.ui.models import Choice


CHOICES = [
    Choice('thebutton'       , 'The Button'       ), # page 6
    Choice('whosonfirst'     , 'Who\'s on First'  ), # pages 9-10
    Choice('morsecode'       , 'Morse Code'       ), # page 12
    Choice('complicatedwires', 'Complicated Wires'), # page 13
    Choice('passwords'       , 'Passwords'        ), # page 16
]


def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        '--gui',
        action='store_true',
        default=False,
        dest='use_gui',
        help='use graphical user interface')

    return parser.parse_args()


def get_ui_class(use_gui):
    if use_gui:
        from bombdefusalmanual.ui.tk import TkGUI
        return TkGUI
    else:
        return ConsoleUI


def ask_for_subject(ui):
    return ui.ask_for_choice('Which subject?', CHOICES)


def import_subject_module(name):
    return import_module('bombdefusalmanual.subjects.{}'.format(name))


def provide_subjects(ui_class):
    subject_name = ask_for_subject(ui_class())
    print('after subject name')

    module = import_subject_module(subject_name)

    try:
        module.execute(ui_class())
    except SystemExit:
        # Close subject and show overview.
        pass


if __name__ == '__main__':
    args = parse_args()
    ui_class = get_ui_class(args.use_gui)

    while True:
        provide_subjects(ui_class)

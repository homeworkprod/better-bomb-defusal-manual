#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run the Better Bomb Defusal Manual

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from importlib import import_module

from bombdefusalmanual.ui.console import ConsoleUI
from bombdefusalmanual.ui.models import Answer


ANSWERS = [
    Answer('thebutton', 'The Button'),
    Answer('complicatedwires', 'Complicated Wires'),
    Answer('morsecode', 'Morse Code'),
    Answer('passwords', 'Passwords'),
    Answer('whosonfirst', 'Who\'s on First'),
]


def ask_for_subject(ui):
    return ui.ask_for_choice('Which subject?', ANSWERS)


def import_subject_module(name):
    return import_module('bombdefusalmanual.subjects.{}'.format(name))


if __name__ == '__main__':
    ui = ConsoleUI()
    subject_name = ask_for_subject(ui)
    module = import_subject_module(subject_name)
    module.execute(ui)

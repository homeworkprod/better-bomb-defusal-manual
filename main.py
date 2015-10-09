#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run the Better Bomb Defusal Manual

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from importlib import import_module

from bombdefusalmanual.userinterface import Answer, Question, ask_question


ANSWERS = [
    Answer('thebutton', 'The Button'),
    Answer('complicatedwires', 'Complicated Wires'),
    Answer('morsecode', 'Morse Code'),
    Answer('passwords', 'Passwords'),
    Answer('whosonfirst', 'Who\'s on First'),
]

QUESTION = Question('Which subject?', ANSWERS)


def ask_for_subject():
    return ask_question(QUESTION)


def execute_subject_module(name):
    module = import_module('bombdefusalmanual.subjects.{}'.format(name))
    module.execute()


if __name__ == '__main__':
    subject_name = ask_for_subject()
    execute_subject_module(subject_name)

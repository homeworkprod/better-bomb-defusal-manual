# -*- coding: utf-8 -*-

"""
Console user interface to ask questions and collect answers.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from .models import Choice


class ConsoleUI(object):

    def ask_for_text(self, question_label):
        display_question(question_label)
        return ask_for_input()

    def ask_for_choice(self, question_label, choices, *, color_map=None):
        """Present a question to the user and return the value of the
        selected choice.
        """
        while True:
            display_question_and_choices(question_label, choices)
            valid_values = get_valid_values(choices)
            selection_input = ask_for_input()
            if selection_input in valid_values:
                break

        selected_index = int(selection_input) - 1
        choice = choices[selected_index]
        return choice.value

    def display_instruction(self, text):
        print('\n  => {} <=\n'.format(text))


def ask_for_input():
    return input('> ')


def display_question_and_choices(question_label, choices):
    display_question(question_label)
    for i, choice in enumerate(choices, start=1):
        print('[{:d}] {}'.format(i, choice.label))


def display_question(label):
    print('\n' + label)


def get_valid_values(choices):
    return frozenset(map(str, range(1, len(choices) + 1)))

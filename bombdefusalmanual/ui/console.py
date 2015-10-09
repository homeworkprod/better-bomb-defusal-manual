# -*- coding: utf-8 -*-

"""
Console user interface to ask questions and collect answers.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from .models import Answer


class ConsoleUI(object):

    def ask_for_text(self, question_label):
        display_question(question_label)
        return ask_for_input()


    def ask_for_choice(self, question_label, answers):
        """Present a question to the user and return the value of the
        selected answer.
        """
        while True:
            display_question_and_answers(question_label, answers)
            valid_values = get_valid_values(answers)
            selection_input = ask_for_input()
            if selection_input in valid_values:
                break

        selected_index = int(selection_input) - 1
        answer = answers[selected_index]
        return answer.value


    def display_instruction(self, text):
        print('\n  => {} <=\n'.format(text))


def ask_for_input():
    return input('> ')


def display_question_and_answers(question_label, answers):
    display_question(question_label)
    for i, answer in enumerate(answers, start=1):
        print('[{:d}] {}'.format(i, answer.label))


def display_question(label):
    print('\n' + label)


def get_valid_values(answers):
    return frozenset(map(str, range(1, len(answers) + 1)))

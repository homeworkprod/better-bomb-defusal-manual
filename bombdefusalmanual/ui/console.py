# -*- coding: utf-8 -*-

"""
Console user interface to ask questions and collect answers.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from .models import Answer, Question


def ask_question(question):
    """Present a question to the user and return the value of the
    selected answer.
    """
    while True:
        display_question_and_answers(question)
        valid_values = get_valid_values(question)
        selection_input = ask_for_input()
        if selection_input in valid_values:
            break

    selected_index = int(selection_input) - 1
    answer = question.answers[selected_index]
    return answer.value


def ask_for_input():
    return input('> ')


def display_question_and_answers(question):
    display_question(question)
    for i, answer in enumerate(question.answers, start=1):
        print('[{:d}] {}'.format(i, answer.label))


def display_question(question):
    print('\n' + question.label)


def get_valid_values(question):
    return frozenset(map(str, range(1, len(question.answers) + 1)))


def display_instruction(text):
    print('\n  => {} <=\n'.format(text))

# -*- coding: utf-8 -*-

"""
Console user interface to ask questions and collect answers.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from collections import namedtuple


Question = namedtuple('Question', 'label answers')
Answer = namedtuple('Answer', 'value label')


def ask_questions(questions):
    for question in questions:
        selected_answer = ask_question(question)
        print('You selected:', selected_answer.value)


def ask_question(question):
    while True:
        display_question_and_answers(question)
        valid_values = get_valid_values(question)
        selection_input = input('> ')
        if selection_input in valid_values:
            break

    selected_index = int(selection_input) - 1
    return question.answers[selected_index]


def display_question_and_answers(question):
    print('\n' + question.label)
    for i, answer in enumerate(question.answers, start=1):
        print('[{:d}] {}'.format(i, answer.label))


def get_valid_values(question):
    return frozenset(map(str, range(1, len(question.answers) + 1)))

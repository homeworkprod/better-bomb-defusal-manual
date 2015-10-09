# -*- coding: utf-8 -*-

"""
On the Subject of Passwords

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from string import ascii_lowercase

from ..ui.console import ask_for_input, display_instruction, display_question
from ..ui.models import Question


PASSWORDS = frozenset([
    'about', 'after', 'again', 'below', 'could',
    'every', 'first', 'found', 'great', 'house',
    'large', 'learn', 'never', 'other', 'place',
    'plant', 'point', 'right', 'small', 'sound',
    'spell', 'still', 'study', 'their', 'there',
    'these', 'thing', 'think', 'three', 'water',
    'where', 'which', 'world', 'would', 'write',
])


def ask_for_letters_and_match_passwords(position_index, passwords):
    letters = ask_for_letters_in_position(position_index)
    matches = list(get_passwords_matching_letters_in_position(passwords,
                                                              position_index,
                                                              letters))

    if not matches:
        display_instruction('No password matches!')
        return

    if len(matches) == 1:
        display_instruction(matches[0])
        return

    print()
    print('  Multiple candidates:')
    for match in matches:
        print('  ->', match)

    ask_for_letters_and_match_passwords(position_index + 1, matches)


def ask_for_letters_in_position(position_index):
    question_label = 'Which letters can be chosen at position {:d}?' \
                     .format(position_index + 1)
    question = Question(question_label, [])
    display_question(question)

    values = ask_for_input()
    return extract_letters(values)


def extract_letters(value):
    """Select and normalize ASCII letters, drop anything else."""
    lowercase_values = frozenset(map(str.lower, value))
    return lowercase_values.intersection(ascii_lowercase)


def get_passwords_matching_letters_in_position(passwords, position, letters):
    """Return all passwords that contain any of the given letters at the
    indicated position.
    """
    predicate = lambda password: password[position] in letters
    return filter(predicate, passwords)


def execute():
    ask_for_letters_and_match_passwords(0, PASSWORDS)

# -*- coding: utf-8 -*-

"""
On the Subject of Passwords

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from string import ascii_lowercase

from ..userinterface import Question, ask_for_input, display_instruction, \
    display_question


PASSWORDS = frozenset([
    'about', 'after', 'again', 'below', 'could',
    'every', 'first', 'found', 'great', 'house',
    'large', 'learn', 'never', 'other', 'place',
    'plant', 'point', 'right', 'small', 'sound',
    'spell', 'still', 'study', 'their', 'there',
    'these', 'thing', 'think', 'three', 'water',
    'where', 'which', 'world', 'would', 'write',
])


def ask_for_letters_in_first_position():
    letters = ask_for_letters_in_position('first')
    matches = list(get_passwords_starting_with(letters))

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


def ask_for_letters_in_position(position_label):
    question_label = 'Which letters are selectable in the {} position?' \
                     .format(position_label)
    question = Question(question_label, [])
    display_question(question)

    values = ask_for_input()
    return extract_letters(values)


def extract_letters(value):
    """Select and normalize ASCII letters, drop anything else."""
    lowercase_values = frozenset(map(str.lower, value))
    return lowercase_values.intersection(ascii_lowercase)


def get_passwords_starting_with(letters):
    """Return all passwords whose first letter is any of the given ones."""
    predicate = lambda word: word[0] in letters
    return filter(predicate, PASSWORDS)


def execute():
    ask_for_letters_in_first_position()

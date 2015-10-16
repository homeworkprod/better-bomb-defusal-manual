# -*- coding: utf-8 -*-

"""
On the Subject of Passwords

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from itertools import chain, groupby
from operator import itemgetter
from string import ascii_lowercase

from ..subjects.passwords import PASSWORDS
from ..templating import render_template


def group_passwords_by_first_letter():
    sorted_passwords = sorted(PASSWORDS)
    grouped = groupby(sorted_passwords, key=itemgetter(0))
    return [list(v) for k, v in grouped]


def get_letters_by_position():
    password_length = len(next(iter(PASSWORDS)))
    positions = range(password_length)

    return list(map(get_unique_letters_at_position, positions))


def get_unique_letters_at_position(position):
    return frozenset(map(itemgetter(position), PASSWORDS))


def get_unique_letters(letters_by_position):
    return frozenset(chain.from_iterable(letters_by_position))


def get_unused_letters():
    used_letters = frozenset(chain.from_iterable(PASSWORDS))
    return frozenset(ascii_lowercase).difference(used_letters)


def render_page():
    passwords_by_first_letter = group_passwords_by_first_letter()
    letters_by_position = get_letters_by_position()
    unique_letters = get_unique_letters(letters_by_position)
    unused_letters = get_unused_letters()

    return render_template('passwords',
                           passwords_by_first_letter=passwords_by_first_letter,
                           letters_by_position=letters_by_position,
                           unique_letters=unique_letters,
                           unused_letters=unused_letters)

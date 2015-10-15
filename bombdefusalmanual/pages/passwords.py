# -*- coding: utf-8 -*-

"""
On the Subject of Passwords

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from itertools import chain
from operator import itemgetter

from ..subjects.passwords import PASSWORDS
from ..templating import render_template


def get_letters_by_position():
    password_length = len(next(iter(PASSWORDS)))
    positions = range(password_length)

    return list(map(get_unique_letters_at_position, positions))


def get_unique_letters_at_position(position):
    return frozenset(map(itemgetter(position), PASSWORDS))


def get_unique_letters(letters_by_position):
    return frozenset(chain.from_iterable(letters_by_position))


def render_page():
    sorted_passwords = sorted(PASSWORDS)
    letters_by_position = get_letters_by_position()
    unique_letters = get_unique_letters(letters_by_position)

    return render_template('passwords',
                           passwords=sorted_passwords,
                           letters_by_position=letters_by_position,
                           unique_letters=unique_letters)

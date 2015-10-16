# -*- coding: utf-8 -*-

"""
On the Subject of Morse Code

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from ..subjects.morsecode import CHARACTERS_TO_MORSE_CODE, WORDS_TO_FREQUENCIES
from ..templating import render_template


def generate():
    for word in sorted(WORDS_TO_FREQUENCIES):
        codes = [CHARACTERS_TO_MORSE_CODE[char] for char in word]
        frequency = WORDS_TO_FREQUENCIES[word]
        yield codes, word, frequency


def render_page():
    codes_words_frequencies = list(generate())

    return render_template('morsecode',
                           codes_words_frequencies=codes_words_frequencies)

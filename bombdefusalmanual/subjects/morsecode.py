# -*- coding: utf-8 -*-

"""
On the Subject of Morse Code

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from ..ui.models import Question
from ..userinterface import ask_for_input, display_instruction, display_question


MORSE_CODE_SYMBOLS = frozenset('.-')


MORSE_CODE_TO_LETTERS = {
    '.-':   'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..':  'd',
    '.':    'e',
    '..-.': 'f',
    '--.':  'g',
    '....': 'h',
    '..':   'i',
    '.---': 'j',
    '-.-':  'k',
    '.-..': 'l',
    '--':   'm',
    '-.':   'n',
    '---':  'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.':  'r',
    '...':  's',
    '-':    't',
    '..-':  'u',
    '...-': 'v',
    '.--':  'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
}


def ask_for_and_translate_morse_code():
    while True:
        code = ask_for_morse_code()
        if not code:
            return

        letter = MORSE_CODE_TO_LETTERS.get(code)
        if letter:
            display_instruction('"{}" ({})'.format(letter, code))
        else:
            display_instruction('unknown ({})'.format(code))


def ask_for_morse_code():
    question = Question('Enter Morse code (`.` = short, `-` = long):', [])
    display_question(question)

    values = ask_for_input()
    return extract_morse_symbols(values)


def extract_morse_symbols(value):
    """Select only dots and dashes."""
    return ''.join(char for char in value if (char in MORSE_CODE_SYMBOLS))
    
    
def execute():
    ask_for_and_translate_morse_code()

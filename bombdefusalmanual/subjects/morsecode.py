# -*- coding: utf-8 -*-

"""
On the Subject of Morse Code

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""


MORSE_CODE_SYMBOLS = frozenset('.-')


MORSE_CODE_TO_CHARACTERS = {
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


CHARACTERS_TO_MORSE_CODE = {char: code for code, char
                            in MORSE_CODE_TO_CHARACTERS.items()}


WORDS_TO_FREQUENCIES = {
    'shell':  3505,
    'halls':  3515,
    'slick':  3522,
    'trick':  3532,
    'boxes':  3535,
    'leaks':  3542,
    'strobe': 3545,
    'bistro': 3552,
    'flick':  3555,
    'bombs':  3565,
    'break':  3572,
    'brick':  3575,
    'steak':  3582,
    'sting':  3592,
    'vector': 3595,
    'beats':  3600,
}


def ask_for_and_translate_morse_code(ui):
    while True:
        code = ask_for_morse_code(ui)
        if not code:
            return

        char = MORSE_CODE_TO_CHARACTERS.get(code)
        if char:
            ui.display_instruction('"{}" ({})'.format(char, code))
        else:
            ui.display_instruction('unknown ({})'.format(code))


def ask_for_morse_code(ui):
    question_label = 'Enter Morse code (`.` = short, `-` = long):'
    values = ui.ask_for_text(question_label)
    return extract_morse_symbols(values)


def extract_morse_symbols(value):
    """Select only dots and dashes."""
    return ''.join(char for char in value if (char in MORSE_CODE_SYMBOLS))
    
    
def execute(ui):
    ask_for_and_translate_morse_code(ui)

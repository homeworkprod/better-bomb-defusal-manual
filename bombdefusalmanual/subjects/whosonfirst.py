# -*- coding: utf-8 -*-

"""
On the Subject of Who's on First

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from enum import Enum

from ..userinterface import Question, ask_for_input, display_instruction, \
    display_question


ButtonPosition = Enum('ButtonPosition', [
    'top_left',
    'middle_left',
    'bottom_left',
    'top_right',
    'middle_right',
    'bottom_right',
])


DISPLAY_VALUES_TO_BUTTON_POSITIONS = {
    'YES':      ButtonPosition.middle_left,
    'FIRST':    ButtonPosition.top_right,
    'DISPLAY':  ButtonPosition.bottom_right,
    'OKAY':     ButtonPosition.top_right,
    'SAYS':     ButtonPosition.bottom_right,
    'NOTHING':  ButtonPosition.middle_left,
    '':         ButtonPosition.bottom_left,
    'BLANK':    ButtonPosition.middle_right,
    'NO':       ButtonPosition.bottom_right,
    'LED':      ButtonPosition.middle_left,
    'LEAD':     ButtonPosition.bottom_right,
    'READ':     ButtonPosition.middle_right,
    'RED':      ButtonPosition.middle_right,
    'REED':     ButtonPosition.bottom_left,
    'LEED':     ButtonPosition.bottom_left,
    'HOLD ON':  ButtonPosition.bottom_right,
    'YOU':      ButtonPosition.middle_right,
    'YOU ARE':  ButtonPosition.bottom_right,
    'YOUR':     ButtonPosition.middle_right,
    'YOU\'RE':  ButtonPosition.middle_right,
    'UR':       ButtonPosition.top_left,
    'THERE':    ButtonPosition.bottom_right,
    'THEY\'RE': ButtonPosition.bottom_left,
    'THEIR':    ButtonPosition.middle_right,
    'THEY ARE': ButtonPosition.middle_left,
    'SEE':      ButtonPosition.bottom_right,
    'C':        ButtonPosition.top_right,
    'CEE':      ButtonPosition.bottom_right,
}


BUTTON_LABELS_FORWARDS = {
    'READY':   ['YES', 'OKAY', 'WHAT', 'MIDDLE', 'LEFT', 'PRESS', 'RIGHT', 'BLANK', 'READY', 'NO', 'FIRST', 'UHHH', 'NOTHING', 'WAIT'],
    'FIRST':   ['LEFT', 'OKAY', 'YES', 'MIDDLE', 'NO', 'RIGHT', 'NOTHING', 'UHHH', 'WAIT', 'READY', 'BLANK', 'WHAT', 'PRESS', 'FIRST'],
    'NO':      ['BLANK', 'UHHH', 'WAIT', 'FIRST', 'WHAT', 'READY', 'RIGHT', 'YES', 'NOTHING', 'LEFT', 'PRESS', 'OKAY', 'NO', 'MIDDLE'],
    'BLANK':   ['WAIT', 'RIGHT', 'OKAY', 'MIDDLE', 'BLANK', 'PRESS', 'READY', 'NOTHING', 'NO', 'WHAT', 'LEFT', 'UHHH', 'YES', 'FIRST'],
    'NOTHING': ['UHHH', 'RIGHT', 'OKAY', 'MIDDLE', 'YES', 'BLANK', 'NO', 'PRESS', 'LEFT', 'WHAT', 'WAIT', 'FIRST', 'NOTHING', 'READY'],
    'YES':     ['OKAY', 'RIGHT', 'UHHH', 'MIDDLE', 'FIRST', 'WHAT', 'PRESS', 'READY', 'NOTHING', 'YES', 'LEFT', 'BLANK', 'NO', 'WAIT'],
    'WHAT':    ['UHHH', 'WHAT', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT'],
    'UHHH':    ['READY', 'NOTHING', 'LEFT', 'WHAT', 'OKEY', 'YES', 'RIGHT', 'NO', 'PRESS', 'BLANK', 'UHHH', 'MIDDLE', 'WAIT', 'FIRST'],
    'LEFT':    ['RIGHT', 'LEFT', 'FIRST', 'NO', 'MIDDLE', 'YES', 'BLANK', 'WHAT', 'UHHH', 'WAIT', 'PRESS', 'READY', 'OKAY', 'NOTHING'],
    'RIGHT':   ['YES', 'NOTHING', 'READY', 'PRESS', 'NO', 'WAIT', 'WHAT', 'RIGHT', 'MIDDLE', 'LEFT', 'UHHH', 'BLANK', 'OKAY', 'FIRST'],
    'MIDDLE':  ['BLANK', 'READY', 'OKAY', 'WHAT', 'NOTHING', 'PRESS', 'NO', 'WAIT', 'LEFT', 'MIDDLE', 'RIGHT', 'FIRST', 'UHHH', 'YES'],
    'OKAY':    ['MIDDLE', 'NO', 'FIRST', 'YES', 'UHHH', 'NOTHING', 'WAIT', 'OKAY', 'LEFT', 'READY', 'BLANK', 'PRESS', 'WHAT', 'RIGHT'],
    'WAIT':    ['UHHH', 'NO', 'BLANK', 'OKAY', 'YES', 'LEFT', 'FIRST', 'PRESS', 'WHAT', 'WAIT', 'NOTHING', 'READY', 'RIGHT', 'MIDDLE'],
    'PRESS':   ['RIGHT', 'MIDDLE', 'YES', 'READY', 'PRESS', 'OKAY', 'NOTHING', 'UHHH', 'BLANK', 'LEFT', 'FIRST', 'WHAT', 'NO', 'WAIT'],
    'YOU':     ['SURE', 'YOU ARE', 'YOUR', 'YOU\'RE', 'NEXT', 'UH HUH', 'UR', 'HOLD', 'WHAT?', 'YOU', 'UH UH', 'LIKE', 'DONE', 'U'],
    'YOU ARE': ['YOUR', 'NEXT', 'LIKE', 'UH HUH', 'WHAT?', 'DONE', 'UH UH', 'HOLD', 'YOU', 'U', 'YOU\'RE', 'SURE', 'UR', 'YOU ARE'],
    'YOUR':    ['UH UH', 'YOU ARE', 'UH HUH', 'YOUR', 'NEXT', 'UR', 'SURE', 'U', 'YOU\'RE', 'YOU', 'WHAT?', 'HOLD', 'LIKE', 'DONE'],
    'YOU\'RE': ['YOU', 'YOU\'RE', 'UR', 'NEXT', 'UH UH', 'YOU ARE', 'U', 'YOUR', 'WHAT?', 'UH HUH', 'SURE', 'DONE', 'LIKE', 'HOLD'],
    'UR':      ['DONE', 'U', 'UR', 'UH HUH', 'WHAT?', 'SURE', 'YOUR', 'HOLD', 'YOU\'RE', 'LIKE', 'NEXT', 'UH UH', 'YOU ARE', 'YOU'],
    'U':       ['UH HUH', 'SURE', 'NEXT', 'WHAT?', 'YOU\'RE', 'UR', 'UH UH', 'DONE', 'U', 'YOU', 'LIKE', 'HOLD', 'YOU ARE', 'YOUR'],
    'UH HUH':  ['UH HUH', 'YOUR', 'YOU ARE', 'YOU', 'DONE', 'HOLD', 'UH UH', 'NEXT', 'SURE', 'LIKE', 'YOU\'RE', 'UR', 'U', 'WHAT?'],
    'UH UH':   ['UR', 'U', 'YOU ARE', 'YOU\'RE', 'NEXT', 'UH UH', 'DONE', 'YOU', 'UH HUH', 'LIKE', 'YOUR', 'SURE', 'HOLD', 'WHAT?'],
    'WHAT?':   ['YOU', 'HOLD', 'YOU\'RE', 'YOUR', 'U', 'DONE', 'UH UH', 'LIKE', 'YOU ARE', 'UH HUH', 'UR', 'NEXT', 'WHAT?', 'SURE'],
    'DONE':    ['SURE', 'UH HUH', 'NEXT', 'WHAT?', 'YOUR', 'UR', 'YOU\'RE', 'HOLD', 'LIKE', 'YOU', 'U', 'YOU ARE', 'UH UH', 'DONE'],
    'NEXT':    ['WHAT?', 'UH HUH', 'UH UH', 'YOUR', 'HOLD', 'SURE', 'NEXT', 'LIKE', 'DONE', 'YOU ARE', 'UR', 'YOU\'RE', 'U', 'YOU'],
    'HOLD':    ['YOU ARE', 'U', 'DONE', 'UH UH', 'YOU', 'UR', 'SURE', 'WHAT?', 'YOU\'RE', 'NEXT', 'HOLD', 'UH HUH', 'YOUR', 'LIKE'],
    'SURE':    ['YOU ARE', 'DONE', 'LIKE', 'YOU\'RE', 'YOU', 'HOLD', 'UH HUH', 'UR', 'SURE', 'U', 'WHAT?', 'NEXT', 'YOUR', 'UH UH'],
    'LIKE':    ['YOU\'RE', 'NEXT', 'U', 'UR', 'HOLD', 'DONE', 'UH UH', 'WHAT?', 'UH HUH', 'YOU', 'LIKE', 'SURE', 'YOU ARE', 'YOUR'],
}


def step1():
    """Ask for the word on the display and return the position of the
    button to check out next.
    """
    question = Question('What does the display say?', [])
    display_question(question)

    display_word = normalize(ask_for_input())
    return DISPLAY_VALUES_TO_BUTTON_POSITIONS.get(display_word)


def step2(button_position):
    """Ask for the label of the button at that position and list the
    potential labels of the button to push next, ordered by priority.
    """
    question_label = 'What does the button in the {} say?' \
                      .format(button_position.name.replace('_', ' ').upper())
    question = Question(question_label, [])
    display_question(question)

    button_label = normalize(ask_for_input())
    return BUTTON_LABELS_FORWARDS.get(button_label)


def normalize(value):
    return value.strip().upper()


def display_button_labels(labels):
    print()
    print('  Push the first button that appears in this list:')
    for label in labels:
        print('  ->', label)


def execute():
    button_position = step1()
    if not button_position:
        display_instruction('Unknown display word!')

    button_labels = step2(button_position)
    if not button_position:
        display_instruction('Unknown button label!')

    display_button_labels(button_labels)

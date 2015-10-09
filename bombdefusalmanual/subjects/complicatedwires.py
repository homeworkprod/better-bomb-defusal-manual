# -*- coding: utf-8 -*-

"""
On the Subject of Complicated Wires

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from enum import Enum

from ..ui.models import Answer


LED = Enum('LED', 'on off')
Red = Enum('Red', 'yes no')
Blue = Enum('Blue', 'yes no')
Star = Enum('Star', 'yes no')

InstructionLetter = Enum('InstructionLetter', 'C D S P B')


INSTRUCTIONS = {
    InstructionLetter.C: 'Cut the wire.',
    InstructionLetter.D: 'Do not cut the wire.',
    InstructionLetter.S: 'Cut the wire if the last digit of the serial number is even.',
    InstructionLetter.P: 'Cut the wire if the bomb has a parallel port.',
    InstructionLetter.B: 'Cut the wire if the bomb has two or more batteries.',
}


COMBINATORICS = {
    (LED.off, Red.no , Blue.no , Star.no ): InstructionLetter.C,
    (LED.off, Red.no , Blue.no , Star.yes): InstructionLetter.C,
    (LED.off, Red.no , Blue.yes, Star.no ): InstructionLetter.S,
    (LED.off, Red.no , Blue.yes, Star.yes): InstructionLetter.D,
    (LED.off, Red.yes, Blue.no , Star.no ): InstructionLetter.S,
    (LED.off, Red.yes, Blue.no , Star.yes): InstructionLetter.C,
    (LED.off, Red.yes, Blue.yes, Star.no ): InstructionLetter.S,
    (LED.off, Red.yes, Blue.yes, Star.yes): InstructionLetter.P,
    (LED.on , Red.no , Blue.no , Star.no ): InstructionLetter.D,
    (LED.on , Red.no , Blue.no , Star.yes): InstructionLetter.B,
    (LED.on , Red.no , Blue.yes, Star.no ): InstructionLetter.P,
    (LED.on , Red.no , Blue.yes, Star.yes): InstructionLetter.P,
    (LED.on , Red.yes, Blue.no , Star.no ): InstructionLetter.B,
    (LED.on , Red.yes, Blue.no , Star.yes): InstructionLetter.B,
    (LED.on , Red.yes, Blue.yes, Star.no ): InstructionLetter.S,
    (LED.on , Red.yes, Blue.yes, Star.yes): InstructionLetter.D,
}


QUESTIONS_AND_ANSWERS = [
    (
        'Is the LED above the wire on?',
        [
            Answer(LED.on, 'yes'),
            Answer(LED.off, 'no'),
        ],
    ),
    (
        'Does the wire have red coloring?',
        [
            Answer(Red.yes, 'yes'),
            Answer(Red.no, 'no'),
        ],
    ),
    (
        'Does the wire have blue coloring?',
        [
            Answer(Blue.yes, 'yes'),
            Answer(Blue.no, 'no'),
        ],
    ),
    (
        'Is a star symbol below the wire?',
        [
            Answer(Star.yes, 'yes'),
            Answer(Star.no, 'no'),
        ],
    ),
]


def ask_questions(ui):
    for question_label, answers in QUESTIONS_AND_ANSWERS:
        yield ui.ask_for_choice(question_label, answers)


def get_instruction(answer_values):
    instruction_letter = COMBINATORICS[answer_values]
    return INSTRUCTIONS[instruction_letter]


def execute(ui):
    answer_values = tuple(ask_questions(ui))
    instruction = get_instruction(answer_values)
    ui.display_instruction(instruction)

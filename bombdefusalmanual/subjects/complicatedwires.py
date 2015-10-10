# -*- coding: utf-8 -*-

"""
On the Subject of Complicated Wires

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from enum import Enum

from ..ui.models import Choice


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


QUESTIONS_AND_CHOICES = [
    (
        'Is the LED above the wire on?',
        [
            Choice(LED.on, 'yes'),
            Choice(LED.off, 'no'),
        ],
    ),
    (
        'Does the wire have red coloring?',
        [
            Choice(Red.yes, 'yes'),
            Choice(Red.no, 'no'),
        ],
    ),
    (
        'Does the wire have blue coloring?',
        [
            Choice(Blue.yes, 'yes'),
            Choice(Blue.no, 'no'),
        ],
    ),
    (
        'Is a star symbol below the wire?',
        [
            Choice(Star.yes, 'yes'),
            Choice(Star.no, 'no'),
        ],
    ),
]


def ask_questions(ui):
    for question_label, choices in QUESTIONS_AND_CHOICES:
        yield ui.ask_for_choice(question_label, choices)


def get_instruction(choice_values):
    instruction_letter = COMBINATORICS[choice_values]
    return INSTRUCTIONS[instruction_letter]


def execute(ui):
    while True:
        choice_values = tuple(ask_questions(ui))
        instruction = get_instruction(choice_values)
        ui.display_instruction(instruction)

# -*- coding: utf-8 -*-

"""
On the Subject of The Button

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from enum import Enum

from ..userinterface import Answer, Question, ask_question, display_instruction


ButtonColor = Enum('ButtonColor', 'blue white yellow red other')
ButtonLabel = Enum('ButtonLabel', 'Abort Detonate Hold other')
BatteryCount = Enum('BatteryCount', 'one_or_less more_than_one more_than_two')
IndicatorLabel = Enum('IndicatorLabel', 'CAR FRK')
Exists = Enum('Exists', 'yes no')
StripColor = Enum('StripColor', 'blue yellow other')


ButtonRelease = Enum('ButtonRelease', [
    'immediately',
    'when_countdown_timer_contains_digit_1',
    'when_countdown_timer_contains_digit_4',
    'when_countdown_timer_contains_digit_5',
])


def get_instruction():
    button_color = ask_for_button_color()
    button_label = ask_for_button_label()

    # Rule #1
    if (button_color is ButtonColor.blue) and (button_label is ButtonLabel.Abort):
        return get_button_release_instruction()

    battery_count = ask_for_battery_count()

    # Rule #2
    if (battery_count is not BatteryCount.one_or_less) and (button_label is ButtonLabel.Detonate):
        return get_button_release_instruction()

    lit_indicator_label = ask_for_lit_indicator_label(IndicatorLabel.CAR)

    # Rule #3
    if (button_color is ButtonColor.white) and (lit_indicator_label is IndicatorLabel.CAR):
        return get_button_release_instruction()

    lit_indicator_label = ask_for_lit_indicator_label(IndicatorLabel.FRK)

    # Rule #4
    if (battery_count is BatteryCount.more_than_two) and (lit_indicator_label is IndicatorLabel.FRK):
        return Release.immediately

    # Rule #5
    if (button_color is ButtonColor.yellow):
        return get_button_release_instruction()

    # Rule #6
    if (button_color is ButtonColor.red) and (button_label is ButtonLabel.Hold):
        return Release.immediately

    # Rule #7
    return get_button_release_instruction()


def ask_for_button_color():
    answers = [Answer(member, member.name) for member in ButtonColor]
    return ask_for_value('Which color does the button have?', answers)


def ask_for_button_label():
    answers = list(generate_button_label_answers())
    return ask_for_value('What does the button say?', answers)


def generate_button_label_answers():
    for member in ButtonLabel:
        label = member.name
        if member is not ButtonLabel.other:
            label = '"{}"'.format(label)
        yield Answer(member, label)


def ask_for_battery_count():
    answers = [Answer(member, member.name) for member in BatteryCount]
    return ask_for_value('How many batteries are there?', answers)


def ask_for_lit_indicator_label(indicator_label):
    question_label = 'Is there a lit indicator labeled "{}"?' \
                     .format(indicator_label.name)
    answers = [Answer(member, member.name) for member in Exists]
    value = ask_for_value(question_label, answers)
    return indicator_label.value if value is Exists.yes else None


def get_button_release_instruction():
    mapping = {
        StripColor.blue: ButtonRelease.when_countdown_timer_contains_digit_4,
        StripColor.yellow: ButtonRelease.when_countdown_timer_contains_digit_5,
    }
    otherwise = ButtonRelease.when_countdown_timer_contains_digit_1

    strip_color = ask_for_strip_color()
    return mapping.get(strip_color, otherwise)


def ask_for_strip_color():
    answers = [Answer(member, member.name) for member in StripColor]
    return ask_for_value(
        'Which color does the strip to the right of the button have?',
        answers)


def ask_for_value(question_label, answers):
    question = Question(question_label, answers)
    return ask_question(question).value


def execute():
    button_release = get_instruction()
    display_instruction('Press button. Release {}.'.format(button_release))

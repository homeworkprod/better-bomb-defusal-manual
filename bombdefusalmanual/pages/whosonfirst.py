# -*- coding: utf-8 -*-

"""
On the Subject of Who's on First

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from ..subjects.whosonfirst import ButtonPosition, \
    DISPLAY_VALUES_TO_BUTTON_POSITIONS
from ..templating import render_template


BUTTOM_POSITION_SYMBOLS = {
    ButtonPosition.top_left:     '↖',
    ButtonPosition.middle_left:  '←',
    ButtonPosition.bottom_left:  '↙',
    ButtonPosition.top_right:    '↗',
    ButtonPosition.middle_right: '→',
    ButtonPosition.bottom_right: '↘',
}


def render_page():
    display_values_to_button_positions = {
        display_value: BUTTOM_POSITION_SYMBOLS[button_position]
        for display_value, button_position
        in DISPLAY_VALUES_TO_BUTTON_POSITIONS.items()}

    return render_template(
        'whosonfirst',
        display_values_to_button_positions=display_values_to_button_positions)

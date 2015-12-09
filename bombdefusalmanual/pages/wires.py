# -*- coding: utf-8 -*-

"""
On the Subject of Wires

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from ..templating import render_template


def render_page():
    custom_filters = {'color': render_color}

    return render_template('wires', custom_filters=custom_filters)


def render_color(name):
    return '<span class="color-{0}">{0}</span>'.format(name)

# -*- coding: utf-8 -*-

"""
Models to exchange information with a user.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from collections import namedtuple


Question = namedtuple('Question', 'label answers')


Answer = namedtuple('Answer', 'value label')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render custom manual pages for Better Bomb Defusal Manual

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from bombdefusalmanual.pages.passwords import render_page


if __name__ == '__main__':
    page = render_page()
    print(page)

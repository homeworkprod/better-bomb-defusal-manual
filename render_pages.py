#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render custom manual pages for Better Bomb Defusal Manual

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from pathlib import Path
import sys

from bombdefusalmanual.pages import morsecode
from bombdefusalmanual.pages import passwords
from bombdefusalmanual.pages import whosonfirst


PAGE_MODULES = [
    morsecode,
    passwords,
    whosonfirst,
]

BUILD_PATH = Path('./build')


def create_build_path(path):
    try:
        path.mkdir()
    except FileExistsError:
        sys.stderr.write(
            'Build path already exists, not generating pages: {}\n' \
                .format(path))
        sys.exit(1)


def render_pages(path, page_modules):
    for module in page_modules:
        name = module.__name__.rpartition('.')[-1]
        output_filename = name + '.html'

        html = module.render_page()

        path.joinpath(output_filename).write_text(html, 'utf-8')


if __name__ == '__main__':
    create_build_path(BUILD_PATH)
    render_pages(BUILD_PATH, PAGE_MODULES)

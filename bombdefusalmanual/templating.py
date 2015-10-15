# -*- coding: utf-8 -*-

"""
Template loading and rendering

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from jinja2 import Environment, PackageLoader, StrictUndefined


FILENAME_EXTENSION = '.html'

LOADER = PackageLoader('bombdefusalmanual.pages')
ENV = Environment(loader=LOADER, undefined=StrictUndefined)


def render_template(name, **context):
    template = load_template(name)
    return template.render(**context)


def load_template(name):
    filename = name + FILENAME_EXTENSION
    return ENV.get_template(filename)

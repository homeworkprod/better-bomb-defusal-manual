# -*- coding: utf-8 -*-

"""
Template loading and rendering

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from jinja2 import Environment, PackageLoader, StrictUndefined


FILENAME_EXTENSION = '.html'

LOADER = PackageLoader('bombdefusalmanual.pages')


def render_template(name, *, custom_filters=None, **context):
    template = load_template(name, custom_filters=custom_filters)

    return template.render(**context)


def load_template(name, *, custom_filters=None):
    env = create_environment(custom_filters=custom_filters)

    filename = name + FILENAME_EXTENSION

    return env.get_template(filename)


def create_environment(*, custom_filters=None):
    env = Environment(loader=LOADER, undefined=StrictUndefined)

    if custom_filters is not None:
        env.filters.update(custom_filters)

    return env

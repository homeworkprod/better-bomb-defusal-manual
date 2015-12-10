# -*- coding: utf-8 -*-

"""
Template loading and rendering

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from jinja2 import Environment, evalcontextfilter, Markup, PackageLoader, \
    StrictUndefined


FILENAME_EXTENSION = '.html'

LOADER = PackageLoader('bombdefusalmanual.pages')


def render_template(name, **context):
    template = load_template(name)

    return template.render(**context)


def load_template(name):
    env = create_environment()

    filename = name + FILENAME_EXTENSION

    return env.get_template(filename)


def create_environment():
    env = Environment(
        autoescape=True,
        loader=LOADER,
        undefined=StrictUndefined)

    env.filters['color'] = render_color

    return env


@evalcontextfilter
def render_color(eval_ctx, name):
    html = '<span class="color-{0}">{0}</span>'.format(name)
    return Markup(html) if eval_ctx.autoescape else html

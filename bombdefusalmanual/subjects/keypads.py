# -*- coding: utf-8 -*-

"""
On the Subject of Keypads

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from collections import Counter
from itertools import chain, zip_longest
from tkinter import ttk
from tkinter import E, N, S, W


COPYRIGHT_SIGN                                   = '\u00A9'
PILCROW_SIGN                                     = '\u00B6'
INVERTED_QUESTION_MARK                           = '\u00BF'
LATIN_SMALL_LETTER_LAMBDA_WITH_STROKE            = '\u019B'
GREEK_CAPITAL_LETTER_PSI                         = '\u03A8'
GREEK_CAPITAL_LETTER_OMEGA                       = '\u03A9'
GREEK_KAI_SYMBOL                                 = '\u03D7'
GREEK_LETTER_ARCHAIC_KOPPA                       = '\u03D8'
GREEK_LETTER_KOPPA                               = '\u03DE'
COPTIC_CAPITAL_LETTER_SHIMA                      = '\u03EC'
GREEK_CAPITAL_DOTTED_LUNATE_SIGMASYMBOL          = '\u03FE'
GREEK_CAPITAL_REVERSED_DOTTED_LUNATESIGMA_SYMBOL = '\u03FF'
CYRILLIC_CAPITAL_LETTER_YAT                      = '\u0462'
CYRILLIC_CAPITAL_LETTER_LITTLE_YUS               = '\u0466'
CYRILLIC_CAPITAL_LETTER_IOTIFIED_BIG_YUS         = '\u046C'
CYRILLIC_CAPITAL_LETTER_KSI                      = '\u046E'
CYRILLIC_CAPITAL_LETTER_OMEGA_WITH_TITLO         = '\u047C'
CYRILLIC_THOUSANDS_SIGN                          = '\u0482'
CYRILLIC_CAPITAL_LETTER_SHORT_I_WITH_TAIL        = '\u048A'
CYRILLIC_CAPITAL_LETTER_ZHE_WITH_DESCENDER       = '\u0496'
CYRILLIC_CAPITAL_LETTER_ABKHASIAN_HA             = '\u04A8'
CYRILLIC_SMALL_LIGATURE_A_IE                     = '\u04D5'
CYRILLIC_CAPITAL_LETTER_E_WITH_DIAERESIS         = '\u04EC'
CYRILLIC_CAPITAL_LETTER_KOMI_DZJE                = '\u0506'
ARABIC_LETTER_TEH_WITH_RING                      = '\u067C'
BLACK_STAR                                       = '\u2605'
WHITE_STAR                                       = '\u2606'


SYMBOLS = frozenset([
    COPYRIGHT_SIGN,
    PILCROW_SIGN,
    INVERTED_QUESTION_MARK,
    LATIN_SMALL_LETTER_LAMBDA_WITH_STROKE,
    GREEK_CAPITAL_LETTER_PSI,
    GREEK_CAPITAL_LETTER_OMEGA,
    GREEK_KAI_SYMBOL,
    GREEK_LETTER_ARCHAIC_KOPPA,
    GREEK_LETTER_KOPPA,
    COPTIC_CAPITAL_LETTER_SHIMA,
    GREEK_CAPITAL_DOTTED_LUNATE_SIGMASYMBOL,
    GREEK_CAPITAL_REVERSED_DOTTED_LUNATESIGMA_SYMBOL,
    CYRILLIC_CAPITAL_LETTER_YAT,
    CYRILLIC_CAPITAL_LETTER_LITTLE_YUS,
    CYRILLIC_CAPITAL_LETTER_IOTIFIED_BIG_YUS,
    CYRILLIC_CAPITAL_LETTER_KSI,
    CYRILLIC_CAPITAL_LETTER_OMEGA_WITH_TITLO,
    CYRILLIC_THOUSANDS_SIGN,
    CYRILLIC_CAPITAL_LETTER_SHORT_I_WITH_TAIL,
    CYRILLIC_CAPITAL_LETTER_ZHE_WITH_DESCENDER,
    CYRILLIC_CAPITAL_LETTER_ABKHASIAN_HA,
    CYRILLIC_SMALL_LIGATURE_A_IE,
    CYRILLIC_CAPITAL_LETTER_E_WITH_DIAERESIS,
    CYRILLIC_CAPITAL_LETTER_KOMI_DZJE,
    ARABIC_LETTER_TEH_WITH_RING,
    BLACK_STAR,
    WHITE_STAR,
])


COLUMNS = [
    [
        # column 1
        GREEK_LETTER_ARCHAIC_KOPPA,
        CYRILLIC_CAPITAL_LETTER_LITTLE_YUS,
        LATIN_SMALL_LETTER_LAMBDA_WITH_STROKE,
        GREEK_LETTER_KOPPA,
        CYRILLIC_CAPITAL_LETTER_IOTIFIED_BIG_YUS,
        GREEK_KAI_SYMBOL,
        GREEK_CAPITAL_REVERSED_DOTTED_LUNATESIGMA_SYMBOL,
    ],
    [
        # column 2
        CYRILLIC_CAPITAL_LETTER_E_WITH_DIAERESIS,
        GREEK_LETTER_ARCHAIC_KOPPA,
        GREEK_CAPITAL_REVERSED_DOTTED_LUNATESIGMA_SYMBOL,
        CYRILLIC_CAPITAL_LETTER_ABKHASIAN_HA,
        WHITE_STAR,
        GREEK_KAI_SYMBOL,
        INVERTED_QUESTION_MARK,
    ],
    [
        # column 3
        COPYRIGHT_SIGN,
        CYRILLIC_CAPITAL_LETTER_OMEGA_WITH_TITLO,
        CYRILLIC_CAPITAL_LETTER_ABKHASIAN_HA,
        CYRILLIC_CAPITAL_LETTER_ZHE_WITH_DESCENDER,
        CYRILLIC_CAPITAL_LETTER_KOMI_DZJE,
        LATIN_SMALL_LETTER_LAMBDA_WITH_STROKE,
        WHITE_STAR,
    ],
    [
        # column 4
        COPTIC_CAPITAL_LETTER_SHIMA,
        PILCROW_SIGN,
        CYRILLIC_CAPITAL_LETTER_YAT,
        CYRILLIC_CAPITAL_LETTER_IOTIFIED_BIG_YUS,
        CYRILLIC_CAPITAL_LETTER_ZHE_WITH_DESCENDER,
        INVERTED_QUESTION_MARK,
        ARABIC_LETTER_TEH_WITH_RING,
    ],
    [
        # column 5
        GREEK_CAPITAL_LETTER_PSI,
        ARABIC_LETTER_TEH_WITH_RING,
        CYRILLIC_CAPITAL_LETTER_YAT,
        GREEK_CAPITAL_DOTTED_LUNATE_SIGMASYMBOL,
        PILCROW_SIGN,
        CYRILLIC_CAPITAL_LETTER_KSI,
        BLACK_STAR,
    ],
    [
        # column 6
        COPTIC_CAPITAL_LETTER_SHIMA,
        CYRILLIC_CAPITAL_LETTER_E_WITH_DIAERESIS,
        CYRILLIC_THOUSANDS_SIGN,
        CYRILLIC_SMALL_LIGATURE_A_IE,
        GREEK_CAPITAL_LETTER_PSI,
        CYRILLIC_CAPITAL_LETTER_SHORT_I_WITH_TAIL,
        GREEK_CAPITAL_LETTER_OMEGA,
    ],
]


SYMBOL_COUNTS = Counter(chain.from_iterable(COLUMNS))


def is_symbol_unique(symbol):
    """Return `True` if the symbol appears only once."""
    return SYMBOL_COUNTS[symbol] == 1


class KeypadFrame(ttk.Frame):

    def __init__(self, parent, symbols):
        super().__init__(parent)

        self.parent = parent

        button_style = create_style('lightgray')
        button_style_unique = create_style('lightgreen')
        ordered_symbols = sorted(symbols)
        chunked_ordered_symbols = split_into_chunks(ordered_symbols, 9)

        for row, chunk in enumerate(chunked_ordered_symbols):
            for column, symbol in enumerate(chunk):
                if symbol is None:
                    continue

                button = SymbolButton(self, text=symbol, value=symbol)
                style = button_style_unique if is_symbol_unique(symbol) else button_style
                button.configure(style=style)
                button.grid(column=column, row=row, sticky=(N, W, E, S))
                self.columnconfigure(column, weight=1)
            self.rowconfigure(row, weight=1)


class SymbolButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        self.value = kwargs.pop('value')
        super().__init__(*args, **kwargs)


def create_style(background_color_name):
    style_name = '{}.TButton'.format(background_color_name)

    style = ttk.Style()
    style.configure(style_name, background=background_color_name)

    return style_name


def split_into_chunks(iterable, chunk_length):
    args = [iter(iterable)] * chunk_length
    return zip_longest(*args)


def display_symbols(ui):
    def create_frame(parent):
        return KeypadFrame(parent, SYMBOLS)

    ui.run_frame(create_frame)


def execute(ui):
    while True:
        display_symbols(ui)

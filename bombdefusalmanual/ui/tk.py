# -*- coding: utf-8 -*-

"""
Graphical user interface to ask questions and collect answers.

Based on Tk/Tkinter.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

import sys
import tkinter as tk
from tkinter import ttk
from tkinter import E, N, S, W

from .console import ConsoleUI


class TkGUI(ConsoleUI):

    def ask_for_text(self, question_label):
        gui = TextGUI(question_label)
        gui.mainloop()
        return gui.text.get()

    def ask_for_choice(self, question_label, choices, *, color_map=None):
        gui = ChoiceGUI(question_label, choices, color_map)
        gui.mainloop()
        return gui.selected_choice_value


class BaseGUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.bind('<Escape>', self.exit)

    def exit(self, event):
        sys.exit()


class TextGUI(BaseGUI):

    def __init__(self, question_label):
        BaseGUI.__init__(self)

        self.add_question_label(question_label)
        self.add_text_entry()

    def add_question_label(self, question_label):
        label = ttk.Label(self, text=question_label)
        label.grid(row=0, sticky=(N, W, E, S))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def add_text_entry(self):
        self.text = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.text)
        entry.grid(row=1, sticky=(N, W, E, S))
        entry.bind('<Return>', self.submit)
        entry.focus()
        self.rowconfigure(1, weight=1)

    def submit(self, event):
        self.destroy()


class ChoiceGUI(BaseGUI):

    def __init__(self, question_label, choices, color_map):
        BaseGUI.__init__(self)

        self.selected_choice_value = None

        self.add_question_label(question_label)
        self.add_choice_buttons(choices, color_map)

    def add_question_label(self, question_label):
        label = ttk.Label(self, text=question_label)
        label.grid(row=0, sticky=(N, W, E, S))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def add_choice_buttons(self, choices, color_map):
        if color_map is None:
            color_map = {}

        for row, choice in enumerate(choices, start=1):
            button = ChoiceButton(self, text=choice.label, value=choice.value)
            button.grid(row=row, sticky=(N, W, E, S))
            self.rowconfigure(row, weight=1)

            color = color_map.get(choice.value)
            if color:
                button.configure(style=create_style(color))

    def set_selected_choice_and_close(self, selected_choice_value):
        self.selected_choice_value = selected_choice_value
        self.destroy()


def create_style(color_name):
    style_name = '{}.TButton'.format(color_name)

    style = ttk.Style()
    style.configure(style_name, background=color_name)

    return style_name


class ChoiceButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        self.value = kwargs.pop('value')
        ttk.Button.__init__(self, *args, **kwargs)
        self.configure(command=self.set_selected_choice)

    def set_selected_choice(self):
        self.master.set_selected_choice_and_close(self.value)

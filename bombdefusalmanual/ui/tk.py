# -*- coding: utf-8 -*-

"""
Graphical user interface to ask questions and collect answers.

Based on Tk/Tkinter.

:Copyright: 2015 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from .console import ConsoleUI

import tkinter as tk
from tkinter import ttk
from tkinter import E, N, S, W


class TkGUI(ConsoleUI):

    def ask_for_choice(self, question_label, choices):
        gui = ChoiceGUI(question_label, choices)
        gui.mainloop()
        return gui.selected_choice_value


class ChoiceGUI(tk.Tk):

    def __init__(self, question_label, choices):
        tk.Tk.__init__(self)

        self.selected_choice_value = None

        self.add_question_label(question_label)
        self.add_choice_buttons(choices)

    def add_question_label(self, question_label):
        label = ttk.Label(self, text=question_label)
        label.grid(row=0, sticky=(N, W, E, S))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def add_choice_buttons(self, choices):
        for row, choice in enumerate(choices, start=1):
            button = ChoiceButton(self, text=choice.label, value=choice.value)
            button.grid(row=row, sticky=(N, W, E, S))
            self.rowconfigure(row, weight=1)

    def set_selected_choice_and_close(self, selected_choice_value):
        self.selected_choice_value = selected_choice_value
        self.destroy()



class ChoiceButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        self.value = kwargs.pop('value')
        ttk.Button.__init__(self, *args, **kwargs)
        self.configure(command=self.set_selected_choice)

    def set_selected_choice(self):
        self.master.set_selected_choice_and_close(self.value)

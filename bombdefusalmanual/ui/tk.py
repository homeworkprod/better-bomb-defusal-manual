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

    def ask_for_choice(self, question_label, answers):
        gui = ChoiceGUI(question_label, answers)
        gui.mainloop()
        return gui.selected_answer_value


class ChoiceGUI(tk.Tk):

    def __init__(self, question_label, answers):
        tk.Tk.__init__(self)

        self.selected_answer_value = None

        self.add_question_label(question_label)
        self.add_answer_buttons(answers)

    def add_question_label(self, question_label):
        label = ttk.Label(self, text=question_label)
        label.grid(row=0, sticky=(N, W, E, S))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def add_answer_buttons(self, answers):
        for row, answer in enumerate(answers, start=1):
            button = ChoiceButton(self, text=answer.label, value=answer.value)
            button.grid(row=row, sticky=(N, W, E, S))
            self.rowconfigure(row, weight=1)

    def set_selected_answer_and_close(self, selected_answer_value):
        self.selected_answer_value = selected_answer_value
        self.destroy()



class ChoiceButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        self.value = kwargs.pop('value')
        ttk.Button.__init__(self, *args, **kwargs)
        self.configure(command=self.set_selected_answer)

    def set_selected_answer(self):
        self.master.set_selected_answer_and_close(self.value)

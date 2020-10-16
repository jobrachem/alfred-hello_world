# -*- coding: utf-8 -*-
from alfred3 import Experiment
from alfred3.page import Page

import alfred3.section as sec
import alfred3.element as elm


class HelloWorld(Page):
    title = "Hello, world!"

    def on_exp_access(self):
        self += elm.TextEntryElement("Please enter some text.")


class MainSection(sec.SegmentedSection):
    def on_exp_access(self):
        self += HelloWorld()


def generate_experiment(self, config):

    exp = Experiment(config=config)
    exp += MainSection()

    return exp

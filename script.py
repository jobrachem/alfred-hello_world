# -*- coding: utf-8 -*-
from alfred3 import Experiment
from alfred3.page import Page

import alfred3.section as sec
import alfred3.element as elm


class HelloWorld(Page):
    def on_showing(self):
        hello_text = elm.TextEntryElement("Please enter some text.")
        self.append(hello_text)


def generate_experiment(self, config):
    exp = Experiment(config=config)

    hello_world = HelloWorld(title="Hello, world!")

    main = sec.Section()
    main.append(hello_world)

    exp.append(main)
    return exp

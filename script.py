# -*- coding: utf-8 -*-
import alfred.element as elm
import alfred.section as sec
from alfred import Experiment
from alfred.page import Page


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

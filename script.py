# -*- coding:utf-8 -*-

from alfred.page import WebCompositePage
from alfred import Experiment, run


def generate_experiment():
    # Create content
    hello_world = WebCompositePage(title="Hello, world!")

    # Create experiment
    exp = Experiment()
    exp.append(hello_world)
    return exp


run(generate_experiment)

# -*- coding:utf-8 -*-

from alfred.page import WebCompositePage
from alfred import Experiment

EXP_TYPE = "web"
EXP_NAME = "template"
EXP_VERSION = "0.1"
EXP_AUTHOR_MAIL = "your@email.com"

class Script(object):

    def generate_experiment(self):
        
        page01 = WebCompositePage(title="Hello, world!")

        exp = Experiment(EXP_TYPE, EXP_NAME, EXP_VERSION, EXP_AUTHOR_MAIL)
        exp.page_controller.append_items(page01)

        return exp


generate_experiment = Script().generate_experiment

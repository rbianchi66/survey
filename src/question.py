#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Question(object):
    def __init__(self, id = 0, name = "New Question"):
        super(Question, self).__init__()
        self.id = id
        self.name = name
        self.answers = {}
        
    def add(self, a):
        self.answers[a.id] = a
        return a
        
class RadioQuestion(object):
    def __init__(self, id = 0, name = "New Question"):
        super(RadioQuestion, self).__init__(id, name)

class CheckboxQuestion(object):
    def __init__(self, id = 0, name = "New Question"):
        super(CheckboxQuestion, self).__init__(id, name)

class OpenQuestion(object):
    def __init__(self, id = 0, name = "New Question"):
        super(OpenQuestion, self).__init__(id, name)

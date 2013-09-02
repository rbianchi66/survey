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
        

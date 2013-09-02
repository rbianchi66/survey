#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Answer(object):
    def __init__(self, id = 0, value = "New Answer"):
        super(Answer, self).__init__()
        self.id = id
        self.value = value
        self.selected = False
        self.editable = False
        

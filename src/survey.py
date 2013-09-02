#!/usr/bin/env python
#-*- coding: utf-8 -*-

## @package survey
#  Data model package which manage the survey data structures.
#
import jsonpickle

## The Survey base class.
#
class Survey(object):
    def __init__(self, name = "New Survey"):
        super(Survey, self).__init__()
        self.name = name
        self.questions = {}
        
    def add(self, q):
        self.questions[q.id] = q
        return q
    
## Save a Survey object into a file.
#
def saveSurvey(survey, filename):
    f = open(filename, "w")
    if f is not None:
        s = jsonpickle.encode(survey)
        f.write(s)
        f.close()
        
## Load a Survey object from a file.
#
def loadSurvey(filename):
    from question import Question
    from answer import Answer
    survey = None
    f = open(filename, "r")
    if f is not None:
        s = ""
        b = f.read(512)
        while len(b):
            s += b
            b = f.read(512)
        f.close()
        sd = jsonpickle.decode(s)
        survey = Survey()
        survey.name = sd['name']
        survey.questions = {}
        for qd in sd['questions'].values():
            question = Question()
            question.id = qd['id']
            question.name = qd['name']
            question.answers = {}
            for ad in qd['answers'].values():
                answer = Answer()
                answer.id = ad['id']
                answer.value = ad['value']
                answer.selected = ad['selected']
                answer.editable = ad['editable']
                question.answers[answer.id] = answer
            survey.questions[question.id] = question
    return survey

if __name__ == '__main__':
    from question import Question
    from answer import Answer
    s = Survey("Survey Load Test")
    q = s.add(Question(1,"Question1"))
    q.add(Answer(1,"answer1"))
    q.add(Answer(2,"answer2"))
    
    q = s.add(Question(2,"Question2"))
    q.add(Answer(3,"answer3"))
    q.add(Answer(4,"answer4"))
    q.add(Answer(5,"answer5"))
    saveSurvey(s, "test_load.svy")
#    s1 = loadSurvey("test_load.svy")
    

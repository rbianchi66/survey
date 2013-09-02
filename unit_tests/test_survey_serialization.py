#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from survey import Survey, saveSurvey, loadSurvey
from question import Question
from answer import Answer

survey = None

class TestSurveySerialization(unittest.TestCase):
    """Tests the serialization of a survey."""

    def setUp(self):
        global survey
        survey = Survey()
        q = survey.add(Question(1,"Question1"))
        q.add(Answer(1,"answer1"))
        q.add(Answer(2,"answer2"))
        q = survey.add(Question(2,"Question2"))
        q.add(Answer(3,"answer3"))
        q.add(Answer(4,"answer4"))
        q.add(Answer(5,"answer5"))

    def test_save_survey(self):
        global survey
        t = True
        try:
            saveSurvey(survey, "test_save.svy")
        except IOError:
            t = False
        self.assertEqual(t, True)

    def test_load_survey(self):
        global survey
        s = loadSurvey("test_load.svy")
        self.assertEqual(s.name, "Survey Load Test")
        self.assertEqual(len(s.questions), 2)

        q = s.questions[1]
        self.assertEqual(q.name, "Question1")
        self.assertEqual(len(q.answers), 2)
        a = q.answers[1]
        self.assertEqual(a.value, "answer1")
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)
        a = q.answers[2]
        self.assertEqual(a.value, "answer2")
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)

        q = s.questions[2]
        self.assertEqual(q.name, "Question2")
        self.assertEqual(len(q.answers), 3)
        a = q.answers[3]
        self.assertEqual(a.value, "answer3")
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)
        a = q.answers[4]
        self.assertEqual(a.value, "answer4")
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)
        a = q.answers[5]
        self.assertEqual(a.value, "answer5")
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)
        


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSurveySerialization)

if __name__ == '__main__':
    unittest.main()


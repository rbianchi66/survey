#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from survey import Survey
from question import Question
from answer import Answer

class TestSurveyBasic(unittest.TestCase):
    """Basic tests for survey."""

    def setUp(self):
        pass

    def test_new_survey(self):
        s = Survey()
        self.assertNotEqual(s, None)
        self.assertEqual(s.name, 'New Survey')

    def test_new_question(self):
        q = Question()
        self.assertNotEqual(q, None)
        self.assertEqual(q.id, 0)
        self.assertEqual(q.name, 'New Question')

    def test_new_answer(self):
        a = Answer()
        self.assertNotEqual(a, None)
        self.assertEqual(a.id, 0)
        self.assertEqual(a.selected, False)
        self.assertEqual(a.editable, False)

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSurveyBasic)

if __name__ == '__main__':
    unittest.main()


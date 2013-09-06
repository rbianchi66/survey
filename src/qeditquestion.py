#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, Qt, QtCore
from translation import L

class QQuestionGridButton(QtGui.QPushButton):
    def __init__(self, question, **kwargs):
        QtGui.QPushButton.__init__(self, **kwargs)
        if question is not None:
            l = question.name
        else:
            l = L("EMPTY")
        l = "\n" + l + "\n"
        self.setText(l)
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Normal)
        font.setStyle(QtGui.QFont.StyleItalic)
        self.setFont(font)

class QSurveyGrid(QtGui.QWidget):
    def __init__(self, survey, **kwargs):
        QtGui.QWidget.__init__(self, **kwargs)
        self.survey = survey
        self.layout = QtGui.QVBoxLayout(self)
        title = QtGui.QLabel(self.survey.name)
        font = QtGui.QFont("Arial", 16, QtGui.QFont.Bold)
        title.setFont(font)
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)
        grid = QtGui.QGridLayout()
        qk = self.survey.questions.keys()
        qk.sort()
        c = 1
        for x in xrange(3):
            for y in xrange(3):
                q = self.survey.questions.get(c, None)
                f = QQuestionGridButton(q)
                grid.addWidget(f, x, y)
                c += 1
        self.layout.addLayout(grid)
            
        

class QSurveyGridShow(QtGui.QMainWindow):
    def __init__(self, survey):
        super(QSurveyGridShow, self).__init__()
        sg = QSurveyGrid(survey)
        self.setCentralWidget(sg)
        self.setWindowTitle("Survey Grid")
        self.show()


if __name__ == "__main__":
    import sys
    from translation import loadTranslation
    from survey import Survey
    from question import Question
    from answer import Answer
    s = Survey("Survey Grid Test")
    q = s.add(Question(1,"Question1"))
    q.add(Answer(1,"answer1"))
    q.add(Answer(2,"answer2"))
    
    q = s.add(Question(2,"Question2"))
    q.add(Answer(3,"answer3"))
    q.add(Answer(4,"answer4"))
    q.add(Answer(5,"answer5"))

    loadTranslation("en")
    
    app = QtGui.QApplication(sys.argv)
    survey_grid = QSurveyGridShow(s)
    survey_grid.setGeometry(200, 100, 800, 600)
    sys.exit(app.exec_())
    


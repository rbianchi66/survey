#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, Qt, QtCore
from translation import L

class QQuestionGridItem(QtGui.QFrame):
    def __init__(self, id, question, **kwargs):
        QtGui.QFrame.__init__(self, **kwargs)
        self.id = id
        self.question = question
        self.selected = False
        self.tracking = False
        fl = QtGui.QVBoxLayout()
        self.setLayout(fl)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        if question is not None:
            l = QtGui.QLabel(question.name)
            font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        else:
            l = QtGui.QLabel(L("EMPTY"))
            font = QtGui.QFont("Arial", 14, QtGui.QFont.Normal)
            font.setStyle(QtGui.QFont.StyleItalic)
        l.setFont(font)
        l.setAlignment(QtCore.Qt.AlignCenter)
        fl.addWidget(l)
        fl.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.setMouseTracking(True)
    
    def select(self, s):
        self.selected = s
        if self.selected:
            self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
            self.setBackgroundRole(QtGui.QPalette.Midlight)
        else:
            self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
            self.setBackgroundRole(QtGui.QPalette.Button)
    
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.tracking = True

    def mouseReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton and self.tracking:
            self.tracking = False
            self.select(not self.selected)
            self.emit(QtCore.SIGNAL("clicked(int)"), self.id)
            self.update()
    
class QSurveyGrid(QtGui.QWidget):
    def __init__(self, survey, **kwargs):
        QtGui.QWidget.__init__(self, **kwargs)
        self.survey = survey
        self.layout = QtGui.QVBoxLayout(self)
        self.items = {}
        title = QtGui.QLabel(self.survey.name)
        font = QtGui.QFont("Arial", 16, QtGui.QFont.Bold)
        title.setFont(font)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setMaximumHeight(100)
        self.layout.addWidget(title)
        grid = QtGui.QGridLayout()
        qk = self.survey.questions.keys()
        qk.sort()
        c = 1
        for x in xrange(3):
            for y in xrange(3):
                q = self.survey.questions.get(c, None)
                f = QQuestionGridItem(c, q)
                self.connect(f, QtCore.SIGNAL("clicked(int)"), self.clickQuestion)
                grid.addWidget(f, x, y)
                self.items[c] = f
                c += 1
        self.layout.addLayout(grid)

    def clickQuestion(self, id):
        item = self.items[id] 
        for i in self.items.values():
            if i != item:
                i.select(False)
        self.emit(QtCore.SIGNAL("clicked(int)"), id)

    def getQuestion(self, id):
        return self.items.get(id, None)
    
    

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
    


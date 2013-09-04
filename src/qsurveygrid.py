#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, Qt, QtCore
from translation import L

class QAnswerGridItem(QtGui.QFrame):
    def __init__(self, answer, **kwargs):
        QtGui.QFrame.__init__(self, **kwargs)
        fl = QtGui.QHBoxLayout()
        self.setLayout(fl)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Normal)


class QQuestionGridItem(QtGui.QFrame):
    def __init__(self, question, **kwargs):
        QtGui.QFrame.__init__(self, **kwargs)
        self.question = question
        self.answers_list = None
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
        if question is not None:
            pb_text = L("QUESTION_GRID_PB") % len(question.answers)
            self.answer_pb = QtGui.QPushButton(pb_text)
            self.answer_pb.clicked.connect(self.showAnswers)
            fl.addWidget(self.answer_pb)
        fl.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
    
    def showAnswers(self):
        if self.answers_list is None and self.question is not None:
            self.answers_list = QtGui.QTableWidget(len(self.question.answers), 1)
            for i,a in enumerate(self.question.answers.values()):
                item = QtGui.QTableWidgetItem(a.value)
                self.answers_list.setItem(i,0,item)
            self.answers_list.setMaximumWidth(100)
            self.layout().addWidget(self.answers_list)
        else:
            self.layout().removeWidget(self.answers_list)
            self.answers_list.hide()
            self.answers_list = None
            
        
        


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
                f = QQuestionGridItem(q)
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
    


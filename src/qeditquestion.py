#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, Qt, QtCore
from translation import L

class QEditRadioAnswer(QtGui.QRadioButton):
    def __init__(self, answer, parent, **kwargs):
        QtGui.QRadioButton.__init__(self, answer.value, parent, **kwargs)
        self.answer = answer

class QEditCheckboxAnswer(QtGui.QCheckBox):
    def __init__(self, answer, parent, **kwargs):
        QtGui.QCheckBox.__init__(self, answer.value, parent, **kwargs)
        self.answer = answer

class QEditOpenAnswer(QtGui.QWidget):
    def __init__(self, answer, parent, **kwargs):
        QtGui.QWidget.__init__(self, parent, **kwargs)
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(QtGui.QLabel(answer.value))
        e = QtGui.QLineEdit()
        e.setReadOnly(True)
        self.layout.addWidget(e)
        self.answer = answer
        
        
class QQuestionEditFrame(QtGui.QFrame):
    def __init__(self, question, rows = 5, **kwargs):
        QtGui.QFrame.__init__(self, **kwargs)
        self.question = question
        self.rows = rows
        self.menu = None
        self.columns = len(question.answers)/rows
        if len(question.answers)%rows > 0:
            self.columns += 1 
        self.layout = QtGui.QHBoxLayout(self)
        title = QtGui.QLabel(self.question.name)
        font = QtGui.QFont("Arial", 16, QtGui.QFont.Bold)
        title.setFont(font)
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)
        line = QtGui.QFrame()
        line.setFrameStyle(QtGui.QFrame.VLine | QtGui.QFrame.Plain)
        self.layout.addWidget(line)
        grid = QtGui.QGridLayout()
        ak = self.question.answers.keys()
        ak.sort()
        c = 0
        r = 0
        for ai in ak:
            el = QtGui.QHBoxLayout()
            answer = self.question.answers[ai]
            f = QEditOpenAnswer(answer, self)
            el.addWidget(f)
            pb = QtGui.QPushButton("-")
            pb.setMaximumWidth(40)
            el.addWidget(pb)
            grid.addLayout(el, r, c)
            r += 1
            if r >= self.rows:
                c += 1
                r = 0
        self.layout.addLayout(grid)
        self.setMouseTracking(True)
        
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.RightButton:
            pos = self.mapToGlobal(e.pos())
            self.menu = QtGui.QMenu(self)
            self.menu.addAction("&Add")
            self.menu.addAction("&Remove")
            self.menu.exec_(pos)
            self.menu = None
        
        
            
class QQuestionEditShow(QtGui.QMainWindow):
    def __init__(self, question):
        super(QQuestionEditShow, self).__init__()
        sg = QQuestionEditFrame(question)
        self.setCentralWidget(sg)
        self.setWindowTitle("Question Edit Frame")
        self.show()


if __name__ == "__main__":
    import sys
    from translation import loadTranslation
    from question import Question
    from answer import Answer
    
    q = Question(2,"Question2")
    q.add(Answer(1,"answer1"))
    q.add(Answer(2,"answer2"))
    q.add(Answer(3,"answer3"))
    q.add(Answer(4,"answer4"))
    q.add(Answer(5,"answer5"))
    q.add(Answer(6,"answer6"))
    q.add(Answer(7,"answer7"))

    loadTranslation("en")
    
    app = QtGui.QApplication(sys.argv)
    survey_grid = QQuestionEditShow(q)
    survey_grid.setGeometry(200, 100, 800, 600)
    sys.exit(app.exec_())
    


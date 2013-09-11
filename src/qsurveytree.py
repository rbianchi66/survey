#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui, Qt, QtCore
from translation import L

QTreeWidgetItem = QtGui.QTreeWidgetItem

class QSurveyTree(QtGui.QTreeWidget):
    def __init__(self, survey, **kwargs):
        QtGui.QTreeWidget.__init__(self, **kwargs)
        self.survey = survey
        s = QtGui.QTreeWidgetItem(self, QtCore.QStringList(survey.name))
        self.insertTopLevelItems(0, [s])
        qk = survey.questions.keys()
        qk.sort()
        for qi in qk:
            q = survey.questions[qi]
            nitem = QtGui.QTreeWidgetItem(s, QtCore.QStringList(q.name), 1000)
            ak = q.answers.keys()
            ak.sort()
            aitems = []
            for ai in ak:
                a = q.answers[ai]
                aitem = QtGui.QTreeWidgetItem(nitem, QtCore.QStringList(a.value), 1001)
        self.connect(self, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.clicked)
        self.setHeaderHidden(True)

    def clicked(self, item, c):
        if item.type() == 1000:
            self.emit(QtCore.SIGNAL("questionClicked(int)"), item.id)
        if item.type() == 1001:
            self.emit(QtCore.SIGNAL("answerClicked(int)"), item.id)
        


class QSurveyTreeShow(QtGui.QMainWindow):
    def __init__(self, survey):
        super(QSurveyTreeShow, self).__init__()
        sg = QSurveyTree(survey)
        self.setCentralWidget(sg)
        self.setWindowTitle("Survey Tree")
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
    survey_tree = QSurveyTreeShow(s)
    survey_tree.setGeometry(200, 100, 800, 600)
    sys.exit(app.exec_())
    


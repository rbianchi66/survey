from PyQt4 import QtGui, Qt, QtCore
from question import Question

class RadioQuestion(Question):
    def __init__(self, id, question, card, parent = None):
        self.buttons = []
        super(RadioQuestion, self).__init__(id, question, card, parent)

    def updateValue(self, question, answer):
        self.card.set(question, answer)
        self.emit( Qt.SIGNAL("clicked()"))
    
    def showButtons(self, q):
        qind = 0
        if len(q) > 5:
            hlay = QtGui.QHBoxLayout() 
            ncols = len(q) / 5
            for nc in xrange(ncols):
                qlay = QtGui.QVBoxLayout()
                for icol in xrange(5):
                    element = QtGui.QRadioButton(self)
                    self.buttons.append(element)
                    n, question, valore = q[qind]
                    self.connect(element, Qt.SIGNAL("clicked()"), lambda n = n : self.updateValue(question, n))
                    if self.card.get(question) == n:
                        element.setChecked(True)
                    element.setText(valore)
                    qlay.addWidget(element)
                    qind += 1
                hlay.addLayout(qlay)
            if len(q)%5 > 0:
                qlay = QtGui.QVBoxLayout()
                for icol in xrange(len(q)%5):
                    element = QtGui.QRadioButton(self)
                    self.buttons.append(element)
                    n, question, val = q[qind]
                    self.connect(element, Qt.SIGNAL("clicked()"), lambda n = n : self.updateValue(question, n))
                    if self.card.get(question) == n:
                        element.setChecked(True)
                    element.setText(val)
                    qlay.addWidget(element)
                    qind += 1
                hlay.addLayout(qlay)
            self.answers_layout.addLayout(hlay)
        else:
            for icol in xrange(len(q)):
                element = QtGui.QRadioButton(self)
                self.buttons.append(element)
                n, question, val = q[qind]
                self.connect(element, Qt.SIGNAL("clicked()"), lambda n = n : self.updateValue(question, n))
                if self.card.get(question) == n:
                    element.setChecked(True)
                element.setText(val)
                self.answers_layout.addWidget(element)
                qind += 1
        if len(self.buttons):
            bf = None
            for b in self.buttons:
                if b.isChecked() == True:
                    bf = b
            if bf is None:
                answer, question, valore = q[0]
                self.updateValue(question, answer)
                self.buttons[0].setChecked(True)
            

from PyQt4 import QtGui, Qt
from card import Card
from question import Question

class CheckQuestion(Question):
    def __init__(self, id, question, card, parent = None):
        self.buttons = []
        super(CheckQuestion, self).__init__(id, question, card, parent)

    def updateValue(self, question, answer):
        al = []
        for b,q,a in self.buttons:
            if b.isChecked():
                al.append(a)
        self.card.set(question, al)
        self.update()
        self.emit( Qt.SIGNAL("clicked()"))
    
    def showButtons(self, q):
        qind = 0
        if len(q) > 5:
            hlay = QtGui.QHBoxLayout() 
            ncols = len(q) / 5
            for nc in xrange(ncols):
                qlay = QtGui.QVBoxLayout()
                for icol in xrange(5):
                    element = QtGui.QCheckBox(self)
                    n, question, valore = q[qind]
                    if self.card.has(question, n):
                        element.setChecked(True)
                    element.setText(valore)
                    self.connect(element, Qt.SIGNAL("stateChanged(int)"), lambda n = n : self.updateValue(question, n))
                    self.buttons.append((element,question,n))
                    qlay.addWidget(element)
                    qind += 1
                hlay.addLayout(qlay)
            if len(q)%5 > 0:
                qlay = QtGui.QVBoxLayout()
                for icol in xrange(len(q)%5):
                    element = QtGui.QCheckBox(self)
                    n, question, val = q[qind]
                    if self.card.has(question, n):
                        element.setChecked(True)
                    element.setText(val)
                    self.connect(element, Qt.SIGNAL("stateChanged(int)"), lambda n = n : self.updateValue(question, n))
                    self.buttons.append((element,question,n))
                    qlay.addWidget(element)
                    qind += 1
                hlay.addLayout(qlay)
            self.answers_layout.addLayout(hlay)
        else:
            for icol in xrange(len(q)):
                element = QtGui.QCheckBox(self)
                n, question, val = q[qind]
                if self.card.has(question, n):
                    element.setChecked(True)
                element.setText(val)
                self.connect(element, Qt.SIGNAL("clicked()"), lambda n = n : self.updateValue(question, n))
                self.buttons.append((element,question,n))
                self.answers_layout.addWidget(element)
                qind += 1
            
            

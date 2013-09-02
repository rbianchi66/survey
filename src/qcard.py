from PyQt4 import QtGui, Qt, QtCore
from radioquestion import RadioQuestion
from checkquestion import CheckQuestion
from multicheckquestion import MultiCheckQuestion
from card import Card
from qsummary import QSummary

class QCard(QtGui.QDialog):
    def __init__(self, qid, survey, *args):
        super(QtGui.QDialog, self).__init__(*args)
        self.survey = survey
        self.questions = survey["questions"]
        self.card = Card(qid)
        self.main_layout = QtGui.QVBoxLayout()
        self.title_layout = QtGui.QVBoxLayout()
        self.question_layout = QtGui.QHBoxLayout()
        self.buttons_layout = QtGui.QHBoxLayout()
        self.summary_layout = QtGui.QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.question_layout)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.summary_layout)

        # Title
        title = QtGui.QLabel("Scheda n.%d" % qid)
        title.setFont(QtGui.QFont("Arial", 20))
        self.title_layout.addWidget(title)
        div = QtGui.QFrame()
        div.setFixedHeight(50)
        #div.setMinimumHeight(10)
        div.setFrameShape(QtGui.QFrame.HLine)
        self.title_layout.addWidget(div)

        # Buttons
        self.prev = QtGui.QPushButton("Indietro")
        self.connect(self.prev, Qt.SIGNAL("clicked()"), self.prevQuestion)
        self.next = QtGui.QPushButton("Avanti")
        self.connect(self.next, Qt.SIGNAL("clicked()"), self.nextQuestion)
        self.quitb = QtGui.QPushButton("Esci")
        self.connect(self.quitb, Qt.SIGNAL("clicked()"), self.reject)
        self.buttons_layout.insertSpacing(-1, 100)
        self.buttons_layout.addWidget(self.prev)
        self.buttons_layout.addWidget(self.next)
        self.buttons_layout.addWidget(self.quitb)
        self.buttons_layout.insertSpacing(-1, 100)
        self.setLayout(self.main_layout)

        # Summary
        div = QtGui.QFrame()
        div.setMinimumHeight(10)
        div.setFrameShape(QtGui.QFrame.HLine)
        self.summary_layout.addWidget(div)
        self.summary = QSummary(qid, self.card, self.survey)
        self.summary_layout.addWidget(self.summary)

        self.question = None
        self.qindex = 0
        self.setQuestion(self.qindex)
        self.setMinimumWidth(700)

    def setQuestion(self, qindex):
        if self.question is not None:
            self.question_layout.removeWidget(self.question)
            #for e in self.question.buttons:
            #    if isinstance(e, tuple):
            #        b,q,a = e
            #    else:
            #        b = e
            #    if b.isChecked():
            #        pass
            self.question.close()
            self.question = None
        qtype = self.getQuestionType(qindex)
        qname = self.questions[qindex]
        if qtype == "r":
            self.question = RadioQuestion(qindex, self.survey[qname], self.card)
        if qtype == "c":
            self.question = CheckQuestion(qindex, self.survey[qname], self.card)
        if qtype == "m":
            self.question = MultiCheckQuestion(qindex, self.card)
        self.connect(self.question, Qt.SIGNAL("clicked()"), self.updateSummary)
        self.question_layout.addWidget(self.question)
        self.prev.setEnabled(qindex > 0)
        if (not qindex < len(self.questions)-1):
            self.next.setText("Inserisci scheda")
            self.disconnect(self.next, Qt.SIGNAL("clicked()"), self.nextQuestion)
            self.connect(self.next, Qt.SIGNAL("clicked()"), self.accept)
        else:
            self.next.setEnabled(True)
        self.updateSummary()

    def prevQuestion(self):
        self.qindex -= 1
        self.setQuestion(self.qindex)

    def nextQuestion(self):
        self.qindex += 1
        self.setQuestion(self.qindex)

    def updateSummary(self):
        self.summary.update()

    def accept(self):
        self.insertCard()
        self.setResult(1)

    def insertCard(self):
        pass
#         c = self.conn.cursor()
#         for k in self.card.answers.keys():
#             a = self.card.get(k)
#             if isinstance(a, list):
#                 for a1 in a:
#                     if isinstance(a1, list):
#                         v = ""
#                         for qid, aid, mid, val in a1:
#                             if val:
#                                 v = "1"
#                             else:
#                                 v = "0"
#                             c.execute("insert into schede_m (id_domanda, id_risposta, id, valore) values (?, ?, ?, ?)", qid,aid,mid,v)
#                     else:
#                         c.execute("insert into schede (id, domanda, risposta) values (?, ?, ?)", self.card.qid, k, a1)
#             else:
#                 c.execute("insert into schede (id, domanda, risposta) values (?, ?, ?)", self.card.qid, k, a)
#         self.conn.commit()
#         self.close()

    def getQuestionType(self, q):
        qname = self.questions[q]
        return self.survey[qname]["type"]
        
    def quit(self):
        QtGui.QApplication.exit(0)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = QCard(1,4)
    window.setMinimumHeight(400)
    window.show()
    sys.exit(app.exec_()) 
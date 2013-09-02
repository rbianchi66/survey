from PyQt4 import QtGui, Qt

class Question(QtGui.QFrame):
    def __init__(self, qnumber, question, card, *args):
        super(QtGui.QFrame, self).__init__(*args)
        print "qnumber:", qnumber
        print "question:", question
        self.card = card
        self.main_layout = QtGui.QGridLayout()
        self.answers_layout = QtGui.QVBoxLayout()
        #row = cur.execute("select valore from domande where id=%d" % qid).fetchone()
        title = QtGui.QLabel("Domanda %d" % qnumber)
        title.setFont(QtGui.QFont("Arial",9,75))
        self.main_layout.addWidget(title, 0, 0)
        self.question = QtGui.QLabel(question["name"])
        self.main_layout.addWidget(self.question, 1, 0)
        self.setFixedHeight(200)
        rows = [(qnumber,i,a) for i,a in enumerate(question["answers"])]
#         cur = self.conn.cursor()
#         rows = cur.execute("select id_domanda,id,valore from risposte where id_domanda=%d" % qid).fetchall()
#         cur.close()
        self.showButtons(rows)
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.answers_layout, 2, 0)

    def updateValue(self):
        pass
    
    def showButtons(self, rows):
        pass
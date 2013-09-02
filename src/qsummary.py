from PyQt4 import QtGui, Qt

class QSummary(QtGui.QFrame):
    def __init__(self, qid, card, survey, *args):
        super(QtGui.QFrame, self).__init__(*args)
        self.card = card
        self.survey = survey
        self.main_layout = QtGui.QVBoxLayout()
        self.title_layout = QtGui.QHBoxLayout()
        self.answers_layout = QtGui.QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.answers_layout)

        title = QtGui.QLabel("Sommario scheda n.%d" % qid)
        self.title_layout.addWidget(title)

        questions = self.survey["questions"]
        questions.sort()
        self.questions = questions
        self.table = QtGui.QTableWidget(len(questions),2)
        self.table.setHorizontalHeaderLabels(["Domanda","Risposta"])
        self.answers_layout.addWidget(self.table)
        for i,q in enumerate(questions):
            qtext = self.survey[q]["name"]
            self.table.setItem(i,0, QtGui.QTableWidgetItem(qtext))
        self.setLayout(self.main_layout)

    def update(self):
        for ind,q in enumerate(self.questions):
            answer = self.card.get(q)
            if answer is not None:
                if isinstance(answer, list):
                    atext = self.updateMulti(answer, q)
                else:
                    atext = self.updateSingle(answer, q) 
            else:
                atext = ""
            self.table.setItem(ind,1, QtGui.QTableWidgetItem(atext))
        self.table.resizeColumnsToContents()
    
    def updateSingle(self, answer, q):
        pass
#         acur = self.c.cursor()
#         arow = acur.execute("select valore from risposte where id=%d " % answer + " and id_domanda = %d" % q).fetchone()
#         t = arow[0]
#         acur.close()
#         return t

    def updateMulti(self, answer, q):
        t = ""
#         if len(answer) > 0:
#             if isinstance(answer[0], list):
#                 t = self.updateMultiMulti(answer, q)
#             else:
#                 for a1 in answer:
#                     acur = self.c.cursor()
#                     arow = acur.execute("select valore from risposte where id=%d " % a1 + " and id_domanda = %d" % q).fetchone()
#                     t += arow[0] + ","
#                     acur.close()
#                 t = t[:-1]
        return t
    
    def updateMultiMulti(self, answer, q):
        t = ""
#         nrow = 1
#         for a in answer:
#             qid,aid,mid,val = a[0]
#             acur = self.c.cursor()
#             arow = acur.execute("select valore from risposte where id=%d " % aid + " and id_domanda = %d" % qid).fetchone()
#             r = arow[0]
#             vals = self.getMultiCols(q)
#             t += "%d:" % nrow
#             for qid,aid,mid,v in a:
#                 if v == 1:
#                     t += vals[mid] + ","
#             t = t[:-1]
#             t += "|"
#             nrow += 1
        return t

    def getMultiCols(self, qid):
        pass
#         cur = self.c.cursor()
#         rrows = cur.execute("select distinct(valore) from risposte_m where id_domanda=%d and id_risposta in (select id from risposte where id_domanda = %d)" % (qid,qid)).fetchall()
#         cols = [v[0] for v in rrows]
#         cur.close()
#         return cols

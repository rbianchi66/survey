from PyQt4 import QtGui, Qt
from card import Card
from question import Question

class MultiCheckQuestion(Question):
    def __init__(self, qid, card, parent = None):
        self.buttons = []
        super(Question, self).__init__()
        self.card = card
        self.main_layout = QtGui.QGridLayout()
        self.answers_layout = QtGui.QVBoxLayout()
#         cur = self.conn.cursor()
#         row = cur.execute("select valore from domande where id=%d" % qid).fetchone()
        title = QtGui.QLabel("Domanda %d" % qid)
        title.setFont(QtGui.QFont("Arial",9,75))
        self.main_layout.addWidget(title, 0, 0)
        self.question = QtGui.QLabel(row[0])
        self.main_layout.addWidget(self.question, 1, 0)
        cur.close()
        self.setFixedHeight(200)
        rows = self.getRows(qid)
        d,i,val = rows[0]
        cols = self.getCols(qid)
        self.showButtons(qid, rows, cols)
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.answers_layout, 2, 0)

    def updateValue(self, question, answer):
        al = []
        for br in self.buttons:
            ar = []
            for element,qid,aid,mid in br:
                val = element.isChecked()
                ar.append([qid,aid,mid,val])
            al.append(ar)
        self.card.set(question, al)
        self.update()
        self.emit( Qt.SIGNAL("clicked()"))
    
    def showButtons(self, qid, rows, cols):
        self.table = QtGui.QGridLayout()
        headers = ["Domanda"]
        ncol = 1
        for val in cols:
            self.table.addWidget(QtGui.QLabel(val), 0, ncol)
            ncol += 1
        nrow = 1
        for did, aid, val in rows:
            val = "%d. " % nrow + val
            self.table.addWidget(QtGui.QLabel(val), nrow, 0)
            nrow += 1
        nrow = 1
        self.buttons = []
        for r1 in self.getValues(qid, len(rows), len(cols)):
            ncol = 1
            br = []
            for did, aid, mid, v in r1:
                element = QtGui.QCheckBox(self)
                element.setChecked((v == 1))
                br.append([element,did,aid,mid])
                self.table.addWidget(element, nrow, ncol)
                self.connect(element, Qt.SIGNAL("stateChanged(int)"), lambda ncol : self.updateValue(qid, None))                
                ncol += 1
            nrow += 1
            self.buttons.append(br)

        self.answers_layout = self.table

            
    def getRows(self, qid):
        pass
#         cur = self.conn.cursor()
#         rrows = cur.execute("select id_domanda,id,valore from risposte where id_domanda=%d" % qid).fetchall()
#         cur.close()
#         rows = []
#         for did,aid,val in rrows:
#             rows.append([qid,aid,val])
#         #rows = [[15,0,'Riga1'],[15,1,'Riga2'],[15,2,'Riga3'],[15,3,'Riga4']]
#         return rows
    
    def getCols(self, qid):
        pass
#         cur = self.conn.cursor()
#         rrows = cur.execute("select distinct(valore) from risposte_m where id_domanda=%d and id_risposta in (select id from risposte where id_domanda = %d)" % (qid,qid)).fetchall()
#         cols = [v[0] for v in rrows]
#         #cols = [[15,0,0,'Si'],[15,0,1,'No'],[15,0,2,'Non so']]
#         cur.close()
#         return cols
    
    def getValues(self, qid, nrows, ncols):
        vals = self.card.get(qid)
        if vals is None:
            vals = []
            for x in xrange(nrows): 
                r = [[qid,x,y,0] for y in xrange(ncols)]
                vals.append(r) 
        return vals

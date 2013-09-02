from PyQt4 import QtGui
import pyodbc

class Domanda(QtGui.QDialog):
    def __init__(self, id, type = "radio", parent = None):
        super(Domanda, self).__init__(parent)
        c = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=c:\\projects\\alimentazione\\db1.mdb')
        main_layout = QtGui.QVBoxLayout()
        question_layout = QtGui.QHBoxLayout()
        answers_layout = QtGui.QHBoxLayout()
        buttons_layout = QtGui.QHBoxLayout()
        main_layout.addLayout(question_layout)
        main_layout.addLayout(answers_layout)
        main_layout.addLayout(buttons_layout)
        cur = c.cursor()
        row = cur.execute("select valore from domande where id=%d" % id).fetchone()
        question = QtGui.QLabel()
        question.setText(row[0])
        question_layout.addWidget(question)
        cur.close()
        
        cur = c.cursor()
        for row in cur.execute("select * from risposte where id_domanda=%d" % id):
            if type == "radio":
                element = QtGui.QRadioButton()
            if type == "check":
                element = QtGui.QCheckBox()
            element.setText(row.valore)
            answers_layout.addWidget(element)
        c.close()

        next = QtGui.QPushButton("Avanti")
        prev = QtGui.QPushButton("Indietro")
        buttons_layout.addWidget(prev)
        buttons_layout.addWidget(next)
        
        self.setLayout(main_layout)


import sys

app = QtGui.QApplication(sys.argv)
window = Domanda(4, "check")
window.setModal(True)
window.show()


sys.exit(app.exec_()) 
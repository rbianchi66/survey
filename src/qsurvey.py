from PyQt4 import QtGui
import sys
import parms

cards = {}

class QSurvey(QtGui.QMainWindow):
    def __init__(self):
        super(QSurvey, self).__init__()
        
        action = QtGui.QAction("&Action2", self)
        
        menubar = self.menuBar()
        menu1 = menubar.addMenu("&File")
        menu1.addAction(action)
        #menu1.addAction("&Action1")
        #tb = self.addToolBar("File")
        #tb.addAction(action)
        self.setWindowTitle("Survey")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":
    import getopt
    
    opts, args = [], []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:", ["survey="])
    except getopt.GetoptError, err:
        print "Error reading options:",err

    survey_file="survey.ini"
    for o, a in opts:
        if o in ("-s", "--survey"):
            survey_file = a
    
    app = QtGui.QApplication(sys.argv)
    ali = QSurvey()
    sys.exit(app.exec_())
               
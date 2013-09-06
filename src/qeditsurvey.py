from PyQt4 import QtGui
import sys
import parms
from translation import L, loadTranslation
from qsurveygrid import QSurveyGrid

class QEditSurvey(QtGui.QMainWindow):
    def __init__(self):
        super(QEditSurvey, self).__init__()

        menubar = self.menuBar()
        
        #
        # File
        #
        
        file_menu = menubar.addMenu(L("FILE_MENU"))
        file_menu.addAction(L("FILE_MENU_NEW"))
        
        # Open 
        action = QtGui.QAction(L("FILE_MENU_OPEN"), self)
        action.triggered.connect(self.openSurvey)
        file_menu.addAction(action)

        file_menu.addAction(L("FILE_MENU_SAVE"))
        file_menu.addAction(L("FILE_MENU_SAVE_AS"))
        file_menu.addAction(L("FILE_MENU_CLOSE"))
        file_menu.addSeparator()
        file_menu.addAction(L("FILE_MENU_EXPORT"))
        file_menu.addAction(L("FILE_MENU_PRINT"))
        file_menu.addSeparator()
        
        # Quit 
        action = QtGui.QAction(L("FILE_MENU_QUIT"), self)
        action.triggered.connect(self.quit)
        file_menu.addAction(action)
        

        # Survey
        survey_menu = menubar.addMenu(L("SURVEY_MENU"))
        question_menu = survey_menu.addMenu(L("SURVEY_MENU_ADD_QUESTION"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_CHECKBOX"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_RADIOBUTTON"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_OPEN"))
        survey_menu.addAction(L("SURVEY_MENU_ADD_ANSWER"))
        
        
        # Survey selection frame
        self.survey_frame = QtGui.QFrame()
        self.survey_frame.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        self.setCentralWidget(self.survey_frame)
        
        
        self.setWindowTitle("Survey")
        self.show()

    def newSurvey(self):
        pass

    def openSurvey(self):
        from survey import Survey, loadSurvey
        filename = QtGui.QFileDialog.getOpenFileName(self, "Select survey file", ".", "Survey Files (*.svy)")
        survey = loadSurvey(filename)
        sg = QSurveyGrid(survey)
        self.setCentralWidget(sg)

    def saveSurvey(self):
        pass

    def saveSurveyAs(self):
        pass

    def exportSurvey(self):
        pass

    def printSurvey(self):
        pass

    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    import getopt
    
    
    opts, args = [], []
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:", ["survey="])
    except getopt.GetoptError, err:
        print "Error reading options:",err

    survey_file="survey.ini"
    lang = "en"
    for o, a in opts:
        if o in ("-s", "--survey"):
            survey_file = a
    
    loadTranslation(lang)
    
    app = QtGui.QApplication(sys.argv)
    edit_survey = QEditSurvey()
    edit_survey.setGeometry(200, 100, 800, 600)
    sys.exit(app.exec_())
               
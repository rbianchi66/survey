from PyQt4 import QtGui
import sys
import parms
from translation import L, loadTranslation

class QEditSurvey(QtGui.QMainWindow):
    def __init__(self):
        super(QEditSurvey, self).__init__()

        menubar = self.menuBar()
        
        # File
        file_menu = menubar.addMenu(L("FILE_MENU"))
        file_menu.addAction(L("FILE_MENU_NEW"))
        file_menu.addAction(L("FILE_MENU_OPEN"))
        file_menu.addAction(L("FILE_MENU_SAVE"))
        file_menu.addAction(L("FILE_MENU_SAVE_AS"))
        file_menu.addAction(L("FILE_MENU_CLOSE"))
        file_menu.addSeparator()
        file_menu.addAction(L("FILE_MENU_EXPORT"))
        file_menu.addAction(L("FILE_MENU_PRINT"))
        file_menu.addSeparator()
        file_menu.addAction(L("FILE_MENU_QUIT"))

        # Survey
        survey_menu = menubar.addMenu(L("SURVEY_MENU"))
        question_menu = survey_menu.addMenu(L("SURVEY_MENU_ADD_QUESTION"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_CHECKBOX"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_RADIOBUTTON"))
        question_menu.addAction(L("SURVEY_MENU_QUESTION_OPEN"))
        survey_menu.addAction(L("SURVEY_MENU_ADD_ANSWER"))
        
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
    lang = "en"
    for o, a in opts:
        if o in ("-s", "--survey"):
            survey_file = a
    
    loadTranslation(lang)
    
    app = QtGui.QApplication(sys.argv)
    ali = QEditSurvey()
    sys.exit(app.exec_())
               
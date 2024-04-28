
from Interface import app as RehabApp
from PyQt6 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RehabGame = QtWidgets.QMainWindow()
    ui = RehabApp.Ui_RehabGame()
    ui.setupUi(RehabGame)
    RehabGame.show()
    sys.exit(app.exec())

"""
# main menu button navigation
        self.GameFirstButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.GameOneSettings))
        self.GameSecondButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.GameSecondSettings))
        self.PerformanceButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PerformanceAnalysis))

        #back and Start navigation
        self.BackButton_GameFirst.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AppInterface))
        self.BackButton_GameTwo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AppInterface))
        self.End_Button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AppInterface))
"""
import constant_value
import cardlib
import randomlib
import mainwindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m_window = mainwindow.Ui_MainWindow()

    m_window.show()
    sys.exit(app.exec_())
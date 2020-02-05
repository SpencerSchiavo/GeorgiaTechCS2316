# Spencer Schiavo
# 903125926
# sschiavo3

import sys
import csv
import sqlite3
import pymysql
import getpass
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QDialog,
    QGroupBox,
    QVBoxLayout,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QLabel,
    qApp,
    QAction,
    QSplitter,
    QListView,
    QTableWidget,
    QTableWidgetItem
)

class MainWindow(QWidget):

    def __init__(self, db):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        cursor = connection.cursor()
        cursor.execute("use " + db)
        cursor.execute("show tables")

        button_names = ['Passengers By Date', 'Routes', 'Stops', 'Vehicles']

        i = 0

        for diction in cursor:

            table_name = diction["Tables_in_marta"]
            layout.addWidget(self.make_button(db, button_names[i], table_name))
            i += 1

        self.setLayout(layout)

    def make_button(self, db, name, table_name):
        button = QPushButton(name, self)
        button.clicked.connect(lambda: self.display(db, table_name))
        return button

    def display(self, db, table_name):
        cursor_2 = connection.cursor()
        cursor_2.execute("select * from " + table_name)
        TableDialog().exec()


class TableDialog(QDialog):

    def __init__(self):
        super(TableDialog, self).__init__()
        layout = QVBoxLayout()
        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)
        self.setLayout(layout)





if __name__=='__main__':

    pw = getpass.getpass('Password for ' + sys.argv[4] + '@' + sys.argv[3] + ':')
    global connection
    connection = pymysql.connect(host = sys.argv[3], user = sys.argv[4], password = pw, db = sys.argv[2], charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

    app = QApplication(sys.argv)
    main = MainWindow(sys.argv[2])
    main.show()
    sys.exit(app.exec_())




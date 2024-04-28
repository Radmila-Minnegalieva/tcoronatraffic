"""returns a running desktop application and takes various types of data from forms, and also broadcasts a running server"""
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import pandas as pd
from PyQt5.QtCore import QUrl
import json


def setup_web_engine():
    """passes to QWebEngineView a URL value that can be changed at any time"""
    with open ('..\data\data.json') as f:
        data_content = json.load(f)
    url = data_content['url']
    ui.webEngineView.setUrl(QUrl(url))

def setup_button():
    """passes to the plotting function the values ​​entered by the user in the forms at the click of a button"""
    ui.pushButton.clicked.connect(
        lambda: show_plot(dataset, ui.criteria.currentText(), ui.criteria_value.currentText(), get_date_from(),
                          get_date_to(), ui.mean.isChecked()))


def setup_combo_boxes():
    """returns the criteria value selected by the user and passes it to the next function to return the correct list of data"""
    ui.criteria.currentTextChanged.connect(
        lambda: handle_combo_box_update()
    )
    ui.criteria.addItems(list(criteria.keys()))


def handle_combo_box_update():
    """takes values ​​from criteria keys and clears if a criterion change occurs"""
    ui.criteria_value.clear()
    ui.criteria_value.addItems(criteria[str(ui.criteria.currentText())])


def get_date_from():
    """returns the date value from"""
    date = ui.dateEdit_2.date()
    return str(date.toPyDate())


def get_date_to():
    """returns the date value to"""
    date = ui.dateEdit.date()
    return str(date.toPyDate())


if __name__ == "__main__":
    sys.path.insert(0, "..")
    from library.MainWindow import Ui_MainWindow
    from library.functions import *

    dataset = pd.read_csv("../data/covid_impact_on_airport_traffic.csv")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setup_button()
    setup_combo_boxes()
    setup_web_engine()
    sys.exit(app.exec_())

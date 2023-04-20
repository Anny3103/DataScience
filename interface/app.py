from PyQt6.QtWidgets import QApplication, QWidget
import sys
from UI.widget import Ui_Form
from analysis.predict import Model
import pandas as pd


model = Model()

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.eval_button.clicked.connect(self.evaluate)
        self.setWindowTitle('Прогноз прибыли')

    def get_data(self):
        x1 = float(self.x1.toPlainText())
        x2 = float(self.x2.toPlainText())
        x3 = float(self.x3.toPlainText())
        x4 = float(self.x4.toPlainText())
        x5 = float(self.x5.toPlainText())
        x6 = float(self.x6.toPlainText())
        x7 = float(self.x7.toPlainText())
        x8 = float(self.x8.toPlainText())
        x9 = float(self.x9.toPlainText())
        x10 = float(self.x10.toPlainText())
        x11 = float(self.x11.toPlainText())
        x12 = float(self.x12.toPlainText())
        data = [[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]]
        df = pd.DataFrame(data, columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12'])
        return df

    def evaluate(self):
        try:
            self.resultbox.setText("%.2f" % model.pred(self.get_data())[0])
        except:
            self.resultbox.setText('Ошибка')


app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()

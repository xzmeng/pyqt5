import json
import sys

import requests
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.air import Ui_Form


class AirForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def query(self):
        url = 'http://web.juhe.cn:8080/environment/air/cityair'
        city = self.ui.lineEdit.text()
        params = {
            'city': city,
            'key': 'bae9fd7d6958840b5f31f0ab49bb537c',
        }

        r = requests.get(url, params)
        d = json.loads(r.content)
        try:
            result = city + 'AQI:' + \
                     d.get('result')[0].get('citynow').get('AQI')
        except:
            result = '没有找到关于"{}"的空气质量信息'.format(city)
        self.ui.textEdit.setText(result)

    def clear(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    app = QApplication([])
    form = AirForm()
    form.show()
    sys.exit(app.exec_())
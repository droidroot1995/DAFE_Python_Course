#!/usr/bin/python3

import sys
import requests # pip install requests
import lxml.etree as ET # pip install lxml
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton)
from PyQt5.QtGui import QPixmap, QFont


class CBR_API(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap('img/logo.png'))
        logo_label.move(0, 0)

        self.days()
        self.month()
        self.year()

        ok_button = QPushButton('OK', self)
        ok_button.resize(50, 23)
        ok_button.move(220, 198)

        ok_button.clicked.connect(self.make_request)

        self.load_result_image()

        self.setFixedSize(300, 400)
        self.setWindowTitle('История курса рубля')
        self.show()

    def days(self):
        self.days_combo = QComboBox(self)

        day_label = QLabel('День', self)
        day_label.move(20, 170)

        for day in range(1, 32):
            self.days_combo.addItem(f'{day}')

        self.days_combo.move(20, 200)


    def month(self):
        self.month_combo = QComboBox(self)

        month_label = QLabel('Месяц', self)
        month_label.move(80, 170)

        for month in range(1, 13):
            self.month_combo.addItem(f'{month}')

        self.month_combo.move(80, 200)

    def year(self):
        self.year_combo = QComboBox(self)

        year_label = QLabel('Год', self)
        year_label.move(140, 170)

        for year in range(2005, 2021):
            self.year_combo.addItem(f'{year}')

        self.year_combo.move(140, 200)

    def make_request(self):
        day_value = self.days_combo.currentText()
        month_value = self.month_combo.currentText()
        year_value = self.year_combo.currentText()

        result = self.get_result(day_value, month_value, year_value)

        self.dollar_value.setText(f"{result['dollar']} руб")
        self.dollar_value.adjustSize()

        self.euro_value.setText(f"{result['euro']} руб")
        self.euro_value.adjustSize()

    def get_result(self, day, month, year):
        
        result = {
            'dollar': 0,
            'euro': 0,
        }

        if int(day) < 10:
            day = f'0{day}'
        
        if int(month) < 10:
            month = f'0{month}'

        try:
            # request: 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=ДД/ММ/ГГГ'
            get_xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}')

            '''response: 
                <ValCurs Date="22.04.2017" name="Foreign Currency Market">
                <Valute ID="R01235">
                    <NumCode>840</NumCode>
                    <CharCode>USD</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Доллар США</Name>
                    <Value>56,2307</Value>
                </Valute>
            
                <Valute ID="R01239">
                    <NumCode>978</NumCode>
                    <CharCode>EUR</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Евро</Name>
                    <Value>60,3187</Value>
                </Valute>
            </ValCurs>'''

            structure = ET.fromstring(get_xml.content)

        except:
            return result

        try:
            dollar = structure.find("./*[@ID='R01235']/Value")
            result['dollar'] = dollar.text.replace(',', '.')
        except:
            result['dollar'] = 'x'

        try:
            euro = structure.find("./*[@ID='R01239']/Value")
            result['euro'] = euro.text.replace(',', '.')
        except:
            result['euro'] = 'x'

        return result

    def load_result_image(self):

        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(18)

        dollar_label = QLabel(self)
        dollar_label.setPixmap(QPixmap('img/dollar.png'))
        dollar_label.move(60, 260)

        self.dollar_value = QLabel('0 руб', self)
        self.dollar_value.setFont(font)
        self.dollar_value.move(130, 263)

        euro_label = QLabel(self)
        euro_label.setPixmap(QPixmap('img/euro.png'))
        euro_label.move(50, 320)

        self.euro_value = QLabel('0 руб', self)
        self.euro_value.setFont(font)
        self.euro_value.move(130, 320)


def main():
    app = QApplication(sys.argv)
    money = CBR_API()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
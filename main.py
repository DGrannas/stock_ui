import sys
from PyQt4 import QtGui, QtCore
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import design

#Load PyQt4 design
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Application
class ExampleApp(QtGui.QMainWindow, designy.Ui_MainWindow):
    #Initialize application and create all clickable buttons in UI
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        #Load portfolio tickers symbols
        with open("portfolios.txt", 'r') as obj:
            self.portfolios  = [[str(ticker) for ticker in line.split()] for line in obj]

        #Read in data for all stocks
        self.data = pd.read_csv("sp500_joined_closes.csv")

        self.portfolio_num = 0

        self.pushButton.clicked.connect(lambda: self.change_ticker(1))
        self.pushButton_2.clicked.connect(lambda: self.change_ticker(2))
        self.pushButton_3.clicked.connect(lambda: self.change_ticker(3))
        self.pushButton_4.clicked.connect(lambda: self.change_ticker(4))
        self.pushButton_5.clicked.connect(lambda: self.change_ticker(5))
        self.pushButton_6.clicked.connect(lambda: self.change_ticker(6))
        self.pushButton_7.clicked.connect(lambda: self.change_ticker(7))
        self.pushButton_8.clicked.connect(lambda: self.change_ticker(8))
        self.pushButton_9.clicked.connect(lambda: self.change_ticker(9))
        self.pushButton_10.clicked.connect(lambda: self.change_ticker(10))
        self.pushButton_11.clicked.connect(lambda: self.change_ticker(11))
        self.pushButton_12.clicked.connect(lambda: self.change_ticker(12))

        self.pushButton_13.clicked.connect(lambda: self.run(0))
        self.pushButton_14.clicked.connect(lambda: self.run(1))
        self.pushButton_15.clicked.connect(lambda: self.run(2))
        self.pushButton_16.clicked.connect(lambda: self.run(3))
        self.pushButton_17.clicked.connect(lambda: self.run(4))

    #Get the last updated price
    def get_price(self,ticker):
        return self.data[ticker].tail(1)

    #Options if clicking the button in UI,
    #either add/remove/change the stock from current portfolio
    def change_ticker(self,button_num):
        choice = QtGui.QMessageBox()
        choice.setIcon(QtGui.QMessageBox.Question)
        choice.setWindowTitle("Message")
        choice.setText("Do you want to add another stock \n or remove the existing stock?")
        choice.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No|QtGui.QMessageBox.Cancel)

        buttonAdd = choice.button(QtGui.QMessageBox.Yes)
        buttonAdd.setText("Add")
        buttonRemove = choice.button(QtGui.QMessageBox.No)
        buttonRemove.setText("Remove")
        choice.exec_()

        #User enters ticker symbol, if it exists in
        #the CSV file then it is added to portfolio
        if choice.clickedButton() == buttonAdd:
            ticker, ok = QtGui.QInputDialog.getText(self, 'Select Stock', 'Enter the ticker symbol:')

            if ok:
                if str(ticker) in self.data.columns:
                    self.change_pushbutton(str(ticker),button_num)
                    self.portfolios[self.portfolio_num][button_num-1] = str(ticker)
                else:
                    error = QtGui.QMessageBox.information(self, "Error", "Ticker symbol not found!", QtGui.QMessageBox.Ok)

        #User can remove stock by clicking "Remove"
        elif choice.clickedButton() == buttonRemove:
            self.portfolios[self.portfolio_num][button_num-1] = "empty"
            self.change_pushbutton("None",button_num)

        #Saves the current stocks in portfilio to
        self.save_portfolios()

    #Gets the current stocks in portfolio
    def get_tickers(self,portf_num):

        if portf_num == 0:
            tickers = self.portfolios[0]
            return tickers

        elif portf_num == 1:
            tickers = self.portfolios[1]
            return tickers

        elif portf_num == 2:
            tickers = self.portfolios[2]
            return tickers

        elif portf_num == 3:
            tickers = self.portfolios[3]
            return tickers

        else:
            tickers = self.portfolios[4]
            return tickers

    #Gets the price for all tickers in portfolio and
    #displays color based on price
    def change_pushbutton(self, ticker, button_num):
        price = 0
        percent_change = 0
        percent = 0
        rounded_price = 0
        rounded_percent = 0

        #Get price from CSV, convert to percentage
        if ticker != "None":
            price = self.get_price(ticker)
            percent_change = self.data[ticker].pct_change(1)
            percent = percent_change.tail(1)
            rounded_price = round(float(price),2)
            rounded_percent = round(float(percent),2)

        #Display stocks in UI and corresponding color
        if button_num == 1:
            if ticker != "None":
                self.pushButton.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton.setStyleSheet("background-color: green")
                else:
                    self.pushButton.setStyleSheet("background-color: red")
            else:
                self.pushButton.setText(_translate("MainWindow","Empty",None))
                self.pushButton.setStyleSheet("background-color: None")
        elif button_num == 2:
            if ticker != "None":
                self.pushButton_2.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_2.setStyleSheet("background-color: green")
                else:
                    self.pushButton_2.setStyleSheet("background-color: red")
            else:
                self.pushButton_2.setText(_translate("MainWindow","Empty",None))
                self.pushButton_2.setStyleSheet("background-color: None")
        elif button_num == 3:
            if ticker != "None":
                self.pushButton_3.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_3.setStyleSheet("background-color: green")
                else:
                    self.pushButton_3.setStyleSheet("background-color: red")
            else:
                self.pushButton_3.setText(_translate("MainWindow","Empty",None))
                self.pushButton_3.setStyleSheet("background-color: None")
        elif button_num == 4:
            if ticker != "None":
                self.pushButton_4.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_4.setStyleSheet("background-color: green")
                else:
                    self.pushButton_4.setStyleSheet("background-color: red")
            else:
                self.pushButton_4.setText(_translate("MainWindow","Empty",None))
                self.pushButton_4.setStyleSheet("background-color: None")
        elif button_num == 5:
            if ticker != "None":
                self.pushButton_5.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_5.setStyleSheet("background-color: green")
                else:
                    self.pushButton_5.setStyleSheet("background-color: red")
            else:
                self.pushButton_5.setText(_translate("MainWindow","Empty",None))
                self.pushButton_5.setStyleSheet("background-color: None")
        elif button_num == 6:
            if ticker != "None":
                self.pushButton_6.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_6.setStyleSheet("background-color: green")
                else:
                    self.pushButton_6.setStyleSheet("background-color: red")
            else:
                self.pushButton_6.setText(_translate("MainWindow","Empty",None))
                self.pushButton_6.setStyleSheet("background-color: None")
        elif button_num == 7:
            if ticker != "None":
                self.pushButton_7.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_7.setStyleSheet("background-color: green")
                else:
                    self.pushButton_7.setStyleSheet("background-color: red")
            else:
                self.pushButton_7.setText(_translate("MainWindow","Empty",None))
                self.pushButton_7.setStyleSheet("background-color: None")
        elif button_num == 8:
            if ticker != "None":
                self.pushButton_8.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_8.setStyleSheet("background-color: green")
                else:
                    self.pushButton_8.setStyleSheet("background-color: red")
            else:
                self.pushButton_8.setText(_translate("MainWindow","Empty",None))
                self.pushButton_8.setStyleSheet("background-color: None")
        elif button_num == 9:
            if ticker != "None":
                self.pushButton_9.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_9.setStyleSheet("background-color: green")
                else:
                    self.pushButton_9.setStyleSheet("background-color: red")
            else:
                self.pushButton_9.setText(_translate("MainWindow","Empty",None))
                self.pushButton_9.setStyleSheet("background-color: None")
        elif button_num == 10:
            if ticker != "None":
                self.pushButton_10.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_10.setStyleSheet("background-color: green")
                else:
                    self.pushButton_10.setStyleSheet("background-color: red")
            else:
                self.pushButton_10.setText(_translate("MainWindow","Empty",None))
                self.pushButton_10.setStyleSheet("background-color: None")
        elif button_num == 11:
            if ticker != "None":
                self.pushButton_11.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_11.setStyleSheet("background-color: green")
                else:
                    self.pushButton_11.setStyleSheet("background-color: red")
            else:
                self.pushButton_11.setText(_translate("MainWindow","Empty",None))
                self.pushButton_11.setStyleSheet("background-color: None")
        elif button_num == 12:
            if ticker != "None":
                self.pushButton_12.setText(_translate("MainWindow","{} {}\n ({})".format(ticker,rounded_price ,rounded_percent),None))
                if rounded_percent >= 0:
                    self.pushButton_12.setStyleSheet("background-color: green")
                else:
                    self.pushButton_12.setStyleSheet("background-color: red")
            else:
                self.pushButton_12.setText(_translate("MainWindow","Empty",None))
                self.pushButton_12.setStyleSheet("background-color: None")

    #Run function called when program starts
    def run(self,portf_num):
        tickers = self.get_tickers(portf_num)
        self.portfolio_num = portf_num
        i = 0
        n = 1
        #Checks all 12 buttons for current stock values
        #If empty button remains empty
        while i <= 12:
            if i < len(tickers):
                if tickers[i] != "empty":
                    self.change_pushbutton(tickers[i], n)
                    i += 1
                    n += 1
                else:
                    self.change_pushbutton("None",n)
                    i += 1
                    n += 1
            else:
                self.change_pushbutton("None",n)
                i += 1
                n += 1

    #Upon exit it saves possible stock adds/removals to txt file
    def save_portfolios(self):
        f = open("portfolios.txt", 'r+')
        f.seek(0)
        f.truncate()
        i = 0
        for x in self.portfolios:
            line = ""
            pos = 0
            while pos < len(self.portfolios[i]):
                line += self.portfolios[i][pos]
                line += " "
                pos += 1
            line += "\n"
            f.write(line)
            i += 1
        f.close()
#Run program
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    form.run(0)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

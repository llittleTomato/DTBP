# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import image
import csv
import BP.network2 as network2
from QT5 import qt5_data_loader


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setWindowModality(QtCore.Qt.NonModal)
		Form.resize(1024, 768)
		Form.setAutoFillBackground(False)
		Form.setStyleSheet("background-image: url(:/png/bg.png);")
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(70, 155, 67, 17))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(70, 225, 67, 17))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Form)
		self.label_3.setGeometry(QtCore.QRect(50, 366, 121, 20))
		self.label_3.setObjectName("label_3")
		self.textEdit_nx = QtWidgets.QTextEdit(Form)
		self.textEdit_nx.setGeometry(QtCore.QRect(60, 320, 80, 30))
		self.textEdit_nx.setObjectName("textEdit_nx")
		self.textEdit_pl = QtWidgets.QTextEdit(Form)
		self.textEdit_pl.setGeometry(QtCore.QRect(60, 390, 80, 30))
		self.textEdit_pl.setObjectName("textEdit_pl")
		self.label_4 = QtWidgets.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(70, 295, 67, 17))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(Form)
		self.label_5.setGeometry(QtCore.QRect(60, 575, 91, 20))
		self.label_5.setObjectName("label_5")
		self.textEdit_gz = QtWidgets.QTextEdit(Form)
		self.textEdit_gz.setGeometry(QtCore.QRect(60, 670, 80, 30))
		self.textEdit_gz.setObjectName("textEdit_gz")
		self.label_6 = QtWidgets.QLabel(Form)
		self.label_6.setGeometry(QtCore.QRect(60, 645, 91, 20))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(Form)
		self.label_7.setGeometry(QtCore.QRect(50, 436, 91, 20))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(Form)
		self.label_8.setGeometry(QtCore.QRect(70, 505, 67, 17))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(Form)
		self.label_9.setGeometry(QtCore.QRect(160, 475, 121, 20))
		self.label_9.setInputMethodHints(QtCore.Qt.ImhNone)
		self.label_9.setText("安全保护不合格项")
		self.label_9.setObjectName("label_9")
		self.textEdit_lh = QtWidgets.QTextEdit(Form)
		self.textEdit_lh.setGeometry(QtCore.QRect(180, 150, 80, 30))
		self.textEdit_lh.setObjectName("textEdit_lh")
		self.textEdit_zj = QtWidgets.QTextEdit(Form)
		self.textEdit_zj.setGeometry(QtCore.QRect(180, 360, 80, 30))
		self.textEdit_zj.setObjectName("textEdit_zj")
		self.textEdit_ms = QtWidgets.QTextEdit(Form)
		self.textEdit_ms.setGeometry(QtCore.QRect(180, 570, 80, 30))
		self.textEdit_ms.setObjectName("textEdit_ms")
		self.label_10 = QtWidgets.QLabel(Form)
		self.label_10.setGeometry(QtCore.QRect(176, 265, 91, 20))
		self.label_10.setObjectName("label_10")
		self.textEdit_ts = QtWidgets.QTextEdit(Form)
		self.textEdit_ts.setGeometry(QtCore.QRect(180, 220, 80, 30))
		self.textEdit_ts.setObjectName("textEdit_ts")
		self.textEdit_kzg = QtWidgets.QTextEdit(Form)
		self.textEdit_kzg.setGeometry(QtCore.QRect(180, 430, 80, 30))
		self.textEdit_kzg.setObjectName("textEdit_kzg")
		self.textEdit_kr = QtWidgets.QTextEdit(Form)
		self.textEdit_kr.setGeometry(QtCore.QRect(180, 290, 80, 30))
		self.textEdit_kr.setObjectName("textEdit_kr")
		self.label_11 = QtWidgets.QLabel(Form)
		self.label_11.setGeometry(QtCore.QRect(175, 335, 101, 20))
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(Form)
		self.label_12.setGeometry(QtCore.QRect(180, 125, 81, 20))
		self.label_12.setObjectName("label_12")
		self.label_13 = QtWidgets.QLabel(Form)
		self.label_13.setGeometry(QtCore.QRect(176, 195, 91, 20))
		self.label_13.setObjectName("label_13")
		self.textEdit_aq = QtWidgets.QTextEdit(Form)
		self.textEdit_aq.setGeometry(QtCore.QRect(180, 500, 80, 30))
		self.textEdit_aq.setObjectName("textEdit_aq")
		self.label_14 = QtWidgets.QLabel(Form)
		self.label_14.setGeometry(QtCore.QRect(176, 615, 101, 20))
		self.label_14.setObjectName("label_14")
		self.textEdit_qt = QtWidgets.QTextEdit(Form)
		self.textEdit_qt.setGeometry(QtCore.QRect(180, 640, 80, 30))
		self.textEdit_qt.setObjectName("textEdit_qt")
		self.label_15 = QtWidgets.QLabel(Form)
		self.label_15.setGeometry(QtCore.QRect(175, 545, 101, 20))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(Form)
		self.label_16.setGeometry(QtCore.QRect(170, 405, 111, 20))
		self.label_16.setObjectName("label_16")
		self.label_17 = QtWidgets.QLabel(Form)
		self.label_17.setGeometry(QtCore.QRect(70, 95, 67, 17))
		self.label_17.setObjectName("label_17")
		self.textEdit_cm = QtWidgets.QTextEdit(Form)
		self.textEdit_cm.setGeometry(QtCore.QRect(60, 120, 80, 30))
		self.textEdit_cm.setObjectName("textEdit_cm")
		self.textEdit_di = QtWidgets.QTextEdit(Form)
		self.textEdit_di.setGeometry(QtCore.QRect(860, 450, 81, 31))
		self.textEdit_di.setObjectName("textEdit_di")
		self.textEdit_gao = QtWidgets.QTextEdit(Form)
		self.textEdit_gao.setGeometry(QtCore.QRect(860, 310, 81, 31))
		self.textEdit_gao.setObjectName("textEdit_gao")
		self.textEdit_zhong = QtWidgets.QTextEdit(Form)
		self.textEdit_zhong.setGeometry(QtCore.QRect(860, 380, 81, 31))
		self.textEdit_zhong.setObjectName("textEdit_zhong")
		self.label_21 = QtWidgets.QLabel(Form)
		self.label_21.setGeometry(QtCore.QRect(440, 40, 300, 71))
		font = QtGui.QFont()
		font.setPointSize(22)
		font.setBold(True)
		font.setWeight(75)
		self.label_21.setFont(font)
		self.label_21.setObjectName("label_21")
		self.comboBox_zh = QtWidgets.QComboBox(Form)
		self.comboBox_zh.setGeometry(QtCore.QRect(60, 180, 80, 30))
		self.comboBox_zh.setObjectName("comboBox_zh")
		self.comboBox_zh.addItems(["有", "无"])
		self.comboBox_jy = QtWidgets.QComboBox(Form)
		self.comboBox_jy.setGeometry(QtCore.QRect(60, 250, 80, 30))
		self.comboBox_jy.setObjectName("comboBox_jy")
		self.comboBox_jy.addItems(["有", "无"])
		self.groupBox = QtWidgets.QGroupBox(Form)
		self.groupBox.setGeometry(QtCore.QRect(30, 50, 271, 671))
		self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);")
		self.groupBox.setFlat(False)
		self.groupBox.setObjectName("groupBox")
		self.comboBox_gl = QtWidgets.QComboBox(self.groupBox)
		self.comboBox_gl.setGeometry(QtCore.QRect(30, 550, 80, 30))
		self.comboBox_gl.setObjectName("comboBox_gl")
		self.comboBox_gl.addItems(["有", "无"])
		self.comboBox_dk = QtWidgets.QComboBox(self.groupBox)
		self.comboBox_dk.setGeometry(QtCore.QRect(30, 480, 80, 30))
		self.comboBox_dk.setObjectName("comboBox_dk")
		self.comboBox_dk.addItems(["有", "无"])
		self.comboBox_jw = QtWidgets.QComboBox(self.groupBox)
		self.comboBox_jw.setGeometry(QtCore.QRect(30, 415, 80, 30))
		self.comboBox_jw.setObjectName("comboBox_jw")
		self.comboBox_jw.addItems(["有", "无"])
		self.groupBox_2 = QtWidgets.QGroupBox(Form)
		self.groupBox_2.setGeometry(QtCore.QRect(840, 170, 121, 351))
		self.groupBox_2.setObjectName("groupBox_2")
		self.label_19 = QtWidgets.QLabel(self.groupBox_2)
		self.label_19.setGeometry(QtCore.QRect(50, 115, 67, 17))
		self.label_19.setObjectName("label_19")
		self.label_18 = QtWidgets.QLabel(self.groupBox_2)
		self.label_18.setGeometry(QtCore.QRect(50, 185, 67, 17))
		self.label_18.setObjectName("label_18")
		self.label_20 = QtWidgets.QLabel(self.groupBox_2)
		self.label_20.setGeometry(QtCore.QRect(50, 255, 67, 17))
		self.label_20.setObjectName("label_20")
		self.label_22 = QtWidgets.QLabel(self.groupBox_2)
		self.label_22.setGeometry(QtCore.QRect(30, 70, 67, 17))
		self.label_22.setObjectName("label_22")
		self.pushButton_choose = QtWidgets.QPushButton(Form)
		self.pushButton_choose.setGeometry(QtCore.QRect(400, 660, 89, 41))
		self.pushButton_choose.setObjectName("pushButton_choose")
		self.label_23 = QtWidgets.QLabel(Form)
		self.label_23.setGeometry(QtCore.QRect(520, 560, 141, 41))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.label_23.setFont(font)
		self.label_23.setObjectName("label_23")
		self.pushButton_js = QtWidgets.QPushButton(Form)
		self.pushButton_js.setGeometry(QtCore.QRect(610, 660, 89, 41))
		self.pushButton_js.setObjectName("pushButton_js")
		self.pushButton_js.clicked.connect(self.js_click)
		self.groupBox_2.raise_()
		self.groupBox.raise_()
		self.label.raise_()
		self.label_2.raise_()
		self.label_3.raise_()
		self.textEdit_nx.raise_()
		self.textEdit_pl.raise_()
		self.label_4.raise_()
		self.label_5.raise_()
		self.textEdit_gz.raise_()
		self.label_6.raise_()
		self.label_7.raise_()
		self.label_8.raise_()
		self.label_9.raise_()
		self.textEdit_lh.raise_()
		self.textEdit_zj.raise_()
		self.textEdit_ms.raise_()
		self.label_10.raise_()
		self.textEdit_ts.raise_()
		self.textEdit_kzg.raise_()
		self.textEdit_kr.raise_()
		self.label_11.raise_()
		self.label_12.raise_()
		self.label_13.raise_()
		self.textEdit_aq.raise_()
		self.label_14.raise_()
		self.textEdit_qt.raise_()
		self.label_15.raise_()
		self.label_16.raise_()
		self.label_17.raise_()
		self.textEdit_cm.raise_()
		self.textEdit_di.raise_()
		self.textEdit_gao.raise_()
		self.textEdit_zhong.raise_()
		self.label_21.raise_()
		self.comboBox_zh.raise_()
		self.comboBox_jy.raise_()
		self.pushButton_choose.raise_()
		self.label_23.raise_()
		self.pushButton_js.raise_()

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "电梯困人概率计算模型"))
		self.label.setText(_translate("Form", "是否召回"))
		self.label_2.setText(_translate("Form", "自动救援"))
		self.label_3.setText(_translate("Form", "使用频率(万次/年)"))
		self.label_4.setText(_translate("Form", "使用年限"))
		self.label_5.setText(_translate("Form", "配置管理人员"))
		self.label_6.setText(_translate("Form", "故障率(次/年)"))
		self.label_7.setText(_translate("Form", "机房降温设施"))
		self.label_8.setText(_translate("Form", "底坑潮湿"))
		self.label_10.setText(_translate("Form", "困人次数(年)"))
		self.label_11.setText(_translate("Form", "主机不合格项"))
		self.label_12.setText(_translate("Form", "量化考核分"))
		self.label_13.setText(_translate("Form", "投诉次数(年)"))
		self.label_14.setText(_translate("Form", "其它不合格项"))
		self.label_15.setText(_translate("Form", "门锁不合格项"))
		self.label_16.setText(_translate("Form", "控制柜不合格项"))
		self.label_17.setText(_translate("Form", "层门数"))
		self.label_21.setText(_translate("Form", "电梯困人概率计算模型"))
		self.groupBox.setTitle(_translate("Form", "输入参数"))
		self.groupBox_2.setTitle(_translate("Form", "输出"))
		self.label_19.setText(_translate("Form", "高"))
		self.label_18.setText(_translate("Form", "中"))
		self.label_20.setText(_translate("Form", "低"))
		self.label_22.setText(_translate("Form", "困人概率"))
		self.pushButton_choose.setText(_translate("Form", "选择模型"))
		self.label_23.setText(_translate("Form", "BP神经网络"))
		self.pushButton_js.setText(_translate("Form", "计算"))

	def js_click(self):
		self.textEdit_gao.setPlainText('')
		self.textEdit_zhong.setPlainText('')
		self.textEdit_di.setPlainText('')

		if self.comboBox_zh.currentText() == '有':
			zh = 1.0
		else:
			zh = 0.0
		if self.comboBox_jy.currentText() == '有':
			jy = 1.0
		else:
			jy = 0.0
		if self.comboBox_jw.currentText() == '有':
			jw = 1.0
		else:
			jw = 0.0
		if self.comboBox_dk.currentText() == '有':
			dk = 1.0
		else:
			dk = 0.0
		if self.comboBox_gl.currentText() == '有':
			gl = 1.0
		else:
			gl = 0.0
		inputdata = [float(self.textEdit_cm.toPlainText()), zh, jy, float(self.textEdit_nx.toPlainText()),
		             float(self.textEdit_pl.toPlainText()),
		             jw, dk, gl, float(self.textEdit_gz.toPlainText()), float(self.textEdit_lh.toPlainText()),
		             float(self.textEdit_ts.toPlainText()), float(self.textEdit_kr.toPlainText()),
		             float(self.textEdit_zj.toPlainText()),
		             float(self.textEdit_kzg.toPlainText()), float(self.textEdit_aq.toPlainText()),
		             float(self.textEdit_ms.toPlainText()),
		             float(self.textEdit_qt.toPlainText())]
		with open('data.csv', 'w', newline='') as data2csv:
			# data2csv = open('data.csv', 'a', newline='')
			csv_write = csv.writer(data2csv, dialect='excel')
			csv_write.writerow(inputdata)
			data2csv.close()

		evaluation_data = list(qt5_data_loader.load_data("data.csv"))
		net = network2.load('dtbp_net.json')
		out = net.feedforward(evaluation_data[0]).tolist()
		risk = out.index(max(out))
		if risk == 0:
			self.textEdit_gao.setText('1')
			self.textEdit_zhong.setText('0')
			self.textEdit_di.setText('0')
		elif risk == 1:
			self.textEdit_gao.setText('0')
			self.textEdit_zhong.setText('1')
			self.textEdit_di.setText('0')
		elif risk == 2:
			self.textEdit_gao.setText('0')
			self.textEdit_zhong.setText('0')
			self.textEdit_di.setText('1')

	def choose_click(self):
		pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
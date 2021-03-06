from PyQt5 import QtCore, QtGui, QtWidgets

class _qline(QtWidgets.QFrame):
    """Creates a line widget"""
    def __init__(self):
        super(_qline, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)

class main_ui(object):

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 600)

        # create central widget and layout
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.central_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.central_layout.setObjectName("central_layout")

        # create main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.main_layout.addWidget(QtWidgets.QLabel("mBCI Lab v0.0.1"))

        # main layout: plot widget
        self.plt = GraphicsLayoutWidget()
        self.plt.setAutoFillBackground(False)
        self.plt.setStyleSheet("border: 1px;")
        self.plt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plt.setLineWidth(0)
        self.plt.setMinimumWidth(600)
        self.plt.setObjectName("plt")
        self.main_layout.addWidget(self.plt)
        
        # main layout: console log
        self.tBrowser_Log = QtWidgets.QTextBrowser()
        self.tBrowser_Log.setFixedHeight(120)
        self.tBrowser_Log.setObjectName("tBrowser_Log")
        self.main_layout.addWidget(self.tBrowser_Log)
        self.tBrowser_Log.append("mBCI Lab is a fork of RTGraph and a real-time graphing program for the mBCI project.\nIts purpose is to plot neural signals in real time.\nIt can also be used for any single-time-domain, serial-port device.\nLink to mBCI project: https://github.com/chanhakim/mbci")
        self.tBrowser_Log.append("-------------------------")


        # create control layout
        self.control_layout = QtWidgets.QVBoxLayout()
        self.control_layout.setObjectName("control_layout")
        empty = QtWidgets.QLabel()
        empty.setFixedWidth(140)
        self.control_layout.addWidget(empty)

        # control layout: view options label
        self.qLabel_ViewOptions = QtWidgets.QLabel("View Options")
        self.qLabel_ViewOptions.setObjectName("qLabel_ViewOptions")
        self.qLabel_ViewOptions.setAlignment(QtCore.Qt.AlignCenter)
        self.control_layout.addWidget(self.qLabel_ViewOptions)

        # control layout: start button
        self.pButton_Start = QtWidgets.QPushButton("Start")
        self.pButton_Start.setObjectName("pButton_Start")
        self.control_layout.addWidget(self.pButton_Start)

        # control layout: stop button
        self.pButton_Stop = QtWidgets.QPushButton("Stop")
        self.pButton_Stop.setObjectName("pButton_Stop")
        self.control_layout.addWidget(self.pButton_Stop)

        self.control_layout.addWidget(_qline()) # hline separator

        # control layout: record options label
        self.qLabel_RecordOptions = QtWidgets.QLabel("Record Options")
        self.qLabel_RecordOptions.setObjectName("qLabel_RecordOptions")
        self.qLabel_RecordOptions.setAlignment(QtCore.Qt.AlignCenter)
        self.control_layout.addWidget(self.qLabel_RecordOptions)

        # control layout: plot sample no. spin box
        self.sBox_Seconds = QtWidgets.QSpinBox()
        self.sBox_Seconds.setObjectName("sBox_Seconds")
        self.sBox_Seconds.setMinimum(0)
        self.sBox_Seconds.setMaximum(3600)
        self.sBox_Seconds.setProperty('value', 0)
        self.control_layout.addWidget(self.sBox_Seconds)

        # control layout: record button
        self.pButton_Record = QtWidgets.QPushButton("Record")
        self.pButton_Record.setObjectName("pButton_Record")
        self.control_layout.addWidget(self.pButton_Record)

        # control layout: save button
        self.pButton_Save = QtWidgets.QPushButton("Save")
        self.pButton_Save.setObjectName("pButton_Save")
        self.control_layout.addWidget(self.pButton_Save)

        self.control_layout.addWidget(_qline()) # hline separator

        # control layout: BCI options label
        self.qLabel_BCIOptions = QtWidgets.QLabel("BCI/Plot Options")
        self.qLabel_BCIOptions.setObjectName("qLabel_BCIOptions")
        self.qLabel_BCIOptions.setAlignment(QtCore.Qt.AlignCenter)
        self.control_layout.addWidget(self.qLabel_BCIOptions)

        # control layout: port id combo box
        self.cBox_Port = QtWidgets.QComboBox()
        self.cBox_Port.setObjectName("cBox_Ports")
        self.cBox_Port.addItem("Ports (Refresh)")
        self.cBox_Port.setFixedWidth(140)
        self.control_layout.addWidget(self.cBox_Port)

        # control layout: baud rate combo box
        self.cBox_BaudRate = QtWidgets.QComboBox()
        self.cBox_BaudRate.setObjectName("cBox_BaudRate")
        self.cBox_BaudRate.addItems([str(num) for num in ["Baud Rate", 9600, 14400, 19200, 38400, 115200]])
        self.cBox_BaudRate.setFixedWidth(140)
        self.control_layout.addWidget(self.cBox_BaudRate)

        # control layout: plot sample no. spin box
        self.sBox_Samples = QtWidgets.QSpinBox()
        self.sBox_Samples.setObjectName("sBox_Samples")
        self.sBox_Samples.setMinimum(2)
        self.sBox_Samples.setMaximum(100000)
        self.sBox_Samples.setProperty('value', 1000)
        self.control_layout.addWidget(self.sBox_Samples)

        self.control_layout.addWidget(_qline()) # hline separator

        # control layout: record button
        self.pButton_Help = QtWidgets.QPushButton("Help")
        self.pButton_Help.setObjectName("pButton_Help")
        self.control_layout.addWidget(self.pButton_Help)

        self.control_layout.addStretch() # add stretch to bottom of controls

        # add main and control widgets to central
        self.central_layout.addLayout(self.main_layout)
        self.central_layout.addLayout(self.control_layout)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mbci_lab"))
        self.pButton_Start.setText(_translate("MainWindow", "Start"))
        self.pButton_Stop.setText(_translate("MainWindow", "Stop"))
        self.pButton_Record.setText(_translate("MainWindow", "Record"))
        self.pButton_Help.setText(_translate("MainWindow", "Help"))
        self.pButton_Save.setText(_translate("MainWindow", "Save"))
        self.sBox_Samples.setSuffix(_translate("MainWindow", " Samples"))
        self.sBox_Seconds.setSuffix(_translate("MainWindow", " Seconds"))


from pyqtgraph import GraphicsLayoutWidget

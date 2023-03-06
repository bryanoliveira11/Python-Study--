# Form implementation generated from reading ui file 'NotUsable_at_EXE\bkp_ui\design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_PytubeDownloader(object):
    def setupUi(self, PytubeDownloader):
        PytubeDownloader.setObjectName("PytubeDownloader")
        PytubeDownloader.resize(871, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("NotUsable_at_EXE\\bkp_ui\\../../imgs/icons8-youtube-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        PytubeDownloader.setWindowIcon(icon)
        PytubeDownloader.setStyleSheet("background-color: #fff;")
        PytubeDownloader.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.Main = QtWidgets.QWidget(parent=PytubeDownloader)
        self.Main.setStyleSheet("color:#fff;")
        self.Main.setObjectName("Main")
        self.gridLayout = QtWidgets.QGridLayout(self.Main)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.Main)
        self.frame.setEnabled(True)
        self.frame.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.frame.setStyleSheet("background-color:#fff;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 80, 627, 95))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.url_info = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.url_info.setStyleSheet("margin-bottom: 7px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"")
        self.url_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.url_info.setObjectName("url_info")
        self.gridLayout_2.addWidget(self.url_info, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.Url_Input = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.Url_Input.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.Url_Input.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Url_Input.setAutoFillBackground(False)
        self.Url_Input.setStyleSheet("background:#657683;\n"
"margin-left: 15px;\n"
"margin-right: 15px;\n"
"margin-bottom:12px;\n"
"border-radius: 4px;\n"
"color: #eee;\n"
"font: 12pt \"Segoe UI Historic\";\n"
"padding: 1px")
        self.Url_Input.setText("")
        self.Url_Input.setFrame(True)
        self.Url_Input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Url_Input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Url_Input.setClearButtonEnabled(False)
        self.Url_Input.setObjectName("Url_Input")
        self.gridLayout_2.addWidget(self.Url_Input, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 0, 451, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.python_ico = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.python_ico.setStyleSheet("margin-left:16px;")
        self.python_ico.setText("")
        self.python_ico.setPixmap(QtGui.QPixmap("NotUsable_at_EXE\\bkp_ui\\../../imgs/icons8-python-70.png"))
        self.python_ico.setObjectName("python_ico")
        self.gridLayout_3.addWidget(self.python_ico, 0, 1, 1, 2)
        self.app_title = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.app_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.app_title.setStyleSheet("font: 63 20pt \"Sitka Heading Semibold\";\n"
"color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.522727 rgba(84, 155, 255, 255), stop:0.710227 rgba(77, 131, 230, 255));\n"
"border-radius:11px;\n"
"margin-left:15px;\n"
"margin-top:5px;\n"
"margin-bottom:5px;\n"
"padding-right:12px;\n"
"padding-left:12px;\n"
"")
        self.app_title.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.app_title.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.app_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.app_title.setObjectName("app_title")
        self.gridLayout_3.addWidget(self.app_title, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setGeometry(QtCore.QRect(-30, 60, 831, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.line.setPalette(palette)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btnDownloadOptions = QtWidgets.QPushButton(parent=self.frame)
        self.btnDownloadOptions.setEnabled(True)
        self.btnDownloadOptions.setGeometry(QtCore.QRect(370, 460, 71, 71))
        self.btnDownloadOptions.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDownloadOptions.setStyleSheet("")
        self.btnDownloadOptions.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("NotUsable_at_EXE\\bkp_ui\\../../imgs/icons8-forward-button-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDownloadOptions.setIcon(icon1)
        self.btnDownloadOptions.setIconSize(QtCore.QSize(50, 50))
        self.btnDownloadOptions.setFlat(False)
        self.btnDownloadOptions.setObjectName("btnDownloadOptions")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 220, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.video_thumb = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.video_thumb.setStyleSheet("")
        self.video_thumb.setText("")
        self.video_thumb.setScaledContents(False)
        self.video_thumb.setObjectName("video_thumb")
        self.gridLayout_5.addWidget(self.video_thumb, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(697, 130, 61, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.btnSearchVideo = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.btnSearchVideo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSearchVideo.setStyleSheet("")
        self.btnSearchVideo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("NotUsable_at_EXE\\bkp_ui\\../../imgs/icons8-magnifying-glass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSearchVideo.setIcon(icon2)
        self.btnSearchVideo.setIconSize(QtCore.QSize(64, 26))
        self.btnSearchVideo.setObjectName("btnSearchVideo")
        self.gridLayout_7.addWidget(self.btnSearchVideo, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(300, 230, 471, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.video_title = QtWidgets.QTextBrowser(parent=self.gridLayoutWidget_2)
        self.video_title.setEnabled(True)
        self.video_title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.video_title.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.video_title.setObjectName("video_title")
        self.gridLayout_6.addWidget(self.video_title, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 400, 131, 71))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.video_type = QtWidgets.QTextBrowser(parent=self.gridLayoutWidget_4)
        self.video_type.setStyleSheet("")
        self.video_type.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.video_type.setObjectName("video_type")
        self.gridLayout_4.addWidget(self.video_type, 0, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(150, 400, 121, 71))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.video_qtd = QtWidgets.QTextBrowser(parent=self.gridLayoutWidget_5)
        self.video_qtd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.video_qtd.setObjectName("video_qtd")
        self.gridLayout_9.addWidget(self.video_qtd, 1, 0, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 751, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Exception_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Exception_Layout.setContentsMargins(0, 0, 0, 0)
        self.Exception_Layout.setObjectName("Exception_Layout")
        self.Url_Exception = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_3)
        self.Url_Exception.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Url_Exception.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Url_Exception.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Url_Exception.setObjectName("Url_Exception")
        self.Exception_Layout.addWidget(self.Url_Exception)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(parent=self.frame)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(0, 539, 71, 41))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.txtgithub = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.txtgithub.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.txtgithub.setStyleSheet("text-decoration:none;")
        self.txtgithub.setOpenExternalLinks(True)
        self.txtgithub.setObjectName("txtgithub")
        self.gridLayout_8.addWidget(self.txtgithub, 0, 2, 1, 1)
        self.githubgif = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.githubgif.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.githubgif.setText("")
        self.githubgif.setOpenExternalLinks(True)
        self.githubgif.setObjectName("githubgif")
        self.gridLayout_8.addWidget(self.githubgif, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        PytubeDownloader.setCentralWidget(self.Main)
        self.btnSearchVideo.setStyleSheet(open(r'css\style.css').read())
        self.btnDownloadOptions.setStyleSheet(open(r'css\style.css').read())
        self.video_type.setStyleSheet(open(r'css\style.css').read())
        self.video_qtd.setStyleSheet(open(r'css\style.css').read())
        self.video_title.setStyleSheet(open(r'css\style.css').read()) 
        self.Url_Exception.setStyleSheet(open(r'css\style.css').read()) 
        self.txtgithub.setStyleSheet(open(r'css\style.css').read())
        self.retranslateUi(PytubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(PytubeDownloader)

    def retranslateUi(self, PytubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        PytubeDownloader.setWindowTitle(_translate("PytubeDownloader", "Youtube Downloader"))
        self.app_title.setText(_translate("PytubeDownloader", "PYVIDEO DOWNLOADER"))
        self.txtgithub.setText(_translate("PytubeDownloader", "GitHub"))
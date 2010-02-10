#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from windowfiltersettings.ui on Wed Jul 22 16:57:56 2009
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.triggerRegexLineEdit = KLineEdit(Form)
        self.triggerRegexLineEdit.setUrlDropsEnabled(False)
        self.triggerRegexLineEdit.setProperty("showClearButton", QtCore.QVariant(True))
        self.triggerRegexLineEdit.setObjectName("triggerRegexLineEdit")
        self.verticalLayout.addWidget(self.triggerRegexLineEdit)
        self.kseparator = KSeparator(Form)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n("Form"))
        self.label.setText(kdecore.i18n("Only trigger in windows with title matching:"))
        self.triggerRegexLineEdit.setToolTip(kdecore.i18n("Window title"))
        self.triggerRegexLineEdit.setWhatsThis(kdecore.i18n("Enter a regular expression that matches the title of windows in which you want this item to trigger."))

from PyKDE4.kdeui import KSeparator, KLineEdit
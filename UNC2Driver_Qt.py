# coding:utf-8
from __future__ import division,print_function

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-05-12 11:31:30'

"""

"""

import os
from PySide.QtGui import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QApplication


class SetDriverDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super(SetDriverDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle(u"X盘 映射工具")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.Path_Get = QWidget()
        path_layout = QHBoxLayout()
        path_layout.setContentsMargins(0, 0, 0, 0)
        self.Path_Get.setLayout(path_layout)

        self.label = QLabel(u"获取本地路径")
        self.edit = QLineEdit()
        self.button = QPushButton(u"获取路径")

        path_layout.addWidget(self.label)
        path_layout.addWidget(self.edit)
        path_layout.addWidget(self.button)

        self.Execute_BTN = QPushButton(u"映射 X 盘")

        layout.addWidget(self.Path_Get)
        layout.addWidget(self.Execute_BTN)

        self.button.clicked.connect(self.getPath)
        self.Execute_BTN.clicked.connect(self.unc2XDriver)

    def getPath(self):
        directory = QFileDialog.getExistingDirectory(self, u"获取目录")
        self.edit.setText(directory)

    def unc2XDriver(self):
        directory = os.path.realpath(self.edit.text())
        if not os.path.exists(directory):
            QMessageBox.warning(self, u"警告", u"%s - 路径不存在" % directory)
            return

        os.system(r"subst X: /D")
        command = r"subst X: %s" % directory
        val = os.system(command)
        if val != 0:
            QMessageBox.warning(self, u"警告", u"%s" % val)
            return

        user_path = os.path.expanduser('~')
        startup_path = os.path.join(
            user_path, r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
        if os.path.exists(startup_path):
            bat_path = os.path.join(startup_path, "substXDriver.bat")
            with open(bat_path, 'w', encoding="utf-8") as f:
                f.write(command)

        QMessageBox.warning(self, u"通知", u"%s - 映射成功" % directory)


if __name__ == "__main__":
    app = QApplication([])
    dialog = SetDriverDialog()
    dialog.show()
    app.exec_()

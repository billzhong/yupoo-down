# -*- coding: utf-8 -*-

"""
这个文件是pyqt5的UI界面
"""

from PyQt5.QtCore import pyqtSlot
#from PyQt5 import QtCore.pyqtSlot as pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Ui_yupoo_down_ui import Ui_MainWindow
import webbrowser
import yupoo_down_main
from yupoo_down_main import download_main
import json
import requests



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    主窗口的信号槽实现，方法实现
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.SID = ''

    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.lineEdit.setText("")
    
    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.lineEdit.setText(p0)
        #global SID
        self.SID = self.lineEdit.text()
        self.textBrowser.append("已经添加SID为：" + self.SID)
        #print(SID)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        如何获取SID  按钮功能；打卡一个网址
        """
        webbrowser.open('http://www.rxx0.com', new=0, autoraise=True)

        
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        生成下载列表按钮
        """
        ssssid = self.SID
        if ssssid != '':
            self.textBrowser.append("正在尝试初始化，如果软件卡死，\
则为初始化问题，重新尝试或者找正确的SID")
            d = download_main(ssssid)
            self.textBrowser.append("初始化没有遇到问题")  
            d.get_all_albun_photo()
            self.textBrowser.append("下载列表已经生成")  
        else:
            self.textBrowser.append("请添加SID！！！")

    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        启动aria2 下载
        """

        d_server = self.lineEdit_2.text()
        #download_url = "https://coding.net/u/mofiter/p/public_files\
        #/git/raw/master/go_to_bottom_button.png"
        with open('urls.txt') as f:
            for line in f.readlines():
                line = line.rstrip('\n')
                json_rpc = json.dumps({
                    'id': '',
                    'jsonrpc': '2.0',
                    'method': 'aria2.addUri',
                    'params': [[line]]
                    })
                response = requests.post(url=d_server, data=json_rpc)
                self.textBrowser.append(str(response))

    @pyqtSlot()
    def on_actionguany_triggered(self):
        """
        关于
        """
        QMessageBox.information(self, '关于Yupoo down', 'Yupoo 是著名的国内云\
相册服务商，前几日 Yupoo 发来公告说将要在明年关闭服务，而本月 28 日将关闭注册、\
上传等通道，于是在官网备份客户端出来之前，我们第三方备份工具已经发布，今天就可以抢先\
一步备份了。\n某些人在上面使用了很长一段时间，用来存一些个人照片。\n注意：仅仅\
为 Yupoo 又拍网关闭服务，其团队很早前就转型云服务提供商，就是又拍云啦（主要产品\
包括 CDN、云存储、直播全套解决方案等等），感兴趣的同学可以去看看。另外花瓣也是\
他们的。\n再注意，由于本月 28 日将关闭注册、上传等功能，不能保证此脚本在此后\
的日子里还可用。')
    
    @pyqtSlot()
    def on_actionopen_triggered(self):
        """
        设置下载文件夹
        """
        pass
    
    @pyqtSlot()
    def on_actionquit_triggered(self):
        """
        退出
        """
        sys.exit(app.exec_())
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    #ui.update_statusx.connect(d.statusx)
    ui.show()
    sys.exit(app.exec_())
    


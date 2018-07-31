# -*- coding: utf-8 -*-
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: makePopup.py
@time: 2018/7/30 11:24
@desc:
'''
from tkinter import *
from tkinter.messagebox import *
from InteractionProgram import builtSystem


class MakePopup(Frame):
    systemglobal = {}

    countrycodes = ('lnlife', 'lnlife1', 'lnlif2', 'lnlife3')
    countrynames = ('环境', '203', '204', '样式', '测试', '看看', '数据')
    filedas = ('Linuxuser', 'Linuxpass')

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.config(bd=2, relieg=GROOVE)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.master.title('标题测试框')
        self.master.iconname("图标名称")
        pass


    def sendGift(self, *args):
        select = self.systemglobal['SelectWidgets']
        var = select.gift
        entrie = self.systemglobal['LoginEntry'].entrie
        if var.get() in self.countrycodes:  # 判断目录是否选中
            username = entrie[self.filedas[0]].get()  # 读取当前输入的账号
            password = entrie[self.filedas[1]].get()  # 读取当前输入的密码
            print("账号密码:", username, password)
            if username and password:
                select.sendGifts(username, password)
            else:
                select.sendGifts("Please enter your account password.")
        else:
            select.sendGifts("Please check the directory you are in.")

    def onPress(self):
        var = self.systemglobal['SelectWidgets'].gift
        print('单选按钮为 : ', var.get())

    def greeting(self):
        builtSystem.greeting()

    def notdone(self):
        builtSystem.notdone()

    def menuQuit(self):
        builtSystem.menuQuit()


demoModules = ['TitleMenu', 'LoginEntry', 'SelectWidgets']
parts = []


def addCpmponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        parts.append(part)


def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part,'report'):
            part.report()
        else:
            print('none')

if __name__ == '__main__':
    # root = Tk()
    # from menuDome2 import NewMenuDemo
    #
    # NewMenuDemo(root)
    # root.mainloop()
    root = Tk()
    Button(root,text = 'ss',command = dumpState).pack(fill = X)
    addCpmponents(root)
    root.mainloop()
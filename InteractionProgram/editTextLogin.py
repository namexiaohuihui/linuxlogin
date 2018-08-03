# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: dengluzhagao.py
@time: 2018/7/31 22:06
@Entry Name:linuxlogin-master
"""
from tkinter import *
from ShowProgram.makePopup import MakePopup
class EditTextLogin(MakePopup):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=TOP,expand=YES, fill=BOTH)  # 缺失path之后，该frame就不会显示出来
        self.systemglobal['LoginEntry'] = self
        self.makeEntryBar()
        pass

    def makeEntryBar(self):
        self.entrie = {}
        entry = Frame(self)
        entry.pack(side=BOTTOM, fill=X)
        for field in self.filedas:
            row = Frame(entry, cursor='hand2', relief=SUNKEN, bd=2)
            lab = Label(row, width=8, text=field)
            ent = Entry(row)
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            # self.entrie.append(lab)
            self.entrie[field] = ent
        # self.bind('<Return>', (lambda event: self.sendGift(self.entrie))) # 绑定键盘事件，这句没什么用先隐藏

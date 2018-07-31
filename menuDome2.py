# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: NewMenuDome.py
@time: 2018/6/26 10:35
@Entry Name:operating
创建一个简易的菜单框，里面设置按钮
"""
from tkinter import *
from tkinter.messagebox import *
from makeRun import MakePopup
from InteractionProgram.loginEntry import LoginEntry
from InteractionProgram.selectWidgets import SelectWidgets
from MenuProgram.titleMenu import TitleMenu


class NewMenuDemo(MakePopup):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # 缺少这个之后，除菜单以外的书都不会显示
        self.createWidgets()
        self.master.title('标题测试框')
        self.master.iconname("图标名称")

    def createWidgets(self):
        TitleMenu()  # 设置菜单
        LoginEntry()  # 设置输入框
        SelectWidgets()  # 设置下拉筛选框

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
import os
import sys
# 获取项目路径下的目录
property_path = r'E:\\linuxlogin'
os.chdir(property_path)
# 将项目路径保存
sys.path.append(property_path)

from InteractionProgram.editTextLogin import EditTextLogin
from InteractionProgram.selectWidgets import SelectWidgets
from InteractionProgram.simpleEditor import SimpleEditor
from MenuProgram.titleMenu import  TitleMenu
demoModules = [TitleMenu, EditTextLogin,SelectWidgets,SimpleEditor]
parts = []


def addCpmponents(root):
    for value in demoModules:
        part = value(root)
        parts.append(part)


def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part,'report'):
            part.report()
        else:
            print('none')

if __name__ == '__main__':
    root = Tk()
    Button(root,text = 'ss',command = dumpState).pack(fill = X)
    addCpmponents(root)
    root.mainloop()
"""
same, but use composition (embedding/attachment) instead of inheritance
"""
import os
import sys
# 获取项目路径下的目录
files_path = 'E:\\linuxlogin'
os.chdir(files_path)
# 将项目路径保存
sys.path.append(files_path)
# import HTMLTestReportCN

# 获取当前文件所在目录
CUR_PATH = os.path.dirname(os.path.realpath(__file__))
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog   import asksaveasfilename
from DemoTest.quitter  import Quitter
from DemoTest.scrolledtext import ScrolledText                     # here, not Python's

class SimpleEditor(Frame):                                # see PyEdit for more
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        self.pack()
        frm = Frame(self)
        frm.pack(fill=X)
        Button(frm, text='Save保存',  command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut剪切',   command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste粘贴', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find查找',  command=self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        self.st = ScrolledText(self, file=file)
        self.st.text.config(font=('courier', 9, 'normal'))

    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.st.gettext()                      # first through last
            open(filename, 'w').write(alltext)            # store text in file

    def onCut(self):
        text = self.st.text.get(SEL_FIRST, SEL_LAST)         # error if no select
        self.st.text.delete(SEL_FIRST, SEL_LAST)             # should wrap in try
        self.clipboard_clear()
        self.clipboard_append(text)

    def onPaste(self):                                    # add clipboard text
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.st.text.insert(INSERT, text)
        except TclError:
            pass                                          # not to be pasted

    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.st.text.search(target, INSERT, END)  # from insert cursor
            if where:                                      # returns an index
                print(where)
                pastit = where + ('+%dc' % len(target))    # index past target
               #self.st.text.tag_remove(SEL, '1.0', END)      # remove selection
                self.st.text.tag_add(SEL, where, pastit)      # select found target
                self.st.text.mark_set(INSERT, pastit)         # set insert mark
                self.st.text.see(INSERT)                      # scroll display
                self.st.text.focus()                          # select text widget

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()    # filename on command line
    else:
        # SimpleEditor().mainloop()                    # or not: start empty
        SimpleEditor(file=r'C:\Users\70486\Desktop\9780596158118\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour\scrolledtext.py').mainloop()                    # or not: start empty

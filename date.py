# 作者 常亮
# 时间：2011年4月30日15:48:47
from tkinter import *
import calendar
from datetime import date


class DateCtrl(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, bg='lightgray')
        self.master = master
        self.master.size = (100, 150)
        self.master.resizable(False, False)
        self.date = date.today()

        self.master.title('我的日历')
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W + E + N + W)
        self.dayid = []
        self.UpdateUI()

    def SetDate(self, date):
        self.date = date
        self.UpdateUI()

    def GetDate(self):
        return self.date

    def MonthBack(self):
        if date == date.min:
            return
        if self.date.month == 1:
            self.date = self.date.replace(year=self.date.year - 1, month=12)
        else:
            if self.date.day > calendar.monthrange(self.date.year, self.date.month - 1)[1]:
                self.date = self.date.replace(month=self.date.month - 1,
                                              day=calendar.monthrange(self.date.year, self.date.month - 1)[1])
            else:
                self.date = self.date.replace(month=self.date.month - 1)
        self.UpdateUI()

    def MonthFoeward(self):
        if date == date.max:
            return
        if self.date.month == 12:
            self.date = self.date.replace(year=self.date.year + 1, month=1)
        else:
            if self.date.day > calendar.monthrange(self.date.year, self.date.month + 1)[1]:
                self.date = self.date.replace(month=self.date.month + 1,
                                              day=calendar.monthrange(self.date.year, self.date.month + 1)[1])
            else:
                self.date = self.date.replace(month=self.date.month + 1)
        self.UpdateUI()

    def UpdateUI(self):
        lendayid = len(self.dayid)
        for i in range(lendayid):
            self.dayid[lendayid - i - 1].destroy()
            del (self.dayid[lendayid - i - 1])
        self.backwardBt = Button(text='<', command=self.MonthBack).grid(row=0, column=0, sticky=W + E + N + S)
        self.YMBtn = Button(text='%d-%d' % (self.date.year, self.date.month), command=lambda sf=self: print(sf.date)).grid(row=0, column=1, columnspan=5, sticky=W + E + N + S)
        self.forwardBt = Button(text='>', command=self.MonthFoeward).grid(row=0, column=6, sticky=W + E + N + S)
        col = 0
        for wk in ['一', '二', '三', '四', '五', '六', '日']:
            Label(text=wk).grid(row=1, column=col, sticky=W + E + N + S)
        col += 1
        row = 2
        col = 0
        today = date.today()
        for weekday in calendar.monthcalendar(self.date.year, self.date.month):
            for dayt in weekday:
                if dayt == 0:
                    col += 1
                    continue
                bkcolour = 'lightgray'
                if col == 5:
                    bkcolour = 'green'
                if col == 6:
                    bkcolour = 'blue'
                if dayt == self.date.day:
                    bkcolour = 'red'
                tdrelief = FLAT
                if self.date.year == today.year \
                    and self.date.month == today.month \
                    and dayt == today.day:
                    tdrelief = GROOVE
            bt = Button(self.master, text='%d' % dayt, relief=tdrelief, bg=bkcolour,
                        command=lambda sf=self, dt=dayt: sf.rpday(dt))
            bt.grid(row=row, column=col, sticky=W + E + N + S)
            self.dayid.append(bt)
            col += 1
        row += 1
        col = 0


def rpday(self, dt):
    self.date = self.date.replace(day=dt)
    self.UpdateUI()


if __name__ == '__main__':
    root = Tk()
    mainfram = DateCtrl(root)
    tdt = date.today()
    mainfram.SetDate(tdt.replace(day=3))  # 试试重置日期
    root.mainloop()

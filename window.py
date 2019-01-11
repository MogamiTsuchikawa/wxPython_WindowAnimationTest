import wx

class win(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title="test")
        self.SetSize(960,540)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.btn = wx.Button(self.panel,-1,label="Push",pos=(0,450))
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.move = False
        self.btn.Bind(wx.EVT_BUTTON,self.OnClick)
    def OnTimer(self,event):
        self.btn.Position = wx.Point(self.btn.GetPosition()[0]+1,self.btn.GetPosition()[1])
    def OnClick(self,event):
        if self.move :
            self.move = False
            self.timer.Stop()
        else:
            self.move = True
            self.timer.Start(1)

win_o = wx.PySimpleApp()
win_f = win(None)
win_f.Show()
win_o.MainLoop()
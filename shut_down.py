import os
# import wx

# class Example(wx.Frame):

#     def __init__(self, parent, title):
#         super(Example, self).__init__(parent, title=title, size=(400, 600))

#         self.InitUI()
#         self.Centre()


#     def InitUI(self):

#         menubar = wx.MenuBar()
#         fileMenu = wx.Menu()
#         menubar.Append(fileMenu, '&File')
#         self.SetMenuBar(menubar)

#         vbox = wx.BoxSizer(wx.VERTICAL)
#         ##self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
#         ##vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
#         gs = wx.GridSizer(4, 1, 5, 5)

#         quitButton = wx.Button(self, label='Quit')
#         quitButton.Bind(wx.EVT_BUTTON, self.onButtonClicked)   
#         #quitButton.SetPosition((200, 500))

#         gs.AddMany([(wx.Button(self, label='10mins'), 0, wx.EXPAND),
#             (wx.Button(self, label='30mins'), 0, wx.EXPAND),
#             (wx.Button(self, label='60mins'), 0, wx.EXPAND)])
#         #gs.Add(quitButton, 0, wx.EXPAND)

#         vbox.Add(gs, proportion=0, flag=wx.EXPAND)
#         self.SetSizer(vbox)  

#         box = wx.BoxSizer(wx.VERTICAL)
#         box.Add(quitButton, wx.ID_ANY, wx.ALIGN_CENTER | wx.ALL, 20)


#     def onButtonClicked(self, e):
#         self.Destroy()

# def main():

#     app = wx.App()
#     ex = Example(None, title='Shutdown App')
#     ex.Show()
#     app.MainLoop()


# if __name__ == '__main__':
#     main()
while True:

    try:
        mins = int(input("Enter how many minutes until shutdown: "))
        secs = mins * 60

        if isinstance(secs, int):

            os.system(f"shutdown /s /t {secs}")

            if mins > 60:
                hours = mins // 60
                remainder = mins % 60
                print(f"The computer will shutdown in {hours} hours and {remainder} minutes!")
                break
            else:
                print(f"The computer will shutdown in {mins} minutes!")
                break

    except:
        print("Invalid number...")

while True:
    if input("\nEnter c to cancel: ") == 'c' or 'C':
        os.system("shutdown /a")
        print("Shutdown has been cancelled.")
        break

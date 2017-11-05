import sys
from Tkinter import *
root = tk.Tk()
portList = [None]

var = tk.StringVar(root)

# My frame for form
class simpleform_ap(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.refreshPorts()
        self.initialize()
        self.grid()

    def initialize(self):
        # Dropdown Menu
        optionList = ["Yes","No"]
        self.dropVar=StringVar()
        self.dropVar.set("Yes") # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *optionList,
                                    command=self.func)
        self.dropMenu1.grid(column=1,row=4)

    def getPortList():
        portslist = [None]
        del portslist[:]
        i=0
        ports = ['COM%s' % (i + 1) for i in range(256)]
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                portslist.append(port)
            except (OSError, serial.SerialException):
                pass
        return portslist

    def refreshPorts(self):
        var.set('')
        portSelect['menu'].delete(0, 'end')
        newPortList = getPortList()
        for port in newPortList:
            portSelect['menu'].add_command(label=port, command=tk._setit(var, port))
    def func(self,value):
        print value


def create_form(argv):
    global var
    form = simpleform_ap(None)
    form.title('My form')
    var = tk.StringVar(root)
    form.mainloop()

if __name__ == "__main__":
    create_form(sys.argv)
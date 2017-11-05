import threading 
from time import sleep
import Tkinter as tk
import sys
import glob
import serial
import time
photo = """
R0lGODdhlABpAOeTAH2ChYCFiIOIi4aIhYSJjIiNkImOkYqPkoyQk42RlI6SlY+TlpGWmJKXmZOY
mpSZm5WanJabnZecnpidn5meoJqfoZugopyho6OgpJ2ipJ6jpaWip5+kpqClqKekqaGmqaKnqqSp
rKWqraarrqyqrqesr62rr66ssKiusKqvsauwsqyxs62ytK6zta+0trC1t7G2uLK3urO4u7S5vLW6
vba7vry6vre8v7i+wLm/wbvAwrzBw73CxL7Dxb/ExsbDyMDFyMHGycLHysPIy8TJzMrIzMXKzczK
zsbMzs3Lz8fNz87M0MnO0MrP0dHO08vQ0tLP1MzR1NPQ1c3S1dTR1s7T1s/U19XT19DV2NfV2dHX
2djW2tLY2tnX29TZ29vY3NXa3NzZ3tbb3d3a39fc397b4Njd4N/c4dne4drf4uDe4tvg4+Hf4+Lg
5Nzi5OPh5d3j5eXi5t/k5ubj6ODl6Ofk6eHm6ejl6uLn6unm6+Po6+Tp7Oro7OXq7evp7ezq7ubs
7u3r7+ft7+/s8enu8PDt8urv8vHu8+vw8/Lv9Ozx9O3y9fPx9e7z9vTy9vXz9+/19/n2+/P4+///
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////ywAAAAAlABpAAAI/gDpCBxI
sKDBgwgTKlzIsKHDhxAjSpxIsaLFixgzatzIsaPHjyBDihxJsqTJkyhTqlzJsqXLlzBjypxJs6bN
mzhz6txJMQ2RHDhw7GBCRg7PoxKrJIAgAUIECyq4wEFKtWEUA1HMeHnyIgINM1XDJoxSgMvANT0c
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
"""	
root = tk.Tk()
portList = [None]
var = tk.StringVar(root)
kg = 0;
items = tk.IntVar()
items.set(0)
closeSerial = False
photo = tk.PhotoImage(data=photo)
root.wm_geometry("248x205+60+60")
root.title("Visualizador")
root.resizable(0,0)
mycolor2 = '#E1E4E9'
root.configure(background=mycolor2)
label = tk.Label(root, image=photo)
label.image = photo  # keep a reference!
label.grid(column=0,row=0)

ser = serial.Serial()
ser.baudrate = 115200
def getPortList():
	portslist = [None]
	del portslist[:]
	i=0
	ports = ['COM%s' % (i + 1) for i in range(64)] #windows
	for port in ports:
	    try:
	        s = serial.Serial(port)
	        s.close()
	        portslist.append(port)
	    except (OSError, serial.SerialException):
	        pass
	return portslist

def refresh():
    var.set('')
    connect_but_text.set("Abrir")
    portSelect['menu'].delete(0, 'end')
    newPortList = getPortList()
    for port in newPortList:
        portSelect['menu'].add_command(label=port, command=tk._setit(var, port))

def openPort():
	global ser
	print "hay que abrir puerto ahora"
	actualport = var.get()
	print actualport
	try:
		ser = serial.Serial(
		port = actualport,
		baudrate = 115200,
		bytesize = serial.EIGHTBITS, 
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE, 
		timeout = 1,
		xonxoff = False,
		rtscts = False,
		dsrdtr = False,
		writeTimeout = 2
		)
		if(getReadings.isAlive() == False):
			getReadings.start()
	except Exception, e1:
		print ("error communicating...: ") + str(e1)

def closePort():
	global closeSerial
	closeSerial = True
	print "hay que cerrar puerto ahora"
	#ser.close()

def changePort():
	global ser
	if(ser.isOpen()== False):
		connect_but_text.set("Cerrar")
		openPort()
	else:
		connect_but_text.set("Abrir")
		closePort()


def getReadings():
	global kg,ser,closeSerial
	while(True):
		if(ser.isOpen()== True):
			read = ser.readline(2000)
			try:
				read_int = int(read)
				items.set(read_int)
				#print read
			except:
				print "Read serial timeout"
			#
			if(closeSerial == True):
				closeSerial = False
				items.set(0)
				ser.close()
		else:
			refresh()
			sleep(5)
		

items.set(kg) #para cambiar valor
portSelect = tk.OptionMenu(root, var, *portList)
portSelect.grid(column=0,row=1,padx=(0,50),pady=(10,0))
connect_but_text = tk.StringVar()
connect_but = tk.Button(root, textvariable=connect_but_text, command=changePort).grid(column=0,row=1,padx=(70,0),pady=(10,0))
value = tk.Label(root, textvariable=items,font=("ubuntu", 11),fg='#808182',bg='#eff0f4').grid(column=0,row=0,padx=(0,10),pady=(1,5))
#Refrescar todos los puertos al abrir
refresh()
getReadings = threading.Thread(target=getReadings)

root.mainloop()





import serial
import threading
import Queue
import Tkinter as tk


class SerialThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        s = serial.Serial('COM21',115200)
        while True:
            if s.inWaiting():
                text = s.readline(s.inWaiting())
                self.queue.put(text)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        var = tk.StringVar(self)
        self.geometry("600x400")
        frameLabel = tk.Frame(self, padx=40, pady =40)
        self.text = tk.Text(frameLabel, wrap='word', font='TimesNewRoman 15',
                            bg=self.cget('bg'), relief='flat')
        frameLabel.pack()
        self.text.pack()
        self.queue = Queue.Queue()
        thread = SerialThread(self.queue)
        thread.start()
        self.process_serial()
        portSelect = tk.OptionMenu(frameLabel, var, "hola","hola")
        portSelect.grid(column=0,row=1,padx=(70,0),pady=(10,0))
        
    def process_serial(self):
        while self.queue.qsize():
            try:
                self.text.delete(1.0, 'end')
                self.text.insert('end', self.queue.get())
            except Queue.Empty:
                pass
        self.after(100, self.process_serial)

app = App()
app.mainloop()
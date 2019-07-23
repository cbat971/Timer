from tkinter import *
from tkinter import ttk 

root = Tk()

counter = 0
def counter_label(label):
	def count_time():
		global counter 
		counter += 1
		the_time.config(text=str(counter))
		the_time.after(100, count_time)
	count_time()


content = ttk.Frame(root)
millisecvar = BooleanVar()
secondsvar = BooleanVar()
minutesvar = BooleanVar()
millisecvar.set(True)
secondsvar.set(False)
minutesvar.set(False)
millisec = ttk.Checkbutton(content, text="Milliseconds", 
	variable=millisecvar, onvalue=True)
seconds = ttk.Checkbutton(content, text="Seconds", 
	variable=secondsvar, onvalue=True)
minutes = ttk.Checkbutton(content, text="Minutes", 
	variable=minutesvar, onvalue=True)
the_time = ttk.Label(content)

the_time.grid(column=0, row=0)


start = ttk.Button(content, text="Start")
pause = ttk.Button(content, text="Pause")
counter_label(counter)

content.grid(column=0, row=0)
millisec.grid(column=1, row=0)
seconds.grid(column=1, row=1)
minutes.grid(column=1, row=2)
start.grid(column=0, row=3)
pause.grid(column=1, row=3)


root.mainloop()
import tkinter as ui

#time module to update the current time
import time

#create new window
window = ui.Tk()

#function to update time every second
def update_clock():
    hours= time.strftime("%I")
    minutes= time.strftime("%M")
    seconds= time.strftime("%S")
    am_or_pm= time.strftime("%p")
    time_text= hours + ":" + minutes + ":" + seconds + ":" + am_or_pm
    digital_clock_lbl.config(text=time_text)
    #we want label to be updated every second so we use after function it means after 1000 millisec= 1 sec 
    #we will be calling update function
    digital_clock_lbl.after(1000, update_clock)

#label in window
digital_clock_lbl = ui.Label(window, text="00:00:00", font="Helvetica 72 bold")
digital_clock_lbl.pack()

update_clock()

window.mainloop()


import tkinter as ui

#time module to update the current time
import time
import math

#create new window
window = ui.Tk()

#set the size of the window
window.geometry("360x360")

#function to update time every second
def update_clock():
    hours= int(time.strftime("%I"))
    minutes= int(time.strftime("%M"))
    seconds= int(time.strftime("%S"))

    #updating seconds hand per second
    seconds_x= seconds_hand_len* math.sin(math.radians(seconds*6)) + center_x
    seconds_y= -1*seconds_hand_len*math.cos(math.radians(seconds*6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    #updating minutes hand per minute
    minutes_x= minutes_hand_len* math.sin(math.radians(minutes*6)) + center_x
    minutes_y= -1*minutes_hand_len*math.cos(math.radians(minutes*6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    #updating hours hand per hour
    hours_x= hours_hand_len* math.sin(math.radians(hours*30)) + center_x
    hours_y= -1*hours_hand_len*math.cos(math.radians(hours*30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)
    

    window.after(1000, update_clock)
    
#whenever we want to drawing this in py we need to create canvas
canvas = ui.Canvas(window, width=360, height=360,bg="white")
canvas.pack(expand= True, fill='both')

#now we load our clock dail image
bg= ui.PhotoImage(file='analog_300.png')
canvas.create_image(180,180, image=bg)

#create clock hands
center_x= 180
center_y= 180
seconds_hand_len= 95
minutes_hand_len= 80
hours_hand_len= 60

#drawing clock hands
seconds_hand= canvas.create_line(180, 180, 180 + seconds_hand_len, 180 +seconds_hand_len,
                                 width=1.5, fill='red')

#minute hand
minutes_hand= canvas.create_line(180, 180, 180 + minutes_hand_len, 180 +minutes_hand_len,
                                 width=2, fill='black')

#hour hand
hours_hand= canvas.create_line(180, 180, 180 + hours_hand_len, 180 +hours_hand_len,
                                 width=4, fill='black')

update_clock()

window.mainloop()

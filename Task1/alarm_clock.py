from playsound import playsound
import os
import time
import datetime
import pygame
import tkinter as tk
from PIL import ImageTk , Image



root = tk.Tk()

root.title("Alarm Clock")
root.geometry("320x600")

CLEAR_AND_RETURN = "\033[H" # for clear screen every second and rewrite the content again
CLEAR = "\033[2J" # same as the previous

#--------------------- functions -------------------------- 

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_lab.config(text=current_time)
    root.after(1000, update_time)  # Update every 1 second (1000 milliseconds)

def add_alarms():
    alarm_time = f"{dt_hour.get()}:{dt_min.get()}"
    alarm_lists.insert(tk.END,alarm_time)
    dt_hour.delete(0, tk.END)
    dt_min.delete(0, tk.END)
    # dt_sec.delete(0, tk.END)

def remove_alarm():
    selected_index = alarm_lists.curselection()
    if selected_index:
        alarm_lists.delete(selected_index)

def check_alarms():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for i in range(alarm_lists.size()):
        alarm_time = alarm_lists.get(i)
        if current_time == alarm_time:
            win = tk.Toplevel(root)
            win.title('Trigger')
            tk.Label(
                win,
                image=alarm_icon,
            ).pack(expand=True,padx=30,pady=10)

            tk.Button(
                win,
                text='STOP',
                font=('consolas',25,'bold'),
                bg='red',
                fg='white',
                command= lambda : pygame.mixer_music.stop()

            ).pack(expand=True,fill='both')

            pygame.init()
            pygame.mixer.music.load('Task1/alarm.mp3')
            pygame.mixer_music.play(loops=3)

            

            alarm_lists.delete(i)
            print(f"Alarm triggered at {alarm_time}")
    root.after(1000, check_alarms)



#-------------- functions ---------------

# clock frame 
clock_frame = tk.Frame(
    root,
)
clock_frame.pack(side='top',pady=8,expand=True,fill='both')
    

# icon to add alarm
add_icon = tk.PhotoImage(file='Task1/plus.png')
remove_icon = tk.PhotoImage(file='Task1/cancel.png')
alarm_icon = tk.PhotoImage(file = r'Task1\alarm.png')


cur_time = tk.Label(
    clock_frame,
    text = 'Our Clock',
    font=('Cairo' , 20 ,'bold'),
    bg='#ED7D31',
    fg='black',
    pady=10
)
cur_time.pack(side='top',expand=True,fill='both',padx=5)

time_lab = tk.Label(
    clock_frame , 
    text=f'{datetime.datetime.now().strftime("%H:%M:%S")}',
    font=('consolas',20,'bold'),
    bg='black',
    fg='white',
    pady=30
)
time_lab.pack(fill="both",padx=5,pady=5)

update_time()


# -------------------------

# alarm_frame
alarm_frame = tk.Frame(
    root,
    pady=15,
    padx=15,
    relief='groove',
    borderwidth=2,
    
)
alarm_frame.pack(expand=True,padx=30,pady=5)


dt_hour = tk.Entry(
    alarm_frame,
    width=5,
    font=('consolas',15,'bold'),
    justify='center'
)
dt_hour.grid(row=0,column=0,padx=5)

dt_min =tk.Entry(
    alarm_frame,
    width=5,
    font=('consolas',15,'bold'),
    justify='center'

)
dt_min.grid(row=0,column=1,padx=5)

# dt_sec = tk.Entry(
#     alarm_frame,
#     width=5,
#     font=('consolas',15,'bold'),
#     justify='center'
# )
# dt_sec.grid(row=0,column=2,padx=5)

# --------------------------------

# buttons frame
btns_frame = tk.Frame(
    root,
)
btns_frame.pack(padx=10,pady=10,side='bottom',expand=True)

add_alarm = tk.Button(
    btns_frame , 
    text = "Add Alarm",
    font = ('consolas',15,'bold'),
    bg = '#EEE',
    fg = 'black',
    image = add_icon,
    compound = 'left',
    pady = 10,
    padx = 10,
    relief = 'raised',
    borderwidth = 3 , 
    command = add_alarms
)
add_alarm.pack(side = 'top' , pady=5)

remove_alarm = tk.Button(
    btns_frame , 
    text = "Remove Alarm",
    font = ('consolas',15,'bold'),
    bg = '#EEE',
    fg = 'black',
    image = remove_icon,
    compound = 'left',
    pady = 10,
    padx = 10,
    relief = 'raised',
    borderwidth = 3 , 
    command = remove_alarm 
)
remove_alarm.pack(side = 'bottom')

alarm_lists = tk.Listbox(
    root,
    width = 20,
    height = 50,
    relief = 'groove',
    font = ('Cairo',15,'bold'),
    # cursor='tab',
    highlightcolor = 'green',
    xscrollcommand = True
)
alarm_lists.pack(padx=10)
# alarm_lists.insert(tk.END,'12:10:12')

check_alarms()



root.mainloop()


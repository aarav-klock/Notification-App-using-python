from tkinter import *
from tkinter import ttk
import random
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time



t = Tk()
t.title('Reminder App')
t.geometry("800x500")
t.iconbitmap(r"ico.ico")


#Image
notifier_img = ImageTk.PhotoImage(Image.open("notify_label.png"))
label = Label(t, image = notifier_img)
label.pack()


#Greeting
def greeting():
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    if curr_time < "12:00":
        return("Good Morning!")
    elif curr_time >= "12:00" and curr_time < "16:00":
        return("Good Afternoon!")
    else:
        return("Good Evening!")

greeting = Label(t,text = greeting(), font=("Helvetica",14,"bold")).place(x=12,y=70)

reminder_title = Label(t, text = "What do you want to be reminded for?", font=("poppins",12)). place(x=12,y=143)

your_tasks_button = Button(t, text = "Your Tasks >>",font=("",10, "bold"),fg="#ffffff", bg="#528DFF", width=18, relief="raised")
your_tasks_button.place(x=15,y=105)

#Notifier
def get_details():
    get_title = title.get() 
    #get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" and get_time == "":
        messagebox.showerror("Alert","All fields are required!")
    elif get_title == "":
        messagebox.showerror("Alert", "Title is empty, please enter all the details!")
    elif get_time == "":
        messagebox.showerror("Alert", "Time is empty, please enter all the details!")
    else:

        motivational_quotes=["Never put off until tomorrow what you can do today.","We are what we repeatedly do. Excellence then, is not an act, but a habit.","Be humble. Be hungry. And always be the hardest worker in the room.","Work hard and be kind and amazing things will happen.","Hard work beats talent when talent doesn’t work hard.","There are no secrets to success. It is the result of preparation, hard work, and learning from failure.","Perseverance is the hard work you do after you get tired of doing the hard work you already did.","Nothing will work unless you do.","Work hard in silence, let your success be your noise.","You don’t have to see the whole staircase, just take the first step.","You can have it all. You just can’t have it all at once.","If you get tired, learn to rest, not to quit.","Believe you can and you’re halfway there.","It always seems impossible until it’s done.","Progress is impossible without change, and those who cannot change their minds cannot change anything.","What we fear of doing most is usually what we most need to do.","Every accomplishment starts with the decision to try."]
        motivation_index= random.randint(0,len(motivational_quotes)-1)
        output_motivation = motivational_quotes[motivation_index]

        def isTimeCorrect(get_time):
            try:
                time.strptime(get_time, '%H:%M')
                return True
            except ValueError:
                messagebox.showerror("Alert", "Time is invalid, please enter valid time in HH:MM format.")
    


    
        while (isTimeCorrect(get_time)):
            curr_time = str(time.strftime("%H:%M", time.localtime()))
            if curr_time==get_time:
                #print("Yes")
                if __name__=="__main__":
                    notification.notify(title=get_title,
                                message= output_motivation,
                                app_name="Notifier",
                                app_icon="ico.ico",
                                toast=True,
                                timeout=10)
                    time.sleep(7)
                break


def meeting_win():
    new = Toplevel(t)
    new.geometry("800x500")
    new.title("Meeting Schedule")
    new.iconbitmap(r'ico.ico')
        
    global meeting_img
    meeting_img = ImageTk.PhotoImage(Image.open("meeting_schedule.png"))
    label = Label(new, image = meeting_img)
    label.pack()

    flag = 0
    

    # Label - Title
    t_label = Label(new, text="Title to Notify:",font=("poppins", 10))
    t_label.place(x=12, y=100)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=100)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=130)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=130)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=135)


    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

custom_button = ttk.Button(t, text ="Custom Task", command = meeting_win).place(x=12,y=180)

meeting_button = ttk.Button(t, text ="Meeting Schedule", command = meeting_win).place(x=100,y=180)

def workout_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Workout Schedule")
    new.iconbitmap(r'ico.ico')

    global workout_img
    workout_img = ImageTk.PhotoImage(Image.open("workout_schedule.png"))
    label = Label(new, image = workout_img)
    label.pack()

    def show():
        label.config( text = clicked.get() )
    options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    clicked = StringVar()
    clicked.set( "Monday" )
    drop = OptionMenu( new , clicked , *options )
    drop.place(x=180,y=65)

    label = Label( new , text = " " )
    label.pack()

    t_label = Label(new, text="Select Day:",font=("poppins", 10))
    t_label.place(x=12, y=70)


    # Label - Title
    t_label = Label(new, text="Title to Notify:",font=("poppins", 10))
    t_label.place(x=12, y=100)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=100)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=130)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=130)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=135)

    var = IntVar()
    Radiobutton(new, text='Repeat every week', variable=var, value=0).place(x=12,y=175)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

workout_button = ttk.Button(t, text ="Workout Schedule", command = workout_win).place(x=215,y=180)

def medicine_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Medicine Reminder")
    new.iconbitmap(r'ico.ico')

    global medicine_img
    medicine_img = ImageTk.PhotoImage(Image.open("medicine_schedule.png"))
    label = Label(new, image = medicine_img)
    label.pack()

    # Label - Title
    t_label = Label(new, text="Medicine Name:",font=("poppins", 10))
    t_label.place(x=12, y=80)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=80)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=110)

    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=110)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=115)

    Label(new, text="Repeat:", font=('Helvetica 10 bold')).place(x=12,y=135)

    var = IntVar()
    Radiobutton(new, text='Never', variable=var, value=0).place(x=12,y=155)
    Radiobutton(new, text='Every Day', variable=var, value=1).place(x=12,y=175)
    Radiobutton(new, text='Every Week', variable=var, value=2).place(x=12,y=195)
    Radiobutton(new, text='Every Month', variable=var, value=3).place(x=12,y=215)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)
    
medicine_button = ttk.Button(t, text ="Medicine Reminder", command = medicine_win).place(x=330,y=180)

def birthday_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Birthday Reminder")
    new.iconbitmap(r'ico.ico')
    
    global birthday_img
    birthday_img = ImageTk.PhotoImage(Image.open("birthday_schedule.png"))
    label = Label(new, image = birthday_img)
    label.pack()

        # Label - Title
    t_label = Label(new, text="Title to Notify:",font=("poppins", 10))
    t_label.place(x=12, y=100)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=100)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=130)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=130)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=135)

    # Label - Date
    t_label = Label(new, text="Set Date:",font=("poppins", 10))
    t_label.place(x=12, y=160)

    # ENTRY - date
    global date
    date = Entry(new, width="5",font=("poppins", 13))
    date.place(x=123, y=160)

    # Label - day
    time_min_label = Label(new, text="DD/MM", font=("poppins", 10))
    time_min_label.place(x=175, y=165)

    var = IntVar()
    Radiobutton(new, text='Repeat every year', variable=var, value=0).place(x=12,y=200)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

birthday_button = ttk.Button(t, text ="Birthday/Anniversary Reminder", command = birthday_win).place(x=12,y=220)

def grocery_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Grocery Reminder")
    new.iconbitmap(r'ico.ico')

    global grocery_img
    grocery_img = ImageTk.PhotoImage(Image.open("grocery_schedule.png"))
    label = Label(new, image = grocery_img)
    label.pack()

    # Label - Title
    t_label = Label(new, text="Enter comma separated item names:",font=("poppins", 10))
    t_label.place(x=12, y=100)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=240, y=100)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=130)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="10", font=("poppins", 13))
    time1.place(x=100, y=130)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=200, y=135)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

groceries_list = ttk.Button(t, text ="Groceries Reminder", command = grocery_win).place(x=200,y=220)

def water_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Water Reminder")
    new.iconbitmap(r'ico.ico')

    global water_img
    water_img = ImageTk.PhotoImage(Image.open("water_schedule.png"))
    label = Label(new, image = water_img)
    label.pack()

    # Label - Title
    t_label = Label(new, text="Title to Notify:",font=("poppins", 10))
    t_label.place(x=12, y=100)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=100)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=130)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=130)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=135)

    var = IntVar()
    Radiobutton(new, text='Repeat every hour', variable=var, value=0).place(x=12,y=180)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

water_drinking_button = ttk.Button(t, text ="Water Drinking Reminder", command = water_win).place(x=320,y=220)

t.resizable(0,0)
t.mainloop()
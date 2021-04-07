from tkinter import *
from tkinter import messagebox
import Back_end



#creates a blank window
mw = Tk()

li = []

def var_states():

    LCheckVarO1 = CheckVarO1.get()
    LCheckVarO2 = CheckVarO2.get()
    LCheckVarO3 = CheckVarO3.get()

    LCheckVarT1 = CheckVarT1.get()
    LCheckVarT2 = CheckVarT2.get()
    LCheckVarT3 = CheckVarT3.get()

    LCheckVarH1 = CheckVarH1.get()
    LCheckVarH2 = CheckVarH2.get()

    LCheckVarW1 = CheckVarW1.get()
    LCheckVarW2 = CheckVarW2.get()
    li = [[LCheckVarO1, LCheckVarO2, LCheckVarO3], [LCheckVarT1,LCheckVarT2,LCheckVarT3], [LCheckVarH1,LCheckVarH2], [LCheckVarW1,LCheckVarW2]]


    for i in range(len(li)):
        ck=0
        for j in range(len(li[i])):
            if li[i][j]==1:
                ck=1
        if ck==0:
            messagebox.showinfo("Alert", "Please fil in all the fiealds")
            break

    if ck!=0:

        Back_end.li = li
        Back_end.main_calculation()


        if Back_end.Play[0] == 1:
            messagebox.showinfo("Good News", f"The match will occur today with a probability of {Back_end.Accuracy*100:.3f}% :)")

        elif Back_end.Play[0] == 0:
            messagebox.showinfo("Bad News", f"There is an {Back_end.Accuracy*100:.3f}% probability that it will not play today :(")






mw.title('Cricket match occurrence predictor')
#set the geometry attribute to change the root windows size
mw.geometry("700x650") #size of the app to be 700x650
mw.resizable(0, 0) #Don't allow resizing in the x or y direction
mw.configure(background='#afc8e0')

theLavel = Label(mw, bg='#afc8e0',font='Helvetica 20 bold', text="Cricket match occurrence predictor")
theLavel.pack()


theLineLavel = Label(mw, bg='#afc8e0',font='Helvetica 10 bold', text="-------------------------------------------------------------------------------------------------------------------")
theLineLavel.pack()

theOutlookLavel = Label(mw, bg='#afc8e0',font='Helvetica 18', text="Outlook")
theOutlookLavel.pack()

CheckVarO1 = IntVar()
CheckVarO2 = IntVar()
CheckVarO3 = IntVar()

CheckVarT1 = IntVar()
CheckVarT2 = IntVar()
CheckVarT3 = IntVar()

CheckVarH1 = IntVar()
CheckVarH2 = IntVar()


CheckVarW1 = IntVar()
CheckVarW2 = IntVar()

CO1 = Checkbutton(mw, text = "Rainy", variable = CheckVarO1,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CO2 = Checkbutton(mw, text = "Overcast", variable = CheckVarO2,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CO3 = Checkbutton(mw, text = "Sunny", variable = CheckVarO3,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CO1.pack()
CO2.pack()
CO3.pack()

theTemperatureLavel = Label(mw, bg='#afc8e0',font='Helvetica 18', text="Temperature")
theTemperatureLavel.pack()

CT1 = Checkbutton(mw, text = "Hot", variable = CheckVarT1,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CT2 = Checkbutton(mw, text = "Mild", variable = CheckVarT2,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CT3 = Checkbutton(mw, text = "Cool", variable = CheckVarT3,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)

CT1.pack()
CT2.pack()
CT3.pack()




theHumidityLavel = Label(mw, bg='#afc8e0',font='Helvetica 18', text="Humidity")
theHumidityLavel.pack()

CH1 = Checkbutton(mw, text = "High", variable = CheckVarH1,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CH2 = Checkbutton(mw, text = "Normal", variable = CheckVarH2,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)

CH1.pack()
CH2.pack()



theWindyLavel = Label(mw, bg='#afc8e0',font='Helvetica 18', text="Windy")
theWindyLavel.pack()

CW1 = Checkbutton(mw, text = "False", variable = CheckVarW1,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)
CW2 = Checkbutton(mw, text = "True", variable = CheckVarW2,
                 onvalue = 1, offvalue = 0, height=1,
                 width = 10)

CW1.pack()
CW2.pack()

btn = Button(mw, text='Submit', command=var_states)
btn.place(relx=0.5, x=24, y=460, anchor=NE)



mw.mainloop()
# execution of python program halts there.

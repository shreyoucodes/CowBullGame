from tkinter import *
import random
from tkinter.font import Font
colours=["Red", "Blue", "Yellow", "Green"]
root=Tk()
root.title("CowBullColourGame")
root.geometry("500x500")
root.config(bg="light green")
 
my_font = Font(
    family = 'Times',
    size = 16,
    weight = 'bold',
    slant = 'roman',
)


def End(Case, Tried):
    Done=Label(root, text="COMPLETED IN "+str(Tried)+" TRIES!", font=my_font)
    Done.place(x=75, y=50)
    if Case == "y":
        Main.config(text="WELL DONE!")
    else:   
        Main.config(text="GAME OVER!")
        Done.config(text="BETTER LUCK NEXT TIME!")
    def Fin():
        exit()
    Finished=Button(root, text="EXIT", height=5, width=13, command=Fin)
    Finished.place(x=75, y=100)

logo=PhotoImage(file="C:\Data\Psnl\coww.png")
logo2=PhotoImage(file="C:\Data\Psnl\corr.png")

def Compare(Try, Tried, Chosen, Answer):
    Main.config(text="RESULTS")
    L=Label(root, text="Your Guess: "+str(Chosen), bg="light green", font="ArielBold 12")
    L.place(x=50, y=50)
    if Chosen[0]==Answer[0]:
        p1="Cor"
        L1=Label(root, text="1st Colour: CORRECT!",image=logo2,bg="light blue",pady=5)
    elif Chosen[0] in Answer:
        p1="Alm"
        L1=Label(root, text="1st Colour: CORRECT Colour, WRONG Place",image= logo, bg="yellow",pady=5)
    else:
        p1="Wro"
        L1=Label(root, text="1st Colour: WRONG!", bg="red")
        
    if Chosen[1]== Answer[1]:
        p2="Cor"
        L2=Label(root, text="2nd Colour: CORRECT!",image=logo2, bg="light blue")
    elif Chosen[1] in Answer:
        p2="Alm"
        L2=Label(root, text="2nd Colour: CORRECT Colour, WRONG Place",image=logo, bg="yellow")
    else:
        p2="Wro"
        L2=Label(root, text="2nd Colour: WRONG!", bg="red",pady=5)
        
    if Chosen[2] == Answer[2]:
        p3="Cor"
        L3=Label(root, text="3rd Colour: CORRECT!",image=logo2, bg="light blue",pady=5)
    elif Chosen[2] in Answer:
        p3="Alm"
        L3=Label(root, text="3rd Colour: CORRECT Colour, WRONG Place", image=logo, bg="yellow",pady=5)
    else:
        p3="Wro"
        L3=Label(root, text="3rd Colour: WRONG!", bg="red",pady=5)
        
    if Chosen[3] == Answer[3]:
        p4 = "Cor"
        L4=Label(root, text="4th Colour: CORRECT!",image=logo2, bg="light blue",pady=5)
    elif Chosen[3] in Answer:
        p4="Alm"
        L4=Label(root, text="4th Colour: CORRECT Colour, WRONG Place", image=logo, bg="yellow",pady=5)
    else:
        p4="Wro"
        L4=Label(root, text="4th Colour: WRONG!", bg="red",pady=5)
    L1.place(x=50, y=100)
    L2.place(x=50, y=150)
    L3.place(x=50, y=200)
    L4.place(x=50, y=250)
    def ret():
        L.destroy()
        L1.destroy()
        L2.destroy()
        L3.destroy()
        L4.destroy()
        Cont.destroy()
        if p1 == "Cor" and p2 =="Cor" and p3 == "Cor" and p4=="Cor":
            End("y", Tried+1)
        else:
            Start(Try, Tried+1)
    Cont= Button(root, text="Continue", height=4, width=10, command=ret,pady=5)
    Cont.place(x=50, y=300)
    
def Start(Try, Tried):
    Easy.destroy()
    Medium.destroy()
    Hard.destroy()
    Main.config(text="You have "+str(Try-Tried)+" attempts left")
    global Chosen
    Chosen=[]
    def R():
        global Chosen
        Chosen.append("Red")
        if len(Chosen)==4:
            Green.place_forget()
            Red.place_forget()
            Yellow.place_forget()
            Blue.place_forget()
            Compare(Try, Tried, Chosen, Answer)
    def B():
        global Chosen
        Chosen.append("Blue")
        if len(Chosen)==4:
            Green.place_forget()
            Red.place_forget()
            Yellow.place_forget()
            Blue.place_forget()
            Compare(Try, Tried, Chosen, Answer)
    def Y():
        global Chosen
        Chosen.append("Yellow")
        if len(Chosen)==4:
            Green.place_forget()
            Red.place_forget()
            Yellow.place_forget()
            Blue.place_forget()
            Compare(Try, Tried, Chosen, Answer)
    def G():
        global Chosen
        Chosen.append("Green")
        if len(Chosen)==4:
            Green.place_forget()
            Red.place_forget()
            Yellow.place_forget()
            Blue.place_forget()
            Compare(Try, Tried, Chosen, Answer)
    Red=Button(root, text="RED", bg="red", height=5, width=13, command=R)
    Red.place(x=75, y=50)
    Blue = Button(root, text="BLUE", bg="light blue", height=5, width=13, command=B)
    Blue.place(x=275, y=50)
    Yellow = Button(root, text="YELLOW", bg="yellow", height=5, width=13, command=Y)
    Yellow.place(x=75, y=200)
    Green = Button(root, text="GREEN", bg="green", height=5, width=13, command=G)
    Green.place(x=275, y=200)
    if Try-Tried<=0:
        Red.destroy()
        Blue.destroy()
        Yellow.destroy()
        Green.destroy()
        End("n", Tried)

Main=Label(root, text="CHOOSE YOUR DIFFICULTY!", font=my_font, bg="light green")
Main.place(x=125, y=0)
Easy= Button(root, text="Easy", bg="green", height=5, width=13, command= lambda :Start(10, 0))
Easy.place(x=50, y=50)
Medium = Button(root, text="Medium", bg="yellow", height=5, width=13, command= lambda :Start(5, 0))
Medium.place(x=200, y=150)
Hard = Button(root, text="Hard", bg="red", height=5, width=13, command= lambda :Start(3, 0))
Hard.place(x=350, y=250)
Answer=[]
for i in range(5):
    Answer.append(random.choice(colours))
root.mainloop()
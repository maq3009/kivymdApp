import kivy
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image






class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        
        self.add_widget(Image(source="/Login_Boiler.png"))
        
        # Set columns
        self.cols = 2
        
        
        
        # Add widgets
        self.add_widget(Label(text = "Name: "))
        #Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text="Favorite Pizza"))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)
        
        self.add_widget(Label(text ="Favorite: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.submit = Button(text="Submit", font_size=32)
        self.add_widget(self.submit)
        
        # #Bind Button
        # self.submit.bind(on_press=self.press)
        # self.add_widget(self.submit)
        
        
       
        
        
        
        
        
        
        
class Myapp(App):
    def build(self):
        return MyGridLayout()


# # Windows Size
# windows = Tk()
# windows.title("Personal Registration Form")
# windows.geometry("540x640+200+10")
# windows.resizable(0, 0)

# frame = Frame(windows, width=610, heigh=640, bg="black", bd=8)
# frame.place(x=0, y=0)

# #labels and Entry fields
# heading = Label(frame, text="Personal Registration Form", fg="#97ffff", bg="black", font=("Calibre", 20, "bold"))
# heading.place(x=90, y=3)

# firstname = Label(frame, text="First Name:", fg="#97ffff", bg="black", font=("Calibre", 15, "bold"))
# firstname.place(x=10, y=70)

# firstnameEntry = Entry(frame, width=30, borderwidth=2)
# firstnameEntry.place(x=240, y=70)

# lastname = Label(frame, text="Last Name:", fg="#97ffff", bg="black", font=("Calibre", 15, "bold"))
# lastname.place(x=10, y=110)

# lastnameEntry = Entry(frame, width=30, borderwidth=2)
# lastnameEntry.place(x=240, y=110)

# email = Label(frame, text="Email:", fg="#97ffff", bg="black", font=("Calibre", 15, "bold"))
# email.place(x=10, y=150)

# emailEntry = Entry(frame, width=30, borderwidth=2)
# emailEntry.place(x=240, y=150)

if __name__=="__main__":
    Myapp().run()






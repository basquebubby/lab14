#########################################
#
#    70pt - Basic collision detection
#
#########################################

# When the player moves the ball into the rectangle, turn the rectangle red
# You will need to code the movement of the player and the collision detection.

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=0,column=0)
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global player
		global drawpad
                px1,py1,px2,py2 = drawpad.coords(player)
		global targetx1, targety1, targetx2, targety2
                drawpad.move(player,0,-10)
                if (px1 >= targetx1 and px2 <= targetx2) and (py1 >= targety1 and py2 <= targety2):
                    drawpad.itemconfig(target, fill='green')

		# Ensure that we are doing our collision detection
		# After we move our object!
	
	
		
myapp = MyApp(root)

root.mainloop()
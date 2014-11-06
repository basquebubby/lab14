#########################################
#
#         85pt - Boundary detection
#
#########################################

# Add a button to move to the right and make them work as you'd expect (repeating lab12)
# This time - make sure that pressing left or right does nothing if you are going
# to hit a "boundary" - i.e. the edge of the screen.

from Tkinter import *
root = Tk()
# Create our drawpad and oval - use variables for our width and height so
# we can access them later on
drawpadwidth = 480
drawpadheight = 320
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")
x1,y1,x2,y2 = drawpad.coords(oval)
class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "green")
		self.left.grid(row=1,column=0)
		self.left.bind("<Button-1>", self.leftClicked)
		self.right = Button(self.myContainer1)
       	        self.right.configure(text="Right", background= "green")
       	        self.right.grid(row=1,column=3)
       	        self.right.bind("<Button-1>", self.rightClicked)
		 
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def leftClicked(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
                # Add in boundary detection
		global oval
		global drawpad
		global drawpadwidth
		global drawpadheight
		x1, y1, x2, y2 = drawpad.coords(oval)
	        if x1 < 0:
	             drawpad.move(oval,(0+(-x1)),0)
	        drawpad.move(oval,-10,0)
	
	def rightClicked(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
                # Add in boundary detection
		global oval
		global drawpad
		global drawpadwidth
		global drawpadheight
		x1, y1, x2, y2 = drawpad.coords(oval)
	        if x2 > drawpadwidth: 
	             drawpad.move(oval,-(x2-drawpadwidth),0)
	        drawpad.move(oval,10,0)
	        
	# Add the button2Click method
		
myapp = MyApp(root)

root.mainloop()
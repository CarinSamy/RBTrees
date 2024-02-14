
from tkinter import *
from tkinter import messagebox



# Define Node
class Node():
    def __init__(self,val):
        self.val = val                                   # Value of Node
        self.parent = None                               # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node


# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red

        y = None
        x = self.root

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.val < x.val :
                x = x.left
            else:
                x = x.right

        node.parent = y                                  # Set parent of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < y.val :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None :                  # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Up


    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # Fix Up Insertion
    def fixInsert(self, k):
        while k.parent.color == 1:                        # While parent is red
            if k.parent == k.parent.parent.right:         # if parent is right child of its parent
                u = k.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # Set grandparent node as Red
                    k = k.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:                # If k is left child of it's parent
                        k = k.parent
                        self.RR(k)                        # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                         # if parent is left child of its parent
                u = k.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # set color of grandparent as Red
                    k = k.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:               # if k is right child of its parent
                        k = k.parent
                        self.LR(k)                        # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)              # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black


   
    
    def searchTree(self, key):
        root = self.root
        while root != self.NULL:
            if key.lower() > root.val.lower():
                root = root.right
            elif key.lower() < root.val.lower():
                root = root.left
            else:
                return True

        return False




    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )



    # Function to longest path
    def HeightCall(self, node):
        if node == None:
            return -1
        rightTree = self.HeightCall(node.right)
        leftTree = self.HeightCall(node.left)

        if leftTree > rightTree:
            return leftTree + 1
        else:
            return rightTree + 1


    # Function to call longest path
    def Height(self):
        return self.HeightCall(self.root)



    # Function to find size
    def sizeCall (self,node):
        if node.left==None and node.right==None:
            return 0
        else:
            return 1 + self.sizeCall(node.left) + self.sizeCall(node.right)




    # Function to call size
    def size(self):
        return self.sizeCall(self.root)


##########################################################################################
disable = 0
#Function to load dictionary
def load():
    global disable
    if disable == 0:
        f = open("/Users/mohammed/Desktop/EN-US-Dictionary.txt", "r")
        for x in f:
            if "\n" in x:
                x = x.replace("\n", "")

            bst.insertNode(x)
        f.close()
        z = bst.size()
        w = bst.Height()
        disable = 1
        messagebox.showinfo("showinfo", "Loading Complete :)\nDictionary Size = " + str(z) + "\nRBT height = " + str(w))
    else:
        z = bst.size()
        w = bst.Height()
        messagebox.showinfo("showinfo","Dictionary Already Loaded:)\nDictionary Size = " + str(z) + "\nRBT height = " + str(w))




def size():
    x= bst.size()
    messagebox.showinfo("showinfo", "Dictionary Size = " + str(x))

def insertword():

    def submit():
        k = entry.get()
        KEY = k.replace("\n", "")
        x = bst.searchTree(KEY)
        if x == True:
            messagebox.showerror("showerror", "ERROR:Word already in the dictionary!")
        else:
            bst.insertNode(KEY)
            z= bst.size()
            w= bst.Height()
            bst.print_tree()
            messagebox.showinfo("showinfo", "Word inserted :)\nDictionary Size = " + str(z)+"\nRBT height = "+str(w))



    x = bst.size()
    if x != 0 :
        window2 = Tk()
        window2.geometry("200x100")
        window2.title("Insert Word")
        entry = Entry(window2, font=("Arial", 10))
        entry.pack(side=LEFT)

        submitbutton = Button(window2, text="submit",
                              command=submit, font=("Matura MT Script Capitals", 20),
                              fg="#0000FF", bg="#000000",
                              activeforeground="#0000FF",
                              activebackground="#000000")
        submitbutton.pack(side=RIGHT)
        window2.mainloop()


    else:
        messagebox.showerror("showerror", "The dictionary is empty, load first")


def lookup():

    def submit2():
        k = entry.get()
        KEY = k.replace("\n", "")
        x = bst.searchTree(KEY)
        if x == True:
            messagebox.showinfo("showinfo", "YES")
        else:
            messagebox.showinfo("showinfo", "NO")



    y = bst.size()
    if y != 0 :
        window3 = Tk()
        window3.geometry("200x100")
        window3.title("Look_up Word")
        entry = Entry(window3, font=("Arial", 10))
        entry.pack(side=LEFT)

        submitbutton = Button(window3, text="submit",
                              command=submit2, font=("Matura MT Script Capitals", 20),
                              fg="#0000FF", bg="#000000",
                              activeforeground="#0000FF",
                              activebackground="#000000")
        submitbutton.pack(side=RIGHT)
        window3.mainloop()


    else:
        messagebox.showerror("showerror", "The dictionary is empty, load first")




#############################################################################################################
if __name__ == "__main__":

   bst = RBTree()
   window1=Tk()
   window1.geometry("420x290")
   window1.title("English Dictionary")
   loadbutton = Button(window1,text='Load Dictionary',
                   command=load,
                   font=("Matura MT Script Capitals",20),
                   fg="#0000FF",bg="#000000",
                   activeforeground="#0000FF",
                   activebackground="#000000",
                       padx=4, pady=4,height=2,width=13,relief=RAISED )

   printbutton = Button(window1,text='Print Dictionary Size',
                   command=size,
                   font=("Matura MT Script Capitals",20),
                   fg="#0000FF",bg="#000000",
                   activeforeground="#0000FF",
                   activebackground="#000000",
                       padx=4, pady=4,height=2,width=13,relief=RAISED )
   insertbutton = Button(window1, text='Insert Word',
                        command=insertword,
                        font=("Matura MT Script Capitals", 20),
                        fg="#0000FF", bg="#000000",
                        activeforeground="#0000FF",
                        activebackground="#000000",
                        padx=4, pady=4,height=2,width=13,relief=RAISED)
   lookupbutton = Button(window1, text='Look_up Word',
                         command=lookup,
                         font=("Matura MT Script Capitals", 20),
                         fg="#0000FF", bg="#000000",
                         activeforeground="#0000FF",
                         activebackground="#000000",
                         padx=4, pady=4,height=2,width=13,relief=RAISED)

   loadbutton.pack()
   printbutton.pack()
   insertbutton.pack()
   lookupbutton.pack()
   window1.mainloop()





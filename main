import os
from tkinter import*
from tkinter import filedialog as fd

class core:
    def __init__(mind):
        mind.gui = Tk()
        mind.gui.title("Unite Pad")
        mind.gui.resizable(False, False)

        #menubars
        mind.menusbar = Menu(mind.gui)

        #cascades
        #File
        mind.Files = Menu(mind.menusbar, tearoff=0)
        #mind.Files.add_command(label="Open",command=mind.open_file,)
        mind.Files.add_command(label="Open Folder", command=mind.open_folder)
        mind.Files.add_command(label="Save")
        mind.Files.add_command(label="Save As")
        mind.menusbar.add_cascade(label="Files", menu=mind.Files)
        
        #Tool
        mind.tools = Menu(mind.menusbar, tearoff=0)
        #Open CMD
        mind.tools.add_command(label="Open CMD/Terminal")
        mind.menusbar.add_cascade(label="Tools", menu=mind.tools)

        mind.gui.config(menu=mind.menusbar)

        
        #Info Bar
        mind.Info_bar = Frame(
            mind.gui,
            bg="black",
        )
        mind.Info_bar.pack(
            fill=BOTH
        )
        #Directory Entry
        mind.directory_entry = Entry(
            mind.Info_bar,   
            width=50,
        )
        mind.directory_entry.pack(
            pady=5,
            padx=5,
            side=LEFT,
        )
        #Filename Entry
        mind.Filename = Entry(
            mind.Info_bar,
        )
        mind.Filename.pack(
            pady=5,
            padx=5,
            side=LEFT,
        )
        #?
        mind.idkwhatisthisshit = Button(
            mind.Info_bar,
            bg="blue",
            text="?",
        )
        mind.idkwhatisthisshit.pack(
            pady=5,
            padx=5,
            side=LEFT,
        )

        #Filler
        mind.filler()

        #Action Bar
        mind.actionbar = Frame(
            mind.gui,
            bg="black",
        )
        mind.actionbar.pack(
            fill=BOTH,
        )
        #Languange Entry
        mind.language_entry = Entry(
            mind.actionbar,
        )
        mind.language_entry.pack(
            padx=5,
            pady=5,
            side=LEFT,
        )

        #Run Button
        mind.run_button = Button(
            mind.actionbar,
            bg="Yellow",
            text="Run",
            command=mind.test_run,
        )
        mind.run_button.pack(
            side=RIGHT,
            pady=5,
            padx=5,
        )
        #Virtual Explorer
        mind.virtualexplorer_toplayer = Frame(
            mind.gui,
            bg="grey"
        )
        mind.virtualexplorer_toplayer.pack(
            fill=BOTH,
            side=LEFT
        )
        #Actionbar Explorer
        mind.Explorer = Listbox(
            mind.virtualexplorer_toplayer,
            bg="grey",
            height=23,
        )
        #Text
        mind.pad = Text(
            mind.gui,
            )
        mind.pad.pack()

    #Functions

    #Open File Function
    def open_folder(mind):
        file = fd.askdirectory()
        #print(file)
        #Then Gets the Directory
        mind.directory_entry.delete(0,"end")
        mind.directory_entry.insert(0, file)
        mind.deploy_virtual_explorer()
    
    #Virtual File Explorer
    def deploy_virtual_explorer(mind):
        def getElement(event):
            selection = event.widget.curselection()
            index = selection[0]
            value = event.widget.get(index)
            dir  = mind.directory_entry.get()
            filepath = dir + "/"+value
            with open(filepath, 'r') as file:
                texts = file.read()
                mind.pad.delete('1.0', END)
                mind.pad.insert('1.0', texts)
                mind.Filename.delete(0,END)
                mind.Filename.insert(0,value)
        dir  = mind.directory_entry.get()
        #print(dir)
        flist = os.listdir(dir)
        #print(flist)
        mind.Explorer = Listbox(
            mind.virtualexplorer_toplayer,
        )
        mind.Explorer.bind('<Double-1>', getElement)
        mind.Explorer.pack()
        for item in flist:
            mind.Explorer.insert(END, item)
        mind.deploy_ext()
            
    def deploy_ext(mind):
        a = mind.directory_entry.get()
        b = mind.Filename.get()
        c= a + "/"  + b
        base = os.path.basename(c)
        os.path.splitext(base)
        e = os.path.splitext(base)[1]
        print("banana" + e)
        mind.language_entry.delete(0,END)
        mind.language_entry.insert(0, e)

    def test_run(mind):
        mind.deploy_ext()
        a = mind.directory_entry.get()
        #print(a)
        b = mind.Filename.get()
        #print(b)
        runner = "python3 " +b
        print(runner)
        #os.system(runner)

    def filler(mind):
        mind.filler_bar = Frame(
            mind.gui,
            bg="white",
        )
        mind.filler_bar.pack(
            fill=BOTH
        )
    
    def process(mind):
        mind.gui.mainloop()

if __name__=="__main__":
    machine=core()
    machine.process()

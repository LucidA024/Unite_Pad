from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import ttk
from pathlib import Path
from tkinter import messagebox



os.system("clear")
mess = '''UnitePad Linux Edition:'''
print(mess)
os.system("neofetch")
print("Dear User, Nothing to Worry! Every Click you made, it automatically saves your progress!")
print("\t~Lucid A024")
print("\n\nIt is designed to interact the app and the console!")

class Core:
	def __init__(main):
		main.gui = Tk()		
		main.Constructor()
		
	def Constructor(main):
		main.App_Configuration()
		main.App_Menu()
		main.Reference_Bar()
		main.VFM()
		main.Working_Sheets()
		#main.Menu_FileManager()
		
		#main.Testing()
	
	def App_Configuration(main):
		main.gui.geometry("1000x700")
		main.gui.title("UnitePad Studio (Beta)")
	
	#Reference Bar --> Displays the directory --> Displays the file name -->Displays what type of file
	def Reference_Bar(main):
		main.Reference_Bar = Frame(
			main.gui,
			bg="black"
			)
		main.Reference_Bar.pack(
			fill=X,
			)
		
		#This is the directory
		main.Directory_Label = Label(
			main.Reference_Bar,
			text="Global Directory: "
			)
		main.Directory_Label.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)
		#This is the status of the directory
		main.Directory_Status = Label(
			main.Reference_Bar,
			text=os.getcwd()
			)
		main.Directory_Status.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)
		
		main.Secondary = Frame(
			main.gui,
			bg = "black",
			)
		main.Secondary.pack(
			fill=X,
			)
		
		main.SL = Label(
			main.Secondary,
			text="File Dir: "
			)
		main.SL.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)
			
		main.SLL = Label(
			main.Secondary,
			text="Choose!"
			)
		main.SLL.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)

		main.SLLL = Label(
			main.Secondary,
			text="None!"
			)
		main.SLLL.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)			
		
		def clean():
			os.system("clear")	
		main.Save_Run_Button = Button(
			main.Reference_Bar,
			text = "Clear Console",
			command = clean,
			)

			
		main.Save_Run_Button.pack(
			side = RIGHT,
			padx = 3,
			pady = 3,
			)
	#Patched File Manager
	def VFM(main):
		main.VFM = Frame(
			main.gui,
			bg="red",
			width = 150,
			)
		main.VFM.pack(
			side=LEFT,
			fill=Y,
			)
		
		#Upper Layer!
		main.UpperLayer00 = Frame(
			main.VFM,
			)
		main.UpperLayer00.pack(
			fill=X,
			)
		main.File_Manager_Label = Label(
			main.UpperLayer00,
			text="File Manager",
			)
		main.File_Manager_Label.pack(
			pady=5,
			padx=5,
			)
		#Button Layer!
		main.ButtonLayer00 = Frame(
			main.VFM,
			)
		main.ButtonLayer00.pack(
			fill=X,
			)
		#Back Button
		main.BackButt = Button(
			main.ButtonLayer00,
			text = "<-- Back",
			bg="yellow",
			command = main.Get_New_Directory,
		)
		main.BackButt.pack(
			side = LEFT,
		)
		
		#New Layer
		main.ListLayer00 = Frame(
			main.VFM,
			)
		main.ListLayer00.pack(
			fill=X,
			)
		main.List_Items()
	def List_Items(main):
		#The listbox of directory
		main.FL = Listbox(
			main.ListLayer00,
			height = 900,
			)
		main.FL.pack()
		main.FL.bind('<Double-1>', lambda event: main.selected())
		#main.FL.forget()
		directory = os.getcwd()
		lists =os.listdir(directory)

		for x in range(len(lists)):
			#print(lists[x])
			main.FL.insert(x,lists[x])
			
	def back_dir(main):
		directory = os.getcwd()
		path = Path(directory)
		backed = path.parent.absolute()
		os.chdir(backed)
		#main.file_lists()
	def selected(main):
		def failsave():
			text = main.notepad.get(1.0,END)
			with open(main.SLLL["text"], 'w') as file:
				file.write(text)
		try:
			failsave() #-->Just incase misclicked!
		
		except:
			pass
		
		try:
			main.IDETab.destroy()
		except:
			pass

		for i in main.FL.curselection():
			ox = main.FL.get(i)
		
		if os.path.isfile(ox) == True :			
			#print("It is a file")
			#ming = ox
			#ming = False
			#print(ming)
			directory = os.getcwd()
			path = directory + "/" + ox
			
			main.SLL.forget()
			main.SLLL.forget()
			main.SLL = Label(
				main.Secondary,
				text=directory
				)
			main.SLL.pack(
				side = LEFT,
				padx = 3,
				pady = 3,
				)
			main.SLLL = Label(
				main.Secondary,
				text=ox
				)
			main.SLLL.pack(
				side = LEFT,
				padx = 3,
				pady = 3,
				)			
			filename, filext =os.path.splitext(path)
			if filext == ".py" or filext == ".java":
				main.IDETab = ttk.Frame(main.WorkingTab, height = 10000, width=1910)
				
				main.StatusFrame = Frame(
					main.IDETab,
					bg="black",
					)
				main.StatusFrame.pack(
					fill = X,
					)

				
				def run_it():
					#print(main.WorkingTab.select(tabId))
					jp = os.getcwd()
					path = jp + "/" + ox
					name, ext = os.path.splitext(path)
					
					if ext == ".py":
						#print("Python")		
						pythonname = main.SLLL["text"]
						pythondir = main.SLL["text"]
						os.chdir(pythondir)
						text = main.notepad.get(1.0,END)
						with open(pythonname, 'w') as file:
							file.write(text)
						#print(text)
						os.system("python3 " + pythonname)
						#print(path)
						#os.chdir.main.Directory_Status["text"]
						#main.file_lists()
						#main.Get_New_Directory()
						#reloads the file manager
						main.FL.forget()
						main.List_Items()
												
					elif ext == ".java":
						#print(main.DirectFile["text"])
						javaname = main.SLLL["text"]
						javadir = main.SLL["text"]
						os.chdir(javadir)
						text = main.notepad.get(1.0,END)
						with open(javaname, 'w') as file:
							file.write(text)
						#print(text)
						mainname, xxx = os.path.splitext(javaname)
						os.system("javac " + javaname)
						os.system("java " + mainname)
						
						#reloads the file manager
						main.FL.forget()
						main.List_Items()
						#main.Get_New_Directory()						
						#main.file_lists()						
						#print(path)						
						#os.chdir.main.Directory_Status["text"]
					
					else:
						print("others")
				
				
				#Rename File
				def renameF():
					#x = messagebox.askquestion("Form", "What do you want to rename to?")
					#print(x)
					print("----------")
					newName = input("You want to rename " + main.SLLL["text"] + " to?: ")
					#print(newName)
					os.rename(main.SLLL["text"], newName)
					
					#reloads the file manager
					main.FL.forget()
					main.List_Items()	
					failsave()
					
					try:
						main.IDETab.destroy()
					except:
						pass									
					
				main.RF_Button = Button(
					main.StatusFrame,
					text = "Rename",
					command = renameF,
					)
				main.RF_Button.pack(
					side = LEFT,
					padx = 3,
					pady = 3,
					)				
				#Save and Run
				main.SR_Button = Button(
					main.StatusFrame,
					text = "Save/Run",
					command = run_it,
					)
				main.SR_Button.pack(
					side = RIGHT,
					padx = 3,
					pady = 3,
					)
				
				#Exit and Save
				main.EButton = Button(
					main.StatusFrame,
					text = "Exit/Save",
					command = lambda: closeTab(),
					)
				main.EButton.pack(
					side = RIGHT,
					padx = 3,
					pady = 3
					)
					
				def closeTab():
					failsave()
					main.WorkingTab.forget(main.WorkingTab.select())
				
				main.notepad = Text(main.IDETab, height = 10000, width=1910)
				main.notepad.pack()
				main.WorkingTab.add(main.IDETab, text=ox)
				
				with open(path, 'r') as file:
					text = file.read()
					main.notepad.insert('1.0', text)
				
			else:
				pass

			

				
				
		
		elif os.path.isdir(ox) == True :
			directory = os.getcwd()
			path = directory + "/"+ox
			new_dir = os.chdir(path)	
			main.FL.forget()
			main.Directory_Status.forget()
			#This is the status of the directory
			main.Directory_Status = Label(
				main.Reference_Bar,
				text=os.getcwd()
				)
			main.Directory_Status.pack(
				side = LEFT,
				padx = 3,
				pady = 3,
				)			
			main.List_Items()
			#print(path)
			
	#Default Null WorkPlace
	def Working_Sheets(main):
		#Declare the notebook
		main.WorkingTab = ttk.Notebook(
			main.gui,
			)
		main.WorkingTab.pack(
			side=LEFT,
			)

	
	#Add Virtual File Manager --> Menu Bar Version
	def Menu_FileManager(main):
		#The default tab
		main.DefaultTab = ttk.Frame(main.WorkingTab, height = 900, width=1910)
		main.WorkingTab.add(main.DefaultTab, text="File Manager")

	
	#Functions
	def exit_app(main):
		exit()
	
	def check_dir(main):
		directory = os.getcwd()
		print(directory)

	def add_tab(main):
		x=0
		x = x+1
		main.DefaultTab = ttk.Frame(main.WorkingTab, height = 900, width=1910)
		main.texty = Text(main.DefaultTab).pack()
		main.WorkingTab.add(main.DefaultTab, text=x)
	
	def Get_New_Directory(main):
		directory = os.getcwd()
		path = Path(directory)
		backed = path.parent.absolute()
		new_dir = os.chdir(backed)	
		main.Directory_Status.forget()
		#This is the status of the directory
		main.Directory_Status = Label(
			main.Reference_Bar,
			text=os.getcwd()
			)
		main.Directory_Status.pack(
			side = LEFT,
			padx = 3,
			pady = 3,
			)		
		main.FL.forget()
		main.List_Items()

		#main.Menu_FileManager()
		
	def Get_New_Directory2(main):
		new_dir = fd.askdirectory()
		os.chdir(new_dir)
		main.Directory_Status.config(text=new_dir)
	
	def App_Menu(main):
		main.MenuBars = Menu(main.gui)
		
		#Files
		main.Files = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label="Files", menu = main.Files)
		
		#main.Files.add_command(label="Open Folder", command=main.Get_New_Directory2)
		main.Files.add_command(label="Save")
		main.Files.add_command(label="Exit", command = main.exit_app)
		
		#Tools
		main.Tools = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label="Tools", menu = main.Tools)
		
		main.Tools.add_command(label="Open CMD/Terminal")
		main.Tools.add_command(label="BODH -Converter")
		main.Tools.add_command(label="Color Picker")
		
		#Programs
		main.Programs = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label="Programs", menu = main.Programs)
		
		#Python
		main.Python = Menu(main.MenuBars, tearoff=0)
		main.Programs.add_cascade(label="Python", menu = main.Python)
		
		main.Python.add_command(label="New Python File")
		main.Python.add_command(label="New Tkinter File(GUI)")
		main.Python.add_command(label="Create Virtual Environment")
		#Add more Python in the future just in case!
				
		#Java
		main.Java = Menu(main.MenuBars, tearoff=0)
		main.Programs.add_cascade(label="Java", menu = main.Java)
		
		main.Java.add_command(label="New Java File")
		main.Java.add_command(label="Java GUI")#Implement all Action Commands and Mouse Listener
		#Add more Java in the future just in case!

		#Web
		main.Web = Menu(main.MenuBars, tearoff=0)
		main.Programs.add_cascade(label="Web", menu = main.Web)
		#HTML
		main.Web.add_command(label="New HTML File")
		#CSS
		main.Web.add_command(label="New CSS File")
		#JavaScript
		main.Web.add_command(label="New Javascript File")
		
		#Graphic
		main.Graphic = Menu(main.MenuBars, tearoff=0)
		main.Programs.add_cascade(label="Graphic", menu = main.Graphic)
		#Editing --> Photo Editing/Video Editing
		main.Editing = Menu(main.MenuBars, tearoff=0)
		main.Graphic.add_cascade(label="Editing", menu = main.Editing)
		main.Editing.add_command(label="Photo Editing")
		main.Editing.add_command(label="Video Editing")
		
		#Animating Beta
		main.Graphic.add_command(label="Painting Beta")
		main.Graphic.add_command(label="Animating Beta")
		main.Graphic.add_command(label="3D Beta")
		
		#Experimental Menu --> Must Delete Later!
		#main.Experimental = Menu(main.MenuBars, tearoff=0)
		#main.MenuBars.add_cascade(label="Experimental Menu", menu = main.Experimental)
		
		#main.Experimental.add_command(label="Check Directory", command = main.check_dir)
		#main.Experimental.add_command(label="Add Tab", command = main.add_tab)
		#main.Experimental.add_command(label="Print File", command = main.PrintFiles)
		
		
		main.gui.config(menu=main.MenuBars)
	
	def PrintFiles(main):
		directory = os.getcwd()
		lists =os.listdir(directory)
		
		for x in range(len(lists)):
			print(lists[x])
	
	def CoreRunner(main):
		main.gui.mainloop()
	
if __name__=="__main__":
	App = Core()
	App.CoreRunner()

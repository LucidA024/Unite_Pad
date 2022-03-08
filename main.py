from tkinter import *
from pathlib import Path
import os

class Core:
	def __init__(main):
		os.system("color 3")
		print("Please save your work before hiting the x or any close button!\n")
		print("Designed to Interact with the console :)\n")
		main.gui = Tk()
		main.Constructor()

	def Constructor(main):
		main.Configuration()
		main.Containers()
		main.MainMenu()

	def Configuration(main):
		main.gui.title("Toaster Pad")
		main.gui.geometry("1000x700")

	def Containers(main):
		#info container
		#File Manager Container
		#Notepad Container

		main.container00 = Frame(
			main.gui,
			bg = "red",
		)
		main.container00.pack(
			fill = X,
		)

		main.container01 = Frame(
			main.gui,
			bg = "blue",
		)
		main.container01.pack(
			fill = Y,
			side = LEFT,
		)

		main.container02 = Frame(
			main.gui,
			bg = "yellow"
		)
		main.container02.pack(
			fill = Y,
			side = LEFT,
		)
		main.ReferenceBar()
		main.FileManager()
		main.TextEd()

	def ReferenceBar(main):
		#layer 1
		main.Layer1 = Frame(
			main.container00,
			bg = "black"
		)
		main.Layer1.pack(
			fill = X,
		)

		main.label00 = Label(
			main.Layer1,
			text = "MCD: ",
			bg = "black",
			fg = "white",
		)
		main.label00.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)
		
		main.MCD = Label(
			main.Layer1,
			text = os.getcwd(),
			bg = "black",
			fg = "white",
		)
		main.MCD.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)
		main.Filler00 = Frame(
			main.container00,
			bg = "white",
		)
		main.Filler00.pack(
			fill = X,
		)

		#Layer 2
		main.Layer2 = Frame(
			main.container00,
			bg = "black",
		)
		main.Layer2.pack(
			fill = X,
		)
		
		main.Label01 = Label(
			main.Layer2,
			text = "OFD: ",
			bg = "black",
			fg = "white",
		)
		main.Label01.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)

		main.OFD = Label(
			main.Layer2,
			text = "No file openned yet!",
			bg = "black",
			fg = "white",
		)
		main.OFD.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)

		main.Filler01 = Frame(
			main.Layer2,
			bg = "white",
		)
		main.Filler01.pack(
			fill = Y,
			side = LEFT,
		)

		#filename
		main.Fname = Label(
			main.Layer2,
			text = "Noname",
			bg = "black",
			fg = "white",
		)
		main.Fname.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)

		main.Filler01 = Frame(
			main.Layer2,
			bg = "white",
		)
		main.Filler01.pack(
			fill = Y,
			side = LEFT,
		)

		#file type
		main.FType = Label(
			main.Layer2,
			text = "NoType",
			bg = "black",
			fg = "white",
		)
		main.FType.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)

		main.Filler03 = Frame(
			main.Layer2,
			bg = "white",
		)
		main.Filler03.pack(
			fill = Y,
			side = LEFT,
		)



	def FileManager(main):
		main.Filler00 = Frame(
			main.container00,
			bg = "white",
		)
		main.Filler00.pack(
			fill = X,
		)

		#container01
		#layer 1
		main.Layer01 = Frame(
			main.container01,
			bg = "black",
		)
		main.Layer01.pack(
			fill = X,
		)
		main.Filler00 = Frame(
			main.Layer01,
			bg = "white",
		)
		main.Filler00.pack(
			fill = Y,
			side = RIGHT,
		)

		#back
		main.back = Button(
			main.Layer01,
			text = "<<",
			command = main.BackFunction,
		)
		main.back.pack(
			padx = 3,
			pady = 3,
			side = LEFT,
		)
		main.update = Button(
			main.Layer01,
			text = "UD",
			command = main.RefreshState,
		)
		main.update.pack(
			padx = 0,
			pady = 3,
			side = LEFT,
		)

		#rename
		main.rename = Button(
			main.Layer01,
			text = "Rename",
			command = main.renameF,
		)
		main.rename.pack(
			padx = 3,
			pady = 3,
			side = RIGHT,
		)

		#delete
		main.delete = Button(
			main.Layer01,
			text = "Delete",
			command = main.deleteF,
		)
		main.delete.pack(
			padx = 3,
			pady = 3,
			side = RIGHT,
		)

		#layer 2
		main.FileList = Listbox(
			main.container01,
			height = 700,
			width = 30,
			bg = "#0d0d0d",
			fg = "white",
		)
		main.FileList.pack()
		directory = os.getcwd()
		lists = os.listdir(directory)
		
		for x in range(len(lists)):
			main.FileList.insert(x,lists[x])

		main.FileList.bind('<Double-1>', lambda event: main.safeSelect())

	def RefreshState(main):
		main.FileList.delete(0,END)
		odir = main.MCD.cget("text")
		lists = os.listdir(odir)
		
		for x in range(len(lists)):
			main.FileList.insert(x,lists[x])

	def safeSelect(main):
		try:
			main.selected()
		except:
			pass

	def selected(main):
		for i in main.FileList.curselection():
			main.Notepad.delete('1.0', 'end')
			lists = main.FileList.get(i)
			#print(lists)
		
		if os.path.isfile(lists) == True:
			main.OFD.config(text = os.getcwd())
			main.Fname.config(text = lists)
			filename, filetext = os.path.splitext(lists)
			main.Notepad.config(state='normal')
			if filetext == ".py":
				main.FType.config(text = "Python")
			elif filetext == ".cs":
				main.FType.config(text = "C#")
			elif filetext == ".c":
				main.FType.config(text = "C")
			elif filetext == ".cpp":
				main.FType.config(text = "C++")
			elif filetext == ".java":
				main.FType.config(text = "Java")
			elif filetext == ".js":
				main.FType.config(text = "Javascript")
			elif filetext == ".html":
				main.FType.config(text = "HTML")
			elif filetext == ".css":
				main.FType.config(text = "CSS")
			elif filetext == ".txt":
				main.FType.config(text = "Text")

			else:
				print("\nSorry unsopported file format! or maybe the developer is not familiar on that format yet and soon to be added on the future updates!")			
				main.Notepad.config(state=DISABLED)

			directory = os.getcwd()
			path = directory + "/" + lists
			with open (path, 'r') as file:
				text = file.read()
				main.Notepad.insert('1.0', text)

		elif os.path.isdir(lists) == True:
			directory = os.getcwd()
			path = directory + "/" + lists
			os.chdir(path)
			
			main.FileList.delete(0,END)
			dirz = os.getcwd()
			lists = os.listdir(dirz)
			
			for x in range(len(lists)):
				main.FileList.insert(x,lists[x])
			main.MCD.config(text = os.getcwd())


	def BackFunction(main):
		directory = os.getcwd()
		path = Path(directory)
		backed = path.parent.absolute()
		new_dir = os.chdir(backed)
		
		main.FileList.delete(0,END)

		directory = os.getcwd()
		lists = os.listdir(directory)
		
		for x in range(len(lists)):
			main.FileList.insert(x,lists[x])	
		
		main.MCD.config(text = os.getcwd())
	
	def TextEd(main):
		main.Notepad = Text(
			main.container02,
			width = 700,
			height = 500,
			undo = True,
			bg = "#1a1a1a",
			fg = "#00ff00",
			insertbackground="white",
		)
		main.Notepad.pack()

		main.gui.bind('<F5>', lambda event: main.saveEnRun())
		main.gui.bind('<Control-r>', lambda event: main.safeRun())
		main.gui.bind('<Control-s>', lambda event: main.safeSave())
	
	def saveEnRun(main):
		main.safeSave()
		main.safeRun()	
	
	def safeRun(main):
		try:
			main.running()
		except:
			pass

	def running(main):
		odir = main.MCD.cget("text")
		dir = main.OFD.cget("text")
		name = main.Fname.cget("text")
		type = main.FType.cget("text")
		if type == "Python":
			#print(name)
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			os.system("python " + name)
			os.chdir(odir)
			main.RefreshState()

		elif type == "Java":
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			os.system("javac " + name)
			jname, ef = os.path.splitext(name)
			os.system("java " + jname)
			os.chdir(odir)
			main.RefreshState()

		elif type == "HTML":
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			os.system(name)
			os.chdir(odir)
			main.RefreshState()

		elif type == "Javascript":
			os.system("color 3")
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			os.system("node " + name)
			os.chdir(odir)
			main.RefreshState()

		elif type == "C":		
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			jname, ef = os.path.splitext(name)
			os.system("gcc " + name + " -o " + jname + ".exe")
			os.system(jname + ".exe")
			os.chdir(odir)
			main.RefreshState()
		
		elif type == "C++":
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			jname, ef = os.path.splitext(name)
			os.system("g++ " + name + " -o " + jname + ".exe")
			os.system(jname + ".exe")
			os.chdir(odir)
			main.RefreshState()

		elif type == "C#":
			os.chdir(dir)
			print("\n\n" + os.getcwd() + "/" + name)
			jname, ef = os.path.splitext(name)
			os.system("csc " + name)
			os.system(jname)
			os.chdir(odir)
			main.RefreshState()

		else:
			pass
	def deleteF(main):
		for i in main.FileList.curselection():
			name = main.FileList.get(i)
			#print(name)	

		print("\nDo you really want to delete " + name + "?")
		feedback = input("y/n: ")	
		feedback.lower()
		if feedback == "y":
			#saving your desicion just in case you regret the first click!
			print("\nAre you 100% super duper sure about that? Because I cannot guarantee that it will be stored on recycle bin later!!")
			feedback02 = input("y/n: ")
			feedback02.lower()

			if feedback02 == "y":
				print("\tOkay! Deleting " + name + ".....")
				try:
					os.remove(name)
					print("\t[Done Deleting the File!]")
				except:
					os.rmdir(name)
					print("\t[Done Deleting the Folder!]")

			elif feedback02 == "n":
				print("\tOkay! You're Welcome!")
				main.RefreshState()
		
		elif feedback == "n":
			print("\nDid you just change your mind? Okay!")
			pass
			
		else:
			print("\nThe only option is Y or N, yes or no, please fix your input!")
			main.renameF()
			

	def renameF(main):
		for i in main.FileList.curselection():
			name = main.FileList.get(i)
			#print(name)

		print("\nYou want to rename " + name + " right?")
		feedback = input("y/n: ")
		feedback.lower()
		if feedback == "y":
			print("\nPlease don't forget to include the file name extension")
			newname = input("Okay! what do you want it to rename to?: ")
				
			print("\nRenaming " + name + " onto " + newname)
				
			os.rename(name, newname)
			main.RefreshState()
		
			print("\n[Finished Renaming!]")
		
		elif feedback == "n":
			print("\nDid you just change your mind? Okay!")
			pass
			
		else:
			print("\nThe only option is Y or N, yes or no, please fix your input!")
			main.renameF()	

	def safeSave(main):
		try:
			main.saved()
		except:
			pass

	def saved(main):
		odir = main.MCD.cget("text")
		dir = main.OFD.cget("text")
		os.chdir(dir)
		text = main.Notepad.get(1.0, END)
		nameX = main.Fname.cget("text")

		if nameX == "Noname":
			pass
		
		else:
			#print(nameX)
			with open(nameX, 'w') as file:
				file.write(text)
		os.chdir(odir)

	def exec(main):
		main.gui.mainloop()
		os.system("color 7")

	def CC(main):
		os.system("cls")	

	def MainMenu(main):
		main.MenuBars = Menu(main.gui)
		main.gui.config(menu = main.MenuBars)
		
		main.menuPlugs()

	def menuPlugs(main):
		main.FileMenu()
		main.ProgramMenu()
		main.ConsoleMenu()

	def ProgramMenu(main):
		main.Programs = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label = "Programs", menu = main.Programs)
	
		main.Programs.add_command(label = "New Folder", command = main.newFolder)
		main.Programs.add_command(label = "New Text", command = main.newText)
		main.Programs.add_command(label = "New Python", command = main.newPython)
		main.Programs.add_command(label = "New Java", command = main.newJava)
		main.Programs.add_command(label = "New C", command = main.newC)
		main.Programs.add_command(label = "New C++", command = main.newCPP)
		main.Programs.add_command(label = "New C#", command = main.newCS)
		main.Programs.add_command(label = "New HTML", command = main.newHTML)
		main.Programs.add_command(label = "New CSS", command = main.newCSS)
		main.Programs.add_command(label = "New Javascript", command = main.newJS)

	def newFolder(main):
		os.mkdir("New ToasterFolder")
		print("\nNew Folder Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newText(main):
		text = ""
		with open("newPyText.txt", "w") as file:
			file.write(text)
		print("\nNew Text File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newPython(main):
		text = ""
		with open("newPyToaster.py", "w") as file:
			file.write(text)
		print("\nNew Python File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newJava(main):
		text = ""
		with open("newJToaster.java", "w") as file:
			file.write(text)
		print("\nNew Java File Created! Make Sure to rename it before using it!")
		main.RefreshState()
	
	def newC(main):
		text = ""
		with open("newCToaster.c", "w") as file:
			file.write(text)
		print("\nNew C File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newCPP(main):
		text = ""
		with open("newCPPToaster.cpp", "w") as file:
			file.write(text)
		print("\nNew C++ File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newCS(main):
		text = ""
		with open("newCSToaster.cs", "w") as file:
			file.write(text)
		print("\nNew C# File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newHTML(main):
		text = ""
		with open("newHTMLToaster.html", "w") as file:
			file.write(text)
		print("\nNew HTML File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newCSS(main):
		text = ""
		with open("newCSSToaster.css", "w") as file:
			file.write(text)
		print("\nNew CSS File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def newJS(main):
		text = ""
		with open("newNodeToaster.js", "w") as file:
			file.write(text)
		print("\nNew Javascript File Created! Make Sure to rename it before using it!")
		main.RefreshState()

	def ConsoleMenu(main):
		main.Console = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label = "Console Commands", menu = main.Console)

		main.Console.add_command(label = "Clear Console", command = main.CC)

	def FileMenu(main):
		main.File = Menu(main.MenuBars, tearoff=0)
		main.MenuBars.add_cascade(label = "File", menu = main.File)

		main.File.add_command(label = "Save (Ctrl-s)", command = main.safeSave)	
		main.File.add_command(label = "Run (Ctrl-r)", command = main.safeRun)	
		main.File.add_command(label = "Save and Run (F5)", command = main.saveEnRun)	


if __name__ == "__main__":
	App = Core()
	App.exec()

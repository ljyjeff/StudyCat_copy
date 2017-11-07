from tkinter import *           # Importing the Tkinter (tool box) library

from PIL import ImageTk, Image

from Cat import Cat

from Monitor import monitor

from time import sleep

from threading import Thread

class CatDisplay:
    def __init__(self, master, cat):
        self.root = master
        self.cat = cat
        img = ImageTk.PhotoImage(self.cat.getImage().resize((250, 250), Image.ANTIALIAS))
        self.panel = Label(self.root, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")

        self.label = Label(self.root, text="Happiness: " + str(self.cat.getState()), fg=self.cat.getText())
        self.label.pack(side="bottom", fill="both", expand="yes")
        self.update()

    def update(self):
        img = ImageTk.PhotoImage(self.cat.getImage().resize((250, 250), Image.ANTIALIAS))
        text = "Happiness: " + str(self.cat.getState())

        self.panel.configure(image = img)
        self.panel.image = img

        self.label.configure(text = text, fg = self.cat.getText())
        self.label.text = text

        self.root.after(1000, self.update)



class DesktopApp:
    def __init__(self):
        self.root = Tk()
        self.cat = Cat()

        self.GUI = CatDisplay(self.root, self.cat)

        #self.root.overrideredirect(1)

        self.monitor = monitor.Monitor("./../Monitor/pList.txt")
        self.running = 1
        self.thread1 = Thread(target=self.monitorProcesses)
        self.thread1.start()

        self.updateAffection()

        self.root.mainloop()

    def monitorProcesses(self):
        while self.running:
            self.monitor.initVars()
            sleep(2)
            print(self.monitor.pollLatestProcess())

    def updateAffection(self):
        self.cat.setState(self.monitor.getAffection())
        self.root.after(5000, self.updateAffection)



if __name__ == '__main__':
    app = DesktopApp()

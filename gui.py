# -*- coding: utf-8 -*-

import tkinter as Tk
import tkinter.font as Font
from retroarchgui import RetroarchGUI
from customgui import CustomGUI
import platform
import wckToolTips

class GUI():

    MACOS_DEFAULT_FONT_SIZE = 7
    DEFAULT_FONT_SIZE = 9      

    def __init__(self,scriptDir,logger,title) :        
        self.scriptDir = scriptDir
        
        self.window = Tk.Tk()
        self.window.resizable(False,False)        
        self.startFontSize = self.DEFAULT_FONT_SIZE        
        
        if platform.system() == 'Windows' :
            self.window.iconbitmap('bestarcade.ico')
        elif platform.system() == 'Darwin' :
            # Handle tkinter font size bug on MacOS
            self.startFontSize = self.MACOS_DEFAULT_FONT_SIZE
            
        self.setFontSize(self.startFontSize)
        self.window.title(title)        
        self.logger = logger

    def draw(self) :
        self.root = Tk.Frame(self.window,padx=10,pady=5)
        self.root.grid(column=0,row=0)
        self.drawSliderFrame()
        self.drawMainframe()
        self.window.mainloop()
    
    def setFontSize(self, value) :        
        default_font = Font.nametofont("TkDefaultFont")
        default_font.configure(size=value)
        text_font = Font.nametofont("TkTextFont")
        text_font.configure(size=value)
        fixed_font = Font.nametofont("TkFixedFont")
        fixed_font.configure(size=value)
    
    def drawSliderFrame(self) :
        self.sliderFrame = Tk.Frame(self.root,padx=10,pady=0)
        self.sliderFrame.grid(column=0,row=0,sticky="EW",pady=0)
        self.sliderFrame.grid_columnconfigure(0, weight=1)
        self.slider = Tk.Scale(self.sliderFrame, from_=4, to=12, orient=Tk.HORIZONTAL, showvalue=0, command=self.setFontSize)
        wckToolTips.register(self.slider, 'Window Size') #TODO internationalization
        self.slider.grid(column=0,row=0,sticky="W",pady=0)
        self.slider.set(self.startFontSize)

# MAINFRAME, NOTEBOOK & TABS
    
    def drawMainframe(self) :
        self.mainFrame = Tk.Frame(self.root,padx=10,pady=0)
        self.mainFrame.grid(column=0,row=1,sticky="EW",pady=5)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.notebook = Tk.ttk.Notebook(self.mainFrame)
        self.notebook.grid(column=0,row=0,sticky="EW",pady=5)
        self.notebook.grid_columnconfigure(0, weight=1)
        
        # RETROARCH TAB
        self.retroarchFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.retroarchFrame.grid(column=0,row=0,sticky="EW",pady=5)
        self.retroarchFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.retroarchFrame, text='Retroarch',sticky="EW")
        self.notebook.select(self.retroarchFrame)
        retroarchGUI = RetroarchGUI(self.retroarchFrame,self.scriptDir,self.logger, self)
        retroarchGUI.draw()
        
        # CUSTOM TAB
        self.customFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.customFrame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.customFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.customFrame, text='Custom',sticky="EWNS")
        self.notebook.select(self.customFrame)
        customGUI = CustomGUI(self.customFrame,'custom',self.scriptDir,self.logger,self)
        customGUI.draw()
        
        # NEOGEOAES TAB
        self.neogeoaesFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.neogeoaesFrame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.neogeoaesFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.neogeoaesFrame, text='Neo Geo AES',sticky="EWNS")
        self.notebook.select(self.neogeoaesFrame)
        neogeoaesGUI = CustomGUI(self.neogeoaesFrame,'neogeoaes',self.scriptDir,self.logger,self)
        neogeoaesGUI.draw()
        
        # MODEL2 TAB
        self.model2Frame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.model2Frame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.model2Frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.model2Frame, text='Sega Model 2',sticky="EWNS")
        self.notebook.select(self.model2Frame)
        model2GUI = CustomGUI(self.model2Frame,'model2',self.scriptDir,self.logger,self)
        model2GUI.draw()
        
        # MODEL3 TAB
        self.model3Frame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.model3Frame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.model3Frame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.model3Frame, text='Sega Model 3',sticky="EWNS")
        self.notebook.select(self.model3Frame)
        model3GUI = CustomGUI(self.model3Frame,'model3',self.scriptDir,self.logger,self)
        model3GUI.draw()
        
        # ATOMISWAVE TAB
        self.atomiswaveFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.atomiswaveFrame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.atomiswaveFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.atomiswaveFrame, text='Atomiswave',sticky="EWNS")
        self.notebook.select(self.atomiswaveFrame)
        atomiswaveGUI = CustomGUI(self.atomiswaveFrame,'atomiswave',self.scriptDir,self.logger,self)
        atomiswaveGUI.draw()  
        
        # NAOMI TAB
        self.naomiFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.naomiFrame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.naomiFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.naomiFrame, text='Naomi',sticky="EWNS")
        self.notebook.select(self.naomiFrame)
        naomiGUI = CustomGUI(self.naomiFrame,'naomi',self.scriptDir,self.logger,self)
        naomiGUI.draw()
        
        # HANDHELD TAB
        self.handheldFrame = Tk.Frame(self.notebook,padx=10,pady=5)
        self.handheldFrame.grid(column=0,row=0,sticky="EWN",pady=5)
        self.handheldFrame.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.handheldFrame, text='Handhelds',sticky="EWNS")
        self.notebook.select(self.handheldFrame)
        handheldGUI = CustomGUI(self.handheldFrame,'handheld',self.scriptDir,self.logger,self)
        handheldGUI.draw()
                
        self.notebook.select(self.retroarchFrame)
        self.drawConsole()
        
    def disableOtherTabs(self, setKey) :
        if setKey == 'retroarch' :            
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'custom' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")            
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'neogeoaes' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")            
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'model2' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'model3' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'atomiswave' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")   
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")            
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'naomi' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.handheldFrame, state="disabled")
        elif setKey == 'handheld' :
            self.notebook.tab(self.retroarchFrame, state="disabled")
            self.notebook.tab(self.customFrame, state="disabled")
            self.notebook.tab(self.neogeoaesFrame, state="disabled")
            self.notebook.tab(self.model2Frame, state="disabled")
            self.notebook.tab(self.model3Frame, state="disabled")
            self.notebook.tab(self.atomiswaveFrame, state="disabled")
            self.notebook.tab(self.naomiFrame, state="disabled")
            
# CONSOLE STUFF

    def drawConsole(self) :
        self.consoleFrame = Tk.Frame(self.root, padx=10)
        self.consoleFrame.grid(column=0,row=5,sticky="EW",pady=5)
        self.consoleFrame.grid_columnconfigure(0, weight=1)
        self.logTest = Tk.Text(self.consoleFrame, height=15, state='disabled', wrap='word',background='black',foreground='yellow')
        self.logTest.grid(column=0,row=0,sticky="EW")
        self.scrollbar = Tk.Scrollbar(self.consoleFrame, orient=Tk.VERTICAL,command=self.logTest.yview)
        self.scrollbar.grid(column=1,row=0,sticky=(Tk.N,Tk.S))
        self.logTest['yscrollcommand'] = self.scrollbar.set
        self.logTest.after(10,self.updateConsoleFromQueue)
    
    def updateConsoleFromQueue(self):        
        while not self.logger.log_queue.empty():
            line = self.logger.log_queue.get()            
            self.writeToConsole(line)
            #TODO ?
            self.root.update_idletasks()
        self.logTest.after(10,self.updateConsoleFromQueue)
        
    def writeToConsole(self, msg):                
        numlines = self.logTest.index('end - 1 line').split('.')[0]
        self.logTest['state'] = 'normal'
        if numlines==24:
            self.logTest.delete(1.0, 2.0)
        if self.logTest.index('end-1c')!='1.0':
            self.logTest.insert('end', '\n')
        self.logTest.insert('end', msg)
        self.logTest.see(Tk.END)
        self.logTest['state'] = 'disabled'

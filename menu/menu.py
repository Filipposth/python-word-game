#needed for settings class
import yaml
import tkinter as tk
from tkinter import ttk, colorchooser
from functools import partial
###from playsound import playsound


#class for the menu GUI, separate from settings
class Menu():
    #add tkinter etc.
    def __init__(self, root):
        self.root = root
        self.f1=tk.Frame(self.root,width=1000)
        self.f1.pack(side='top')
        label1=tk.Label(self.f1,text="Python Word Game", font='Vivaldi 40',bg='#069486',width=1000)
        label1.pack(expand=1,fill='x')
        label2=tk.Label(self.f1,text='MENU', font='Stencil 40',bg="#069486",width=1000)
        label2.pack()
        self.f4=tk.Frame(self.root,width=500,bg='#069486')
        self.f4.pack(side='top',expand=1,fill='both')
        self.f2=tk.Frame(self.root,width=500,bg='#069486')
        self.f2.pack(side='top',expand=1,fill='both')
        #PLAY
        self.play_button=tk.Button(self.f2,text='PLAY',font='Arial 16',relief='groove',bg='#1d7b72',command=self.play_game)
        self.play_button.pack(side='top')
        #self.play_button.bind('<Enter>',self.color_config(self.play_button, "red",event)) 
        #self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        self.play_button.bind('<Enter>',partial(self.color_config, self.play_button, "red")) 
        self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        #https://docs.python.org/3/library/functools.html  
        #https://stackoverflow.com/questions/10239292/changing-text-color-when-hovering-over-text-with-tkinter
        #
        #LEADERBOARD
        self.leader_button=tk.Button(self.f2,text='LEADERBOARD',font='Arial 16',relief='groove',bg='#1d7b72',command=self.leaderboard)
        self.leader_button.pack(side='top')
        self.leader_button.bind('<Enter>',partial(self.color_config, self.leader_button, "red"))
        self.leader_button.bind("<Leave>", partial(self.color_config, self.leader_button, "black"))
        #QUIT
        self.quit_button=tk.Button(self.f2,text='EXIT',font='Arial 16',relief='groove',bg='#1d7b72',command=self.game_exit)
        self.quit_button.pack(side='top')
        self.quit_button.bind('<Enter>',partial(self.color_config, self.quit_button, "red")) #"#942706" complementary color
        self.quit_button.bind("<Leave>", partial(self.color_config, self.quit_button, "black"))
        self.f3=tk.Frame(self.root,height=100,bg='#069486')
        self.f3.pack(side='bottom',expand=1,fill='both')

    #start main game, WIP
    def play_game(self):
        self.options_window=tk.Toplevel(self.root,bg='#069486',height=400,width=400)
        #top.geometry("180x100")
        self.options_window.geometry('500x250+300+175')
        self.option1=tk.Button(self.options_window,text='HARD',bg='#1d7b72',relief='groove')### ADD command!!!!!!!!!
        self.option1.pack()
        self.option1.bind('<Enter>',partial(self.color_config,self.option1,'red'))
        self.option1.bind("<Leave>", partial(self.color_config, self.option1, "black"))
        self.option2=tk.Button(self.options_window,text='MEDIUM',bg='#1d7b72',relief='groove')### ADD command!!!!!!!!!
        self.option2.pack()
        self.option2.bind('<Enter>',partial(self.color_config,self.option2,'red'))
        self.option2.bind("<Leave>", partial(self.color_config, self.option2, "black"))
        self.option3=tk.Button(self.options_window,text='EASY',bg='#1d7b72',relief='groove')### ADD command!!!!!!!!!
        self.option3.pack()
        self.option3.bind('<Enter>',partial(self.color_config,self.option3,'red'))
        self.option3.bind("<Leave>", partial(self.color_config, self.option3, "black"))
        self.option4=tk.Button(self.options_window,text='EXIT',bg='#1d7b72',relief='groove',command=self.options_window.destroy)
        self.option4.pack()
        self.option4.bind('<Enter>',partial(self.color_config,self.option4,'red'))
        self.option4.bind("<Leave>", partial(self.color_config, self.option4, "black"))


        
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        
        widget.configure(foreground=color)


    #show leaderboards, WIP
    def leaderboard(self): pass


    #exit the game
    def game_exit(self): self.root.destroy()

    #go to settings GUI
    def settings(self): 
        settings = Settings()
        #find a way to simply change the layout instead of creating a new window

#class for settings GUI, separate from menu
#store settings in a .yaml file
class Settings():
    def __init__(self, root): 
        self.root = root
        with open("menu\\config.yaml", "r") as f: self.config = yaml.safe_load(f)
        self.sfx_multiplier = self.config["sfx_multiplier"]
        self.music_multiplier = self.config["music_multiplier"]
        self.bg_color = self.config["bg_color"]
        #add tkinter 

    #sound effects volume slider(?) 0-100
    def adjust_sfx(self, inp): 
        self.config["sfx_multiplier"] = self.sfx_multiplier = inp/100 #change 100 as necessary so input is in range
        #find sounds to add, find module for sound manipulation in python

    #music volume slider(?) 0-100
    def adjust_music(self, inp): 
        self.config["music_multiplier"] = self.music_multiplier = inp/100 
        #same as above

    #exit settings GUI, replace quit() with tkinter kill()
    def settings_exit(self): 
        #implement in tkinter with buttons
        x = input("Save changes?(Y/N):")
        if x == "Y": 
            with open("config.yaml", "w") as f: yaml.dump(self.config, f)
        quit()
        #self.root.kill() or equivalent

    #let the user choose a bg color using askcolor()
    def set_bg_color(self): 
        choice = colorchooser.askcolor(title = "Select a color")[1]
        self.config["bg_color"], self.bg_color = choice
        #set_bg_color(self.selected_color)

if __name__ == "__main__":
    root=tk.Tk()
    root.title('Python Word Game')
    root.geometry('1000x500+50+50')
    Menu(root)
    root.mainloop()

import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "admin_login.ui"


class AdminLogin:
    def __init__(self, master=None):
        # build ui
        self.Main_frame = tk.Frame(master)
        self.image_label_main = ttk.Label(self.Main_frame)
        self.img_image = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/image.png')
        self.image_label_main.configure(image=self.img_image, text='label2')
        self.image_label_main.place(anchor='nw', relx='0.02', rely='0.34', x='0', y='0')
        self.mm_label_main = tk.Label(self.Main_frame)
        self.mm_label_main.configure(background='#1a543e', compound='bottom', font='{ARVO} 14 {italic}', foreground='white')
        self.mm_label_main.configure(text='Message Management')
        self.mm_label_main.place(anchor='nw', relx='0.21', rely='0.4', x='0', y='0')
        self.separator_main = ttk.Separator(self.Main_frame)
        self.separator_main.configure(orient='horizontal')
        self.separator_main.pack(fill='y', ipady='200', pady='50', side='top')
        self.s_label_main = ttk.Label(self.Main_frame)
        self.s_label_main.configure(background='#1a543e', font='{ARVO} 14 {italic}', foreground='white', text='System')
        self.s_label_main.place(anchor='nw', relx='0.28', rely='0.45', x='0', y='0')
        self.welcome_label_main = ttk.Label(self.Main_frame)
        self.welcome_label_main.configure(background='#1a543e', font='{ARVO} 24 {italic}', foreground='White', text='Welcome')
        self.welcome_label_main.place(anchor='nw', relx='0.65', rely='0.15', x='0', y='0')
        self.username_entry_main = ttk.Entry(self.Main_frame)
        self.username_entry_main.configure(font='{ARVO} 12 {italic}')
        self.username_entry_main.place(anchor='nw', relx='0.69', rely='0.4', x='0', y='0')
        self.passwird_entry_main = ttk.Entry(self.Main_frame)
        self.passwird_entry_main.configure(font='{ARVO} 12 {italic}')
        self.passwird_entry_main.place(anchor='nw', relx='0.69', rely='0.55', x='0', y='0')
        self.username_label_main = ttk.Label(self.Main_frame)
        self.username_label_main.configure(background='#1a543e', font='{ARVO} 14 {italic}', foreground='white', text='Username :')
        self.username_label_main.place(anchor='nw', relx='0.51', rely='0.4', x='0', y='0')
        self.password_label_main = ttk.Label(self.Main_frame)
        self.password_label_main.configure(background='#1a543e', font='{AVRO} 14 {italic}', foreground='white', text='Password :')
        self.password_label_main.place(anchor='nw', relx='0.51', rely='0.55', x='0', y='0')
        self.label8 = ttk.Label(self.Main_frame)
        self.label8.configure(text='label8')
        self.label8.pack(side='top')
        self.login_button = tk.Button(self.Main_frame)
        self.login_button.configure(background='#ff8000', borderwidth='0', font='{AVRO} 12 {}', foreground='white')
        self.login_button.configure(highlightthickness='0', text='     Login      ')
        self.login_button.place(anchor='nw', relx='0.75', rely='0.7', x='0', y='0')
        self.login_button.configure(command=self.login)
        self.Main_frame.configure(background='#1a543e', height='500', width='800')
        self.Main_frame.pack(expand='true', fill='both', side='top')
        self.Main_frame.pack_propagate(0)

        # Main widget
        self.mainwindow = self.Main_frame
    
    def run(self):
        self.mainwindow.mainloop()

    def login(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Admin Login')
    root.resizable(height=False,width=False)
    app = AdminLogin(root)
    app.run()


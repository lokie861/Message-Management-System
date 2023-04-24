import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "dashboard.ui"


class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = tk.Frame(master)
        self.Main_frame = tk.Frame(self.frame1)
        self.Main_frame.configure(background='white', height='200', width='800')
        self.Main_frame.place(anchor='nw', x='0', y='0')
        self.button2 = tk.Button(self.frame1)
        self.img_mail_dashboard1 = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/mail_dashboard.png')
        self.button2.configure(borderwidth='0', highlightthickness='0', image=self.img_mail_dashboard1, text='Send Mail')
        self.button2.place(anchor='nw', relx='0.78', rely='0.2', x='0', y='0')
        self.button2.configure(command=self.open_sendmail_panel)
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(background='white', font='{Avro} 25 {bold italic}', text='DashBoard')
        self.label1.place(anchor='nw', relx='0.02', rely='0.03', x='0', y='0')
        self.delete_button_dash = tk.Button(self.frame1)
        self.img_delete_dash = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/delete_dash.png')
        self.delete_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_delete_dash, text='delete button')
        self.delete_button_dash.place(anchor='nw', relx='0.53', rely='0.2', x='0', y='0')
        self.delete_button_dash.configure(command=self.open_delete_panel)
        self.add_button_dash = tk.Button(self.frame1)
        self.img_add_dash = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/add_dash.png')
        self.add_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_add_dash, text='add details')
        self.add_button_dash.place(anchor='nw', relx='0.03', rely='0.2', x='0', y='0')
        self.add_button_dash.configure(command=self.open_add_panel)
        self.update_button_dash = tk.Button(self.frame1)
        self.img_update_dash = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/update_dash.png')
        self.update_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_update_dash, text='update button')
        self.update_button_dash.place(anchor='nw', relx='0.28', rely='0.2', x='0', y='0')
        self.update_button_dash.configure(command=self.open_update_panel)
        self.label2 = tk.Label(self.frame1)
        self.label2.configure(background='black', font='{avro} 14 {bold italic}', foreground='White', text='Add Details')
        self.label2.place(anchor='nw', relx='0.05', rely='0.55', x='0', y='0')
        self.label3 = tk.Label(self.frame1)
        self.label3.configure(background='black', font='{avro} 14 {bold italic}', foreground='White', text='Update Details')
        self.label3.place(anchor='nw', relx='0.28', rely='0.55', x='0', y='0')
        self.label5 = tk.Label(self.frame1)
        self.label5.configure(background='black', font='{avro} 14 {bold italic}', foreground='White', text='Delete Details')
        self.label5.place(anchor='nw', relx='0.53', rely='0.55', x='0', y='0')
        self.label6 = tk.Label(self.frame1)
        self.label6.configure(background='black', font='{avro} 14 {bold italic}', foreground='White', text='Send Mail')
        self.label6.place(anchor='nw', relx='0.82', rely='0.55', x='0', y='0')
        self.label7 = tk.Label(self.frame1)
        self.label7.configure(background='black', font='{avro} 12 {bold italic}', foreground='White', text='Message Management System')
        self.label7.place(anchor='nw', relx='0.64', rely='0.93', x='0', y='0')
        self.frame1.configure(background='black', borderwidth='0', height='500', highlightthickness='0')
        self.frame1.configure(width='800')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1
    
    def run(self):
        self.mainwindow.mainloop()

    def open_sendmail_panel(self):
        pass

    def open_delete_panel(self):
        pass

    def open_add_panel(self):
        pass

    def open_update_panel(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('DashBoard')
    root.resizable(height=False,width=False)
    app = DashboardApp(root)
    app.run()


import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "nexx.ui"


class Add_Details:
    def __init__(self, master=None):
        # build ui
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(self.frame1)
        self.label1 = tk.Label(self.frame2)
        self.img_last = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/last.png')
        self.label1.configure(image=self.img_last, text='label1')
        self.label1.place(anchor='nw', relx='0.21', rely='0.4', x='0', y='0')
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(background='#f04324', font='{Avero} 18 {bold italic}', text='ADD DETAILS ')
        self.label2.place(anchor='nw', relx='0.17', rely='0.1', x='0', y='0')
        self.frame2.configure(background='#f04324', height='500', width='275')
        self.frame2.place(anchor='nw', x='0', y='0')
        self.back_button_add = tk.Button(self.frame1)
        self.img_back = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/back.png')
        self.back_button_add.configure(activebackground='white', activeforeground='white', background='#f2dae5', borderwidth='0')
        self.back_button_add.configure(disabledforeground='white', foreground='white', highlightbackground='white', highlightcolor='white')
        self.back_button_add.configure(highlightthickness='0', image=self.img_back, text='button4')
        self.back_button_add.place(anchor='nw', relx='0.39', rely='0.02', y='0')
        self.back_button_add.configure(command=self.back)
        self.erp_label_add = tk.Label(self.frame1)
        self.erp_label_add.configure(background='#f2dae5', font='{revo} 12 {italic}', text='ERP  ')
        self.erp_label_add.place(anchor='nw', relx='0.4', rely='0.25', x='0', y='0')
        self.erp_entry_add = tk.Entry(self.frame1)
        self.erp_entry_add.configure(font='{aervo} 12 {italic}')
        self.erp_entry_add.place(anchor='nw', relx='0.55', rely='0.25', width='250', x='0', y='0')
        self.name_label_add = tk.Label(self.frame1)
        self.name_label_add.configure(background='#f2dae5', font='{revo} 12 {italic}', text='Name ')
        self.name_label_add.place(anchor='nw', relx='0.4', rely='0.35', x='0', y='0')
        self.mail_id_entry_add = tk.Entry(self.frame1)
        self.mail_id_entry_add.configure(font='{aervo} 12 {italic}')
        self.mail_id_entry_add.place(anchor='nw', relx='0.55', rely='0.75', width='250', x='0', y='0')
        self.name_entry_add = tk.Entry(self.frame1)
        self.name_entry_add.configure(font='{aervo} 12 {italic}')
        self.name_entry_add.place(anchor='nw', relx='0.55', rely='0.35', width='250', x='0', y='0')
        self.mail_id_add = tk.Label(self.frame1)
        self.mail_id_add.configure(background='#f2dae5', font='{revo} 12 {italic}', text='Mail ID ')
        self.mail_id_add.place(anchor='nw', relx='0.4', rely='0.45', x='0', y='0')
        self.label4 = ttk.Label(self.frame1)
        self.label4.configure(background='#f2dae5', font='{aevo} 12 {italic}', text='Father Name')
        self.label4.place(anchor='nw', relx='0.4', rely='0.75', x='0', y='0')
        self.mail_entry_add = tk.Entry(self.frame1)
        self.mail_entry_add.configure(font='{aervo} 12 {italic}')
        self.mail_entry_add.place(anchor='nw', relx='0.55', rely='0.45', width='250', x='0', y='0')
        self.add_button_add = tk.Button(self.frame1)
        self.img_add = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/add.png')
        self.add_button_add.configure(borderwidth='0', disabledforeground='#f2dae5', highlightthickness='0', image=self.img_add)
        self.add_button_add.place(anchor='nw', relx='0.75', rely='0.85', x='0', y='0')
        self.add_button_add.configure(command=self.add_details)
        self.year_label_add = tk.Label(self.frame1)
        self.year_label_add.configure(background='#f2dae5', font='{revo} 12 {italic}', text='Year')
        self.year_label_add.place(anchor='nw', relx='0.4', rely='0.55', x='0', y='0')
        self.depart_label_add = tk.Label(self.frame1)
        self.depart_label_add.configure(background='#f2dae5', font='{revo} 12 {italic}', text='Department')
        self.depart_label_add.place(anchor='nw', relx='0.4', rely='0.65', x='0', y='0')
        self.year_entry_add = tk.Entry(self.frame1)
        self.year_entry_add.configure(font='{aervo} 12 {italic}')
        self.year_entry_add.place(anchor='nw', relx='0.55', rely='0.55', width='250', x='0', y='0')
        self.depart_entry_add = tk.Entry(self.frame1)
        self.depart_entry_add.configure(font='{aervo} 12 {italic}')
        self.depart_entry_add.place(anchor='nw', relx='0.55', rely='0.65', width='250', x='0', y='0')
        self.frame1.configure(background='#f2dae5', height='500', width='800')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1
    
    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        pass

    def add_details(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Add Details')
    root.resizable(height=False,width=False)
    app = Add_Details(root)
    app.run()


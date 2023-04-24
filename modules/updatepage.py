import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "update_page.ui"


class UpdatePage:
    def __init__(self, master=None):
        # build ui
        self.Main_Frame = tk.Frame(master)
        self.blue_frame = tk.Frame(self.Main_Frame)
        self.Update_image = tk.Label(self.blue_frame)
        self.img_update = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/update.png')
        self.Update_image.configure(image=self.img_update, text='label5')
        self.Update_image.place(anchor='nw', relx='0.16', rely='0.3', x='0', y='0')
        self.blue_frame.configure(background='#249ae3', height='500', width='275')
        self.blue_frame.place(anchor='nw', x='0', y='0')
        self.Edit_label = tk.Label(self.Main_Frame)
        self.Edit_label.configure(background='#249ae3', font='{avero} 16 {bold}', text='Edit Details')
        self.Edit_label.place(anchor='nw', relx='0.07', rely='0.05', x='0', y='0')
        self.erp_entry_update = tk.Entry(self.Main_Frame)
        self.erp_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.erp_entry_update.place(anchor='nw', relx='0.55', rely='0.2', x='0', y='0')
        self.erp_label_update = tk.Label(self.Main_Frame)
        self.erp_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='ERP')
        self.erp_label_update.place(anchor='nw', relx='0.38', rely='0.2', x='0', y='0')
        self.name_label_update = tk.Label(self.Main_Frame)
        self.name_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Name')
        self.name_label_update.place(anchor='nw', relx='0.38', rely='0.3', x='0', y='0')
        self.mail_id_entry_update = tk.Entry(self.Main_Frame)
        self.mail_id_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.mail_id_entry_update.place(anchor='nw', relx='0.55', rely='0.4', x='0', y='0')
        self.mail_id_label_update = tk.Label(self.Main_Frame)
        self.mail_id_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Mail ID')
        self.mail_id_label_update.place(anchor='nw', relx='0.38', rely='0.4', x='0', y='0')
        self.name_entry_update = tk.Entry(self.Main_Frame)
        self.name_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.name_entry_update.place(anchor='nw', relx='0.55', rely='0.3', x='0', y='0')
        self.year_label_update = tk.Label(self.Main_Frame)
        self.year_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Year')
        self.year_label_update.place(anchor='nw', relx='0.38', rely='0.5', x='0', y='0')
        self.year_entry_update = tk.Entry(self.Main_Frame)
        self.year_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.year_entry_update.place(anchor='nw', relx='0.55', rely='0.5', x='0', y='0')
        self.depart_label_update = tk.Label(self.Main_Frame)
        self.depart_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Department')
        self.depart_label_update.place(anchor='nw', relx='0.38', rely='0.6', x='0', y='0')
        self.father_name_label_update = tk.Label(self.Main_Frame)
        self.father_name_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Father Name')
        self.father_name_label_update.place(anchor='nw', relx='0.38', rely='0.7', x='0', y='0')
        self.depart_entry_update = tk.Entry(self.Main_Frame)
        self.depart_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.depart_entry_update.place(anchor='nw', relx='0.55', rely='0.6', x='0', y='0')
        self.father_name_entry_update = tk.Entry(self.Main_Frame)
        self.father_name_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.father_name_entry_update.place(anchor='nw', relx='0.55', rely='0.7', x='0', y='0')
        self.back_button_update = tk.Button(self.Main_Frame)
        self.img_back_update = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/back_update.png')
        self.back_button_update.configure(background='#edf5fa', borderwidth='0', highlightthickness='0', image=self.img_back_update)
        self.back_button_update.configure(text='button1')
        self.back_button_update.place(anchor='nw', relx='0.37', rely='0.029', x='0', y='0')
        self.back_button_update.configure(command=self.back)
        self.update_button_update = tk.Button(self.Main_Frame)
        self.img_Update_update = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/Update_update.png')
        self.update_button_update.configure(background='#edf5fa', borderwidth='0', highlightthickness='0', image=self.img_Update_update)
        self.update_button_update.configure(text='button2')
        self.update_button_update.place(anchor='nw', relx='0.8', rely='0.84', x='0', y='0')
        self.update_button_update.configure(command=self.update)
        self.button1 = tk.Button(self.Main_Frame)
        self.img_ok_update = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/ok_update.png')
        self.button1.configure(background='#edf5fa', borderwidth='0', highlightthickness='0', image=self.img_ok_update)
        self.button1.configure(text='button1')
        self.button1.place(anchor='nw', relx='0.85', rely='0.17', x='0', y='0')
        self.button1.configure(command=self.ok)
        self.label1 = ttk.Label(self.Main_Frame)
        self.label1.configure(background='#edf5fa', text='Note: The Date format should be YYYY/MM/DD')
        self.label1.place(anchor='nw', relx='0.38', rely='0.9', x='0', y='0')
        self.Main_Frame.configure(background='#edf5fa', height='500', width='800')
        self.Main_Frame.pack(side='top')

        # Main widget
        self.mainwindow = self.Main_Frame
    
    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        pass

    def update(self):
        pass

    def ok(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Update Details')
    root.resizable(height=False,width=False)
    app = UpdatePage(root)
    app.run()


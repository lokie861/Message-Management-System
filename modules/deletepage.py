import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "delete_page.ui"


class DeletePage:
    def __init__(self, master=None):
        # build ui
        self.Main_frame = tk.Frame(master)
        self.grey_frame = tk.Frame(self.Main_frame)
        self.image_label_delete = tk.Label(self.grey_frame)
        self.img_deletee = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/deletee.png')
        self.image_label_delete.configure(image=self.img_deletee, text='label1')
        self.image_label_delete.place(anchor='nw', relx='0.17', rely='0.3', x='0', y='0')
        self.label2 = tk.Label(self.grey_frame)
        self.label2.configure(background='grey', font='{avro} 14 {bold italic}', foreground='white', text='Delete Details')
        self.label2.place(anchor='nw', relx='0.2', rely='0.1', x='0', y='0')
        self.grey_frame.configure(background='grey', height='500', width='275')
        self.grey_frame.place(anchor='nw', x='0', y='0')
        self.erp_label_delete = tk.Label(self.Main_frame)
        self.erp_label_delete.configure(background='white', font='{avro} 14 {italic}', foreground='black', text='ERP  ')
        self.erp_label_delete.place(anchor='nw', relx='0.4', rely='0.35', x='0', y='0')
        self.erp_entry_delete = tk.Entry(self.Main_frame)
        self.erp_entry_delete.configure(font='{avro} 14 {italic}')
        self.erp_entry_delete.place(anchor='nw', relx='0.5', rely='0.35', x='0', y='0')
        self.note_label_delete = tk.Label(self.Main_frame)
        self.note_label_delete.configure(background='white', font='{timesnew} 10 {}', text="Note: Once deleted can't be recovered")
        self.note_label_delete.place(anchor='nw', relx='0.35', rely='0.9', x='0', y='0')
        self.delete_button_delete = tk.Button(self.Main_frame)
        self.img_delete_button = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/delete_button.png')
        self.delete_button_delete.configure(background='white', borderwidth='0', highlightthickness='0', image=self.img_delete_button)
        self.delete_button_delete.configure(text='button1')
        self.delete_button_delete.place(anchor='nw', relx='0.8', rely='0.55', x='0', y='0')
        self.delete_button_delete.configure(command=self.detele_details)
        self.back_button_delete = tk.Button(self.Main_frame)
        self.img_back_delete = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/back_delete.png')
        self.back_button_delete.configure(background='white', borderwidth='0', highlightthickness='0', image=self.img_back_delete)
        self.back_button_delete.configure(text='button2')
        self.back_button_delete.place(anchor='nw', relx='0.37', rely='0.04', x='0', y='0')
        self.back_button_delete.configure(command=self.back)
        self.Main_frame.configure(background='white', height='500', width='800')
        self.Main_frame.pack(side='top')

        # Main widget
        self.mainwindow = self.Main_frame
    
    def run(self):
        self.mainwindow.mainloop()

    def detele_details(self):
        pass

    def back(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Delete Details ')
    root.resizable(height=False,width=False)
    app = DeletePage(root)
    app.run()


import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "send_mail.ui"


class SendMail:
    def __init__(self, master=None):
        # build ui
        self.main_frame = tk.Frame(master)
        self.blue_frame = tk.Frame(self.main_frame)
        self.mai_image_send = tk.Label(self.blue_frame)
        self.img_mail_send = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/mail_send.png')
        self.mai_image_send.configure(image=self.img_mail_send, text='label1')
        self.mai_image_send.place(anchor='nw', relx='0.08', rely='0.35', x='0', y='0')
        self.sm_label_send = ttk.Label(self.blue_frame)
        self.sm_label_send.configure(background='#10e396', font='{avro} 14 {bold italic}', text='Send Mail')
        self.sm_label_send.place(anchor='nw', relx='0.25', rely='0.15', x='0', y='0')
        self.blue_frame.configure(background='#10e396', height='500', width='300')
        self.blue_frame.place(anchor='nw', x='0', y='0')
        self.mail_sub_label_send = ttk.Label(self.main_frame)
        self.mail_sub_label_send.configure(background='#cafae6', font='{avro} 12 {italic}', text='Mail Subject')
        self.mail_sub_label_send.place(anchor='nw', relx='0.4', rely='0.15', x='0', y='0')
        self.subject_entry_send = ttk.Entry(self.main_frame)
        self.subject_entry_send.configure(font='{avro} 12 {italic}')
        self.subject_entry_send.place(anchor='nw', relx='0.6', rely='0.15', x='0', y='0')
        self.body_label_send = tk.Label(self.main_frame)
        self.body_label_send.configure(background='#cafae6', font='{avro} 12 {italic}', text='Mail Body')
        self.body_label_send.place(anchor='nw', relx='0.4', rely='0.25', x='0', y='0')
        self.body_text_send = tk.Text(self.main_frame)
        self.body_text_send.configure(height='10', width='50')
        self.body_text_send.place(anchor='nw', relx='0.4', rely='0.3', width='365', x='0', y='0')
        self.list_erp_label_send = tk.Label(self.main_frame)
        self.list_erp_label_send.configure(background='#cafae6', font='{avro} 12 {italic}', text='List of ERP')
        self.list_erp_label_send.place(anchor='nw', relx='0.4', rely='0.65', x='0', y='0')
        self.seperate_label_send = tk.Label(self.main_frame)
        self.seperate_label_send.configure(background='#cafae6', text='(separated by , )')
        self.seperate_label_send.place(anchor='nw', relx='0.51', rely='0.65', x='0', y='0')
        self.erp_text_send = tk.Text(self.main_frame)
        self.erp_text_send.configure(height='10', width='50')
        self.erp_text_send.place(anchor='nw', height='75', relx='0.4', rely='0.7', width='365', x='0', y='0')
        self.all_checkbutton_send = tk.Checkbutton(self.main_frame)
        self.all_checkbutton_send.configure(background='#cafae6', font='{avro} 12 {}', text='  All')
        self.all_checkbutton_send.place(anchor='nw', relx='0.4', rely='0.85', x='0', y='0')
        self.all_checkbutton_send.configure(command=self.all_mail)
        self.cm_label_send = tk.Label(self.main_frame)
        self.cm_label_send.configure(background='#cafae6', font='{avro} 14 {bold italic}', text='Compose Mail')
        self.cm_label_send.place(anchor='nw', relx='0.4', rely='0.04', x='0', y='0')
        self.send_send = tk.Button(self.main_frame)
        self.img_send = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/send.png')
        self.send_send.configure(activebackground='#cafae6', background='#cafae6', borderwidth='0', highlightthickness='0')
        self.send_send.configure(image=self.img_send, text='button3')
        self.send_send.place(anchor='nw', relx='0.86', rely='0.9', x='0', y='0')
        self.send_send.configure(command=self.send_mail)
        self.main_frame.configure(background='#cafae6', borderwidth='0', height='500', highlightbackground='#cafae6')
        self.main_frame.configure(highlightcolor='#cafae6', highlightthickness='0', width='800')
        self.main_frame.pack(expand='false', side='top')
        self.main_frame.pack_propagate(0)

        # Main widget
        self.mainwindow = self.main_frame
    
    def run(self):
        self.mainwindow.mainloop()

    def all_mail(self):
        pass

    def send_mail(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Send Mail')
    root.resizable(height=False,width=False)
    app = SendMail(root)
    app.run()


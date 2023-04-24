import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
def call_dashboard():
    root1 = tk.Tk()
    root1.resizable(height=False,width=False)
    dash = DashboardApp(root1)
    dash.run()

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
        self.back_button_add.configure(activebackground='white', activeforeground='white', background='#f2dae5',
                                       borderwidth='0')
        self.back_button_add.configure(disabledforeground='white', foreground='white', highlightbackground='white',
                                       highlightcolor='white')
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
        self.add_button_add.configure(borderwidth='0', disabledforeground='#f2dae5', highlightthickness='0',
                                      image=self.img_add)
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
        self.img_back_update = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/back_update.png')
        self.back_button_update.configure(background='#edf5fa', borderwidth='0', highlightthickness='0',
                                          image=self.img_back_update)
        self.back_button_update.configure(text='button1')
        self.back_button_update.place(anchor='nw', relx='0.37', rely='0.029', x='0', y='0')
        self.back_button_update.configure(command=self.back)
        self.update_button_update = tk.Button(self.Main_Frame)
        self.img_Update_update = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/Update_update.png')
        self.update_button_update.configure(background='#edf5fa', borderwidth='0', highlightthickness='0',
                                            image=self.img_Update_update)
        self.update_button_update.configure(text='button2')
        self.update_button_update.place(anchor='nw', relx='0.8', rely='0.84', x='0', y='0')
        self.update_button_update.configure(command=self.update)
        self.button1 = tk.Button(self.Main_Frame)
        self.img_ok_update = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/ok_update.png')
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
        self.label2.configure(background='grey', font='{avro} 14 {bold italic}', foreground='white',
                              text='Delete Details')
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
        self.note_label_delete.configure(background='white', font='{timesnew} 10 {}',
                                         text="Note: Once deleted can't be recovered")
        self.note_label_delete.place(anchor='nw', relx='0.35', rely='0.9', x='0', y='0')
        self.delete_button_delete = tk.Button(self.Main_frame)
        self.img_delete_button = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/delete_button.png')
        self.delete_button_delete.configure(background='white', borderwidth='0', highlightthickness='0',
                                            image=self.img_delete_button)
        self.delete_button_delete.configure(text='button1')
        self.delete_button_delete.place(anchor='nw', relx='0.8', rely='0.55', x='0', y='0')
        self.delete_button_delete.configure(command=self.detele_details)
        self.back_button_delete = tk.Button(self.Main_frame)
        self.img_back_delete = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/back_delete.png')
        self.back_button_delete.configure(background='white', borderwidth='0', highlightthickness='0',
                                          image=self.img_back_delete)
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


class SendMail:
    def __init__(self, master=None):
        # build ui
        self.main_frame = tk.Frame(master)
        self.blue_frame = tk.Frame(self.main_frame)
        self.mai_image_send = tk.Label(self.blue_frame)
        self.img_mail_send = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/mail_send.png')
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
        self.send_send.configure(activebackground='#cafae6', background='#cafae6', borderwidth='0',
                                 highlightthickness='0')
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


class DashboardApp:
    def __init__(self, master=None):
        # build ui
        self.master = master
        self.frame1 = tk.Frame(master)
        self.Main_frame = tk.Frame(self.frame1)
        self.Main_frame.configure(background='white', height='200', width='800')
        self.Main_frame.place(anchor='nw', x='0', y='0')
        self.button2 = tk.Button(self.frame1)
        self.img_mail_dashboard1 = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/mail_dashboard.png')
        self.button2.configure(borderwidth='0', highlightthickness='0', image=self.img_mail_dashboard1,
                               text='Send_Mail')
        self.button2.place(anchor='nw', relx='0.78', rely='0.2', x='0', y='0')
        self.button2.configure(command=self.open_sendmail_panel)
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(background='white', font='{Avro} 25 {bold italic}', text='DashBoard')
        self.label1.place(anchor='nw', relx='0.02', rely='0.03', x='0', y='0')
        self.delete_button_dash = tk.Button(self.frame1)
        self.img_delete_dash = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/delete_dash.png')
        self.delete_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_delete_dash,
                                          text='delete button')
        self.delete_button_dash.place(anchor='nw', relx='0.53', rely='0.2', x='0', y='0')
        self.delete_button_dash.configure(command=self.open_delete_panel)
        self.add_button_dash = tk.Button(self.frame1)
        self.img_add_dash = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/add_dash.png')
        self.add_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_add_dash,
                                       text='add details')
        self.add_button_dash.place(anchor='nw', relx='0.03', rely='0.2', x='0', y='0')
        self.add_button_dash.configure(command=self.open_add_panel)
        self.update_button_dash = tk.Button(self.frame1)
        self.img_update_dash = tk.PhotoImage(
            file='/home/garuda/Desktop/project/message_manage/assets/images/update_dash.png')
        self.update_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_update_dash,
                                          text='update button')
        self.update_button_dash.place(anchor='nw', relx='0.28', rely='0.2', x='0', y='0')
        self.update_button_dash.configure(command=self.open_update_panel)
        self.label2 = tk.Label(self.frame1)
        self.label2.configure(background='black', font='{avro} 14 {bold italic}', foreground='White',
                              text='Add Details')
        self.label2.place(anchor='nw', relx='0.05', rely='0.55', x='0', y='0')
        self.label3 = tk.Label(self.frame1)
        self.label3.configure(background='black', font='{avro} 14 {bold italic}', foreground='White',
                              text='Update Details')
        self.label3.place(anchor='nw', relx='0.28', rely='0.55', x='0', y='0')
        self.label5 = tk.Label(self.frame1)
        self.label5.configure(background='black', font='{avro} 14 {bold italic}', foreground='White',
                              text='Delete Details')
        self.label5.place(anchor='nw', relx='0.53', rely='0.55', x='0', y='0')
        self.label6 = tk.Label(self.frame1)
        self.label6.configure(background='black', font='{avro} 14 {bold italic}', foreground='White', text='Send Mail')
        self.label6.place(anchor='nw', relx='0.82', rely='0.55', x='0', y='0')
        self.label7 = tk.Label(self.frame1)
        self.label7.configure(background='black', font='{avro} 12 {bold italic}', foreground='White',
                              text='Message Management System')
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


class AdminLogin:
    def __init__(self, master):
        # build ui
        self.master = master
        self.Main_frame = tk.Frame(master)
        self.image_label_main = ttk.Label(self.Main_frame)
        self.img_image = tk.PhotoImage(file='/home/garuda/Desktop/project/message_manage/assets/images/image.png')
        self.image_label_main.configure(image=self.img_image, text='label2')
        self.image_label_main.place(anchor='nw', relx='0.02', rely='0.34', x='0', y='0')
        self.mm_label_main = tk.Label(self.Main_frame)
        self.mm_label_main.configure(background='#1a543e', compound='bottom', font='{ARVO} 14 {italic}',
                                     foreground='white')
        self.mm_label_main.configure(text='Message Management')
        self.mm_label_main.place(anchor='nw', relx='0.21', rely='0.4', x='0', y='0')
        self.separator_main = ttk.Separator(self.Main_frame)
        self.separator_main.configure(orient='horizontal')
        self.separator_main.pack(fill='y', ipady='200', pady='50', side='top')
        self.s_label_main = ttk.Label(self.Main_frame)
        self.s_label_main.configure(background='#1a543e', font='{ARVO} 14 {italic}', foreground='white', text='System')
        self.s_label_main.place(anchor='nw', relx='0.28', rely='0.45', x='0', y='0')
        self.welcome_label_main = ttk.Label(self.Main_frame)
        self.welcome_label_main.configure(background='#1a543e', font='{ARVO} 24 {italic}', foreground='White',
                                          text='Welcome')
        self.welcome_label_main.place(anchor='nw', relx='0.65', rely='0.15', x='0', y='0')
        self.username_entry_main = ttk.Entry(self.Main_frame)
        self.username_entry_main.configure(font='{ARVO} 12 {italic}')
        self.username_entry_main.place(anchor='nw', relx='0.69', rely='0.4', x='0', y='0')
        self.passwird_entry_main = ttk.Entry(self.Main_frame)
        self.passwird_entry_main.configure(font='{ARVO} 12 {italic}')
        self.passwird_entry_main.place(anchor='nw', relx='0.69', rely='0.55', x='0', y='0')
        self.username_label_main = ttk.Label(self.Main_frame)
        self.username_label_main.configure(background='#1a543e', font='{ARVO} 14 {italic}', foreground='white',
                                           text='Username :')
        self.username_label_main.place(anchor='nw', relx='0.51', rely='0.4', x='0', y='0')
        self.password_label_main = ttk.Label(self.Main_frame)
        self.password_label_main.configure(background='#1a543e', font='{AVRO} 14 {italic}', foreground='white',
                                           text='Password :')
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
        if (self.username_entry_main.get() == 'Admin') and (self.passwird_entry_main.get() == 'Admin'):
            self.master.destroy()
            call_dashboard()
            print('correct password')

        else:
            print('Incorrect Password')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Admin Login')
    root.resizable(height=False, width=False)
    app = AdminLogin(root)
    app.run()


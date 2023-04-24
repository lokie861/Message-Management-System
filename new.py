#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3
import smtplib

location='/home/pc/Desktop/VS Workspace/message_manage/assets/images/'
#Sqlite3 connection commands
connection = sqlite3.connect('example.db')
cursur = connection.cursor()

#smtp sending amil commands from and app Password
from_mail='lokie2301@gmail.com'
password='gcchfctpododhunv'

#smtp objects
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.starttls()
smtp_obj.login(from_mail,password)

#Create a table command 
#cursur.execute("create table Example(ERP int(3) primary key,Name varchar(25),Year number(4),Department varchar(20),Mail varchar(40),Contact varchar(35))")

class AddDetails:
    def __init__(self, master):
        # build ui
        self.det=str()
        self.master = master
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(self.frame1)
        self.label1 = tk.Label(self.frame2)
        self.img_last = tk.PhotoImage(file=f'{location}last.png')
        self.label1.configure(image=self.img_last, text='label1')
        self.label1.place(anchor='nw', relx='0.21', rely='0.4', x='0', y='0')
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(background='skyblue', font='{Avero} 18 {bold italic}', text='ADD DETAILS ')
        self.label2.place(anchor='nw', relx='0.17', rely='0.1', x='0', y='0')
        self.frame2.configure(background='skyblue', height='500', width='275')
        self.frame2.place(anchor='nw', x='0', y='0')
        self.back_button_add = tk.Button(self.frame1)
        self.back_button_add = tk.Button(self.frame1)
        self.back_button_add.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            justify="right",
            text=' Back  ')
        self.back_button_add.place(anchor="nw", relx=0.39, rely=0.02, y=0)
        self.back_button_add.configure(command=self.back)
        self.erp_label_add = tk.Label(self.frame1)
        self.erp_label_add.configure(background='#cbf0f7', font='{revo} 12 {italic}', text='ERP  ')
        self.erp_label_add.place(anchor='nw', relx='0.4', rely='0.25', x='0', y='0')
        self.erp_entry_add = tk.Entry(self.frame1)
        self.erp_entry_add.configure(font='{aervo} 12 {italic}')
        self.erp_entry_add.place(anchor='nw', relx='0.55', rely='0.25', width='250', x='0', y='0')
        self.name_label_add = tk.Label(self.frame1)
        self.name_label_add.configure(background='#cbf0f7', font='{revo} 12 {italic}', text='Name ')
        self.name_label_add.place(anchor='nw', relx='0.4', rely='0.35', x='0', y='0')
        self.Contact_entry_add = tk.Entry(self.frame1)
        self.Contact_entry_add.configure(font='{aervo} 12 {italic}')
        self.Contact_entry_add.place(anchor='nw', relx='0.55', rely='0.75', width='250', x='0', y='0')
        self.name_entry_add = tk.Entry(self.frame1)
        self.name_entry_add.configure(font='{aervo} 12 {italic}')
        self.name_entry_add.place(anchor='nw', relx='0.55', rely='0.35', width='250', x='0', y='0')
        self.mail_id_add = tk.Label(self.frame1)
        self.mail_id_add.configure(background='#cbf0f7', font='{revo} 12 {italic}', text='Mail ID ')
        self.mail_id_add.place(anchor='nw', relx='0.4', rely='0.45', x='0', y='0')
        self.label4 = ttk.Label(self.frame1)
        self.label4.configure(background='#cbf0f7', font='{aevo} 12 {italic}', text='Contact')
        self.label4.place(anchor='nw', relx='0.4', rely='0.75', x='0', y='0')
        self.mail_entry_add = tk.Entry(self.frame1)
        self.mail_entry_add.configure(font='{aervo} 12 {italic}')
        self.mail_entry_add.place(anchor='nw', relx='0.55', rely='0.45', width='250', x='0', y='0')
        self.add_button_add = tk.Button(self.frame1)
        self.add_button_add.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            text='  ADD  ')
        self.add_button_add.place(anchor="nw", relx=0.75, rely=0.85, x=0, y=0)
        self.add_button_add.configure(command=self.add_details)
        self.year_label_add = tk.Label(self.frame1)
        self.year_label_add.configure(background='#cbf0f7', font='{revo} 12 {italic}', text='Year')
        self.year_label_add.place(anchor='nw', relx='0.4', rely='0.55', x='0', y='0')
        self.depart_label_add = tk.Label(self.frame1)
        self.depart_label_add.configure(background='#cbf0f7', font='{revo} 12 {italic}', text='Department')
        self.depart_label_add.place(anchor='nw', relx='0.4', rely='0.65', x='0', y='0')
        self.year_entry_add = tk.Entry(self.frame1)
        self.year_entry_add.configure(font='{aervo} 12 {italic}')
        self.year_entry_add.place(anchor='nw', relx='0.55', rely='0.55', width='250', x='0', y='0')
        self.depart_entry_add = tk.Entry(self.frame1)
        self.depart_entry_add.configure(font='{aervo} 12 {italic}')
        self.depart_entry_add.place(anchor='nw', relx='0.55', rely='0.65', width='250', x='0', y='0')
        self.frame1.configure(background='#cbf0f7', height='500', width='800')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1
    
    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        self.master.destroy()
        call_dashboard()

    def add_details(self):
        if not (self.erp_entry_add.get() == '' or self.name_entry_add.get() == '' or self.year_entry_add.get() == '' or self.depart_entry_add.get() == '' or self.mail_entry_add.get() == '' or self.Contact_entry_add.get() == ''):

            self.det=f'{self.erp_entry_add.get()},"{self.name_entry_add.get()}",{self.year_entry_add.get()},"{self.depart_entry_add.get()}","{self.mail_entry_add.get()}","{self.Contact_entry_add.get()}"'
            cursur.execute('insert into Example(ERP,Name,Year,Mail,Department,Contact) values({});'.format(self.det))
            print('{}\n{}\n{}\n{}\n{}\n{}'.format(self.erp_entry_add.get(),self.name_entry_add.get(),self.year_entry_add.get(),self.depart_entry_add.get(),self.mail_entry_add.get(),self.Contact_entry_add.get()))
            cursur.execute('commit;')
            messagebox.showinfo('Info','\nDetails Added Successfully.  \n')
            self.clear()
        else:
            messagebox.showwarning('Warning','Fill all the Details.  ')
    def clear(self):
        self.erp_entry_add.delete(0,'end')
        self.name_entry_add.delete(0,'end')
        self.year_entry_add.delete(0,'end')
        self.depart_entry_add.delete(0,'end')
        self.mail_entry_add.delete(0,'end')
        self.Contact_entry_add.delete(0,'end')


class UpdatePage:
    def __init__(self, master):
        # build ui
        self.master = master
        self.det=str()
        self.ans=list()
        self.Main_Frame = tk.Frame(master)
        self.blue_frame = tk.Frame(self.Main_Frame)
        self.Update_image = tk.Label(self.blue_frame)
        self.img_update = tk.PhotoImage(file=f'{location}update.png')
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
        self.Contact_label_update = tk.Label(self.Main_Frame)
        self.Contact_label_update.configure(background='#edf5fa', font='{avero} 12 {italic}', text='Contact')
        self.Contact_label_update.place(anchor='nw', relx='0.38', rely='0.7', x='0', y='0')
        self.depart_entry_update = tk.Entry(self.Main_Frame)
        self.depart_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.depart_entry_update.place(anchor='nw', relx='0.55', rely='0.6', x='0', y='0')
        self.Contact_entry_update = tk.Entry(self.Main_Frame)
        self.Contact_entry_update.configure(font='{avero} 12 {}', highlightthickness='0')
        self.Contact_entry_update.place(anchor='nw', relx='0.55', rely='0.7', x='0', y='0')
        self.back_button_update = tk.Button(self.Main_Frame)
        self.back_button_update.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            text='  Back  ')
        self.back_button_update.place(anchor="nw", relx=0.37, rely=0.029, x=0, y=0)
        self.back_button_update.configure(command=self.back)
        self.update_button_update = tk.Button(self.Main_Frame)
        self.update_button_update.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            text=' Update ')
        self.update_button_update.place(anchor="nw", relx=0.8, rely=0.84, x=0, y=0)
        self.update_button_update.configure(command=self.update)
        self.button1 = tk.Button(self.Main_Frame)
        self.button1.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            text='  OK  ')
        self.button1.place(anchor="nw", relx=0.85, rely=0.17, x=0, y=0)
        self.button1.configure(command=self.ok)
        self.label1 = ttk.Label(self.Main_Frame)
        #self.label1.configure(background='#edf5fa', text='Note: The Date format should be YYYY/MM/DD')
        self.label1.place(anchor='nw', relx='0.38', rely='0.9', x='0', y='0')
        self.Main_Frame.configure(background='#edf5fa', height='500', width='800')
        self.Main_Frame.pack(side='top')

        # Main widget
        self.mainwindow = self.Main_Frame

    def run(self):
        self.mainwindow.mainloop()

    def back(self):
        self.master.destroy()
        call_dashboard()


    def update(self):
        self.det=f'Name="{self.name_entry_update.get()}",Year={self.year_entry_update.get()},Department="{self.depart_entry_update.get()}",Mail="{self.mail_id_entry_update.get()}",Contact="{self.Contact_entry_update.get()}"'
        cursur.execute(f'update Example set {self.det} where ERP={self.erp_entry_update.get()}')
        cursur.execute('commit;')
        messagebox.showinfo('Info','\nDetails Updated Successfully.  \n')

        print("Details Updated Successfully \n" + self.det)
        self.clear()
        
    def ok(self): 

        
        self.name_entry_update.delete(0,'end')
        self.year_entry_update.delete(0,'end')
        self.depart_entry_update.delete(0,'end')
        self.mail_id_entry_update.delete(0,'end')
        self.Contact_entry_update.delete(0,'end')
                                              
        cursur.execute(f'select * from Example where ERP={self.erp_entry_update.get()};')
        for x in cursur:
            self.ans=x
        self.name_entry_update.insert(0,self.ans[1])
        self.year_entry_update.insert(0,self.ans[2])
        self.depart_entry_update.insert(0,self.ans[3])
        self.mail_id_entry_update.insert(0,self.ans[4])
        self.Contact_entry_update.insert(0,self.ans[5])
        
        self.ans=[]
        

    def clear(self):
        self.erp_entry_update.delete(0,'end')
        self.name_entry_update.delete(0,'end')
        self.year_entry_update.delete(0,'end')
        self.depart_entry_update.delete(0,'end')
        self.mail_id_entry_update.delete(0,'end')
        self.Contact_entry_update.delete(0,'end')

class DeletePage:
    def __init__(self, master):
        # build ui
        self.master = master
        self.Main_frame = tk.Frame(master)
        self.grey_frame = tk.Frame(self.Main_frame)
        self.image_label_delete = tk.Label(self.grey_frame)
        self.img_deletee = tk.PhotoImage(file=f'{location}deletee.png')
        self.image_label_delete.configure(image=self.img_deletee, text='label1')
        self.image_label_delete.place(anchor='nw', relx='0.17', rely='0.3', x='0', y='0')
        self.label2 = tk.Label(self.grey_frame)
        self.label2.configure(background='grey', font='{avro} 14 {bold italic}', foreground='white',text='Delete Details')
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
        self.note_label_delete.configure(background='white', font='{timesnew} 10 {}',text="Note: Once deleted can't be recovered")
        self.note_label_delete.place(anchor='nw', relx='0.35', rely='0.9', x='0', y='0')
        self.delete_button_delete = tk.Button(self.Main_frame)
        self.delete_button_delete.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            text=' Delete ')
        self.delete_button_delete.place(anchor="nw", relx=0.8, rely=0.55, x=0, y=0)
        self.delete_button_delete.configure(command=self.detele_details)
        self.back_button_delete = tk.Button(self.Main_frame)
        self.back_button_delete.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            text='  Back  ')
        self.back_button_delete.place(anchor="nw", relx=0.37, rely=0.04, x=0, y=0)
        self.back_button_delete.configure(command=self.back)
        self.Main_frame.configure(background='white', height='500', width='800')
        self.Main_frame.pack(side='top')

        # Main widget
        self.mainwindow = self.Main_frame

    def run(self):
        self.mainwindow.mainloop()

    def detele_details(self):
        cursur.execute(f'delete from Example where ERP={self.erp_entry_delete.get()};')
        messagebox.askyesno('Warning ','\nAre you sure to Delete the Details?  \n')
        cursur.execute('commit;')
        self.erp_entry_delete.delete(0,'end')
        print('\n Details Deleted Successfully...')
    def back(self):
        self.master.destroy()
        call_dashboard()

class SendMail:
    def __init__(self, master):
        # build ui
        self.all_flag=0
        self.erp = list()
        self.mailids = list()
        self.subject=str()
        self.message=str()
        self.erpstring=str()
        self.master = master
        self.main_frame = tk.Frame(master)
        self.blue_frame = tk.Frame(self.main_frame)
        self.mai_image_send = tk.Label(self.blue_frame)
        self.back_button_add = tk.Button(self.main_frame)
        self.back_button_add.configure(borderwidth='1',highlightthickness='0')
        self.back_button_add.configure(text='  Back  ')
        self.back_button_add.place(anchor='nw', relx='0.84', rely='0.02', y='0')
        self.back_button_add.configure(command=self.back)
        self.img_mail_send = tk.PhotoImage(file=f'{location}mail_send.png')
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
        self.body_text_send.configure(height='10', width=50)
        self.body_text_send.place(anchor='nw', relx='0.4', rely='0.3', width='365', x='0', y='0')
        self.list_erp_label_send = tk.Label(self.main_frame)
        self.list_erp_label_send.configure(background='#cafae6', font='{avro} 12 {italic}', text='List of ERP')
        self.list_erp_label_send.place(anchor='nw', relx='0.4', rely='0.65', x='0', y='0')
        self.seperate_label_send = tk.Label(self.main_frame)
        self.seperate_label_send.configure(background='#cafae6', text='(separated by , )')
        self.seperate_label_send.place(anchor='nw', relx='0.51', rely='0.65', x='0', y='0')
        self.erp_text_send = tk.Text(self.main_frame)
        self.erp_text_send.configure(height='10', width=50)
        self.erp_text_send.place(anchor='nw', height='75', relx='0.4', rely='0.7', width='365', x='0', y='0')
        self.all_checkbutton_send = tk.Checkbutton(self.main_frame)
        self.all_checkbutton_send.configure(background='#cafae6',activebackground='#cafae6', font='{avro} 12 {}', text='  All')
        self.all_checkbutton_send.place(anchor='nw', relx='0.4', rely='0.85', x='0', y='0')
        self.all_checkbutton_send.configure(command=self.all_mail)
        self.cm_label_send = tk.Label(self.main_frame)
        self.cm_label_send.configure(background='#cafae6', font='{avro} 14 {bold italic}', text='Compose Mail')
        self.cm_label_send.place(anchor='nw', relx='0.4', rely='0.04', x='0', y='0')
        self.send_send = tk.Button(self.main_frame)
        self.send_send.configure(
            borderwidth=1,
            font="{Aero} 12 {italic}",
            highlightthickness=0,
            text='  Send  ')
        self.send_send.place(anchor="nw", relx=0.86, rely=0.9, x=0, y=0)
        self.send_send.configure(command=self.send_mail)
        self.main_frame.configure(background='#cafae6', borderwidth='0', height='500', highlightbackground='#cafae6', highlightthickness='0')
        self.main_frame.configure(highlightcolor='#cafae6', highlightthickness='0', width='800')
        self.main_frame.pack(expand='false', side='top')
        

        # Main widget
        self.mainwindow = self.main_frame

    def run(self):
        self.mainwindow.mainloop()

    def all_mail(self):
        self.erp_text_send.configure(state='disabled')
        self.all_flag=1

    def send_mail(self):
        self.message=self.body_text_send.get('1.0','end')

        self.subject=self.subject_entry_send.get()
        self.message=f'Subject:{self.subject}\n\n' + self.message
        if self.all_flag==0:

            self.erpstring=self.erp_text_send.get('1.0','end')
            self.erpstring.replace('\n',' ')
            self.erpstring=self.erpstring.split(',')
            

            for x in self.erpstring:
                self.erp.append(int(x))
            

            for x in self.erp:
                cursur.execute(f'select Department from Example where ERP={x};')
                for i in cursur:
                    self.mailids.append(i[0])

        else:

            cursur.execute('select ERP from Example;')
            for x in cursur:
                self.erp.append(x[0])

            cursur.execute('select Department from Example')
            for x in cursur:
                self.mailids.append(x[0])    

        print(self.erp)
        print(self.mailids)
        
        for i in range(len(self.mailids)):
            smtp_obj.sendmail(from_mail,self.mailids[i],self.message)
            print('Mail sent Successfully to ' + self.mailids[i])

        self.body_text_send.delete('1.0','end')
        self.erp_text_send.delete('1.0','end')
        self.subject_entry_send.delete(0,'end')
        print('\n\nMail sent Successfully.....')
        messagebox.showinfo('Info ','Mail sent Successfully.  ')
        self.mailids=[]
        self.erp=[]

    def back(self):
        self.master.destroy()
        call_dashboard()

class DashboardApp:
    def __init__(self, master):
        # build ui
        self.master = master
        self.frame1 = tk.Frame(master)
        self.Main_frame = tk.Frame(self.frame1)
        self.Main_frame.configure(background='white', height='200', width='800')
        self.Main_frame.place(anchor='nw', x='0', y='0')
        self.button2 = tk.Button(self.frame1)
        self.img_mail_dashboard1 = tk.PhotoImage(file=f'{location}mail_dashboard.png')
        self.button2.configure(borderwidth='0', highlightthickness='0', image=self.img_mail_dashboard1,text='Send_Mail')
        self.button2.place(anchor='nw', relx='0.78', rely='0.2', x='0', y='0')
        self.button2.configure(command=self.open_sendmail_panel)
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(background='white', font='{Avro} 25 {bold italic}', text='DashBoard')
        self.label1.place(anchor='nw', relx='0.02', rely='0.03', x='0', y='0')
        self.delete_button_dash = tk.Button(self.frame1)
        self.img_delete_dash = tk.PhotoImage(file=f'{location}delete_dash.png')
        self.delete_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_delete_dash,text='delete button')
        self.delete_button_dash.place(anchor='nw', relx='0.53', rely='0.2', x='0', y='0')
        self.delete_button_dash.configure(command=self.open_delete_panel)
        self.add_button_dash = tk.Button(self.frame1)
        self.img_add_dash = tk.PhotoImage(file=f'{location}add_dash.png')
        self.add_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_add_dash,text='add details')
        self.add_button_dash.place(anchor='nw', relx='0.03', rely='0.2', x='0', y='0')
        self.add_button_dash.configure(command=self.open_add_panel)
        self.update_button_dash = tk.Button(self.frame1)
        self.img_update_dash = tk.PhotoImage(file=f'{location}update_dash.png')
        self.update_button_dash.configure(borderwidth='0', highlightthickness='0', image=self.img_update_dash,text='update button')
        self.update_button_dash.place(anchor='nw', relx='0.28', rely='0.2', x='0', y='0')
        self.update_button_dash.configure(command=self.open_update_panel)
        self.label2 = tk.Label(self.frame1)
        self.label2.configure(background='black', font='{avro} 14 {bold italic}', foreground='White',text='Add Details')
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
                              text='Message Management')
        self.label7.place(anchor='nw', relx='0.64', rely='0.93', x='0', y='0')
        self.frame1.configure(background='black', borderwidth='0', height='500', highlightthickness='0')
        self.frame1.configure(width='800')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1

    def run(self):
        self.mainwindow.mainloop()

    def open_sendmail_panel(self):
        self.master.destroy()
        call_sendmail_page()

    def open_delete_panel(self):
        self.master.destroy()
        call_deletedetails_page()

    def open_add_panel(self):
        self.master.destroy()
        call_adddetails_page()


    def open_update_panel(self):
        self.master.destroy()
        call_updatedetails_page()

def call_dashboard():
    root1 = tk.Tk()
    root1.resizable(height=False,width=False)
    root1.title('DashBoard')
    dash = DashboardApp(root1)
    dash.run()

def call_adddetails_page():
    root2 = tk.Tk()
    root2.resizable(height=False,width=False)
    root2.title('Add Details')
    add_details = AddDetails(root2)
    add_details.run()

def call_updatedetails_page():
    root3 = tk.Tk()
    root3.resizable(height=False,width=False)
    root3.title('Update Details')
    update_details = UpdatePage(root3)
    update_details.run()

def call_deletedetails_page():
    root5 =tk.Tk()
    root5.resizable(height=False,width=False)
    root5.title('Delete Details')
    delete_details = DeletePage(root5)
    delete_details.run()

def call_sendmail_page():
    root4 = tk.Tk()
    root4.resizable(height=False,width=False)
    root4.title('Send Mail')
    send_mail = SendMail(root4)
    send_mail.run()

class AdminLogin:
    def __init__(self, master):
        # build ui
        self.master = master
        self.Main_frame = tk.Frame(master)
        self.image_label_main = ttk.Label(self.Main_frame)
        self.img_image = tk.PhotoImage(file=f'{location}image.png')
        self.image_label_main.configure(image=self.img_image, text='label2')
        self.image_label_main.place(anchor='nw', relx='0.02', rely='0.34', x='0', y='0')
        self.mm_label_main = tk.Label(self.Main_frame)
        self.mm_label_main.configure(background='#1a543e', compound='bottom', font='{ARVO} 14 {italic}', foreground='white')
        self.mm_label_main.configure(text='Message Management ')
        self.mm_label_main.place(anchor='nw', relx='0.21', rely='0.4', x='0', y='0')
        self.separator_main = ttk.Separator(self.Main_frame)
        self.separator_main.configure(orient='horizontal')
        self.separator_main.pack(fill='y', ipady='200', pady='50', side='top')
        self.s_label_main = ttk.Label(self.Main_frame)
        self.s_label_main.configure(background='#1a543e', font='{ARVO} 14 {italic}', foreground='white', text='Using E-Mail')
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
        if (self.username_entry_main.get() == '') and (self.passwird_entry_main.get() == '' ):
            messagebox.showinfo('Info', 'Login Successfull.  ')
            self.master.destroy()
            print('correct password....\nLogging in \n')
            call_dashboard()

        else:

            messagebox.showwarning("Warning",'Incorrect Details.   ')
            self.username_entry_main.delete(0,'end')
            self.passwird_entry_main.delete(0,'end')
            print('Incorrect Password.... Try again\n')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Admin Login')
    root.resizable(height=False, width=False)
    app = AdminLogin(root)
    app.run()


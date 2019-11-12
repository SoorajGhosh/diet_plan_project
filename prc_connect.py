import sqlite3
from tkinter import *
from tkinter import messagebox




#=====================BackEnd===========================





# database operations include inserting and updating and retrieving

conn = sqlite3.connect("prc_db.db")
c = conn.cursor()

def create_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS client(
					c_id TEXT NOT NULL PRIMARY KEY,
					c_name TEXT NOT NULL,
					c_height REAL)
				""")

create_table()

#inserting Data
def insert_client(cl):
	with conn:
		c.execute( "INSERT INTO client VALUES (:c_id, :c_name, :c_height)",
			{'c_id':cl.cl_id, 'c_name':cl.name, 'c_height':cl.height })

# QUERRY TABLES #

#
def get_all_clients():
	with conn:
		c.execute("SELECT * FROM client")
	return c.fetchall()

# selecting a specific client
def get_client_by_id(client_id):
	with conn:
		c.execute("SELECT * FROM client WHERE c_id = :client_id", {'client_id':client_id})
	return c.fetchone()


# UPDATE TABLES #

def update_client_by_id(client_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE client SET {upd_fld} = :upd_val WHERE c_id = :client_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'client_id':client_id})


# DELETE ENTRY #

def delete_client_by_id(client_id):
	with conn:
		c.execute("DELETE FROM client WHERE c_id = :client_id", {'client_id':client_id})






class Client():
	def __init__(self,cl_id,nm,hg):
		self.cl_id = cl_id
		self.name = nm
		self.height = hg
try:
	default_client = get_client_by_id(1)
	activeClient = Client(default_client[0],default_client[1],default_client[2])
except:
	print("No Data found")


#=====================FrontEnd===========================

class Root(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		
		for F in (DetailsFrame,InsertFrame,UpdateFrame):
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')
		
		self.show_frame(DetailsFrame)
		
	def show_frame(self,f):
		frame = self.frames[f]
		if f == DetailsFrame:	#this updates the lis in the detail frame
			frame.update_list()
		elif f == UpdateFrame:	# this is to update the frame with before viewing it
			frame.set_text()
		frame.tkraise()



class DetailsFrame(Frame):
	def __init__(self,parent,controller):
		
		self.controller =controller

		Frame.__init__(self,parent,bg="white")
		cl_heading = Label(self, text ="Client", font=('Helvetica',12), bg = "light green")	# label of the name
		cl_heading.pack(side=TOP,  fill="x")
		
		# client List Box

		self.cl_lbx = Listbox(self, font=('Verdana',16))
		self.cl_lbx.pack(side=LEFT,fill="both",expand=True)
		cl_sbr = Scrollbar(self,)
		cl_sbr.pack(side=RIGHT,fill="both")
		cl_sbr.config(command= self.cl_lbx.yview)
		self.cl_lbx.config(yscrollcommand=cl_sbr.set)

		self.update_list()

		# Buttons
		self.btnAddData=Button(self,text ="Add New", font=('arial',11,'bold'), height=1, width=16, bd=2, command = lambda:controller.show_frame(InsertFrame))
		self.btnAddData.pack()		# grid(row=0,column=0, padx=3, pady=1.5, sticky='nsew')

		self.btnUpdData=Button(self,text ="Update", font=('arial',11,'bold'), height=1, width=16, bd=2, command = self.update_client)# lambda:controller.show_frame(UpdateFrame))# lambda:controller.show_frame(UpdateFrame))
		self.btnUpdData.pack()		# grid(row=0,column=0, padx=3, pady=1.5, sticky='nsew')

		self.btnDelData=Button(self,text ="Delete", font=('arial',11,'bold'), height=1, width=16, bd=2, command = self.del_cl)# lambda:controller.show_frame(UpdateFrame))
		self.btnDelData.pack()

	def active_client(self):
		client = self.cl_lbx.get(ACTIVE)
		global activeClient
		activeClient = Client(client[0],client[1],client[2])
		return client[0]

	def update_client(self):
		self.active_client()
		global activeClient
		self.controller.show_frame(UpdateFrame)

	def update_list(self):
		clients = get_all_clients()		# use a better method for more data to handle like , generator
		self.cl_lbx.delete(0,END)
		for client in range(len(clients)):
			self.cl_lbx.insert(client,clients[client])

	def del_cl(self):
		c_id = self.active_client()
		messagebox.showinfo('Client', f'Deleting Client {get_client_by_id(c_id)[1]}')
		delete_client_by_id(c_id)
		self.update_list()


class InsertFrame(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="black")

		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)
		# self.grid_columnconfigure(1,weight=1)

		cl_id=StringVar()
		id_lbl = Label(self, text ="ID",font=('Helvetica',12))	
		id_lbl.grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.id_entry = Entry(self, textvariable = cl_id)	
		self.id_entry.grid(row=0,column=1, sticky='nsew', padx = 10, pady =10)

		cl_name=StringVar()
		name_lbl = Label(self, text ="Name",font=('Helvetica',12))	
		name_lbl.grid(row=1, column=0, sticky='nsew', padx = 10, pady = 10)

		self.name_entry = Entry(self, textvariable = cl_name)	
		self.name_entry.grid(row=1,column=1, sticky='nsew', padx = 10, pady =10)

		cl_hgt=StringVar()
		hgt_lbl = Label(self, text ="Height",font=('Helvetica',12))	
		hgt_lbl.grid(row=2, column=0, sticky='nsew', padx = 10, pady = 10)

		self.hgt_entry = Entry(self, textvariable = cl_hgt)	
		self.hgt_entry.grid(row=2,column=1, sticky='nsew', padx = 10, pady =10)

		# Buttons
		self.btnAddData = Button(self,text = "Create", font=('arial',11,'bold'), bd=2, command = lambda:self.create_client(cl_id = cl_id.get(), nm = cl_name.get(), hg = cl_hgt.get()))
		self.btnAddData.grid(row=0,column=2, padx=3, pady=1.5, sticky='nsew')

		self.btnBackData = Button(self,text = "Back", font=('arial',11,'bold'), bd=2, command = lambda:controller.show_frame(DetailsFrame))
		self.btnBackData.grid(row=1,column=2, padx=3, pady=1.5, sticky='nsew')

	
	def clear_all(self):
		self.id_entry.delete(0,END)
		self.name_entry.delete(0,END)
		self.hgt_entry.delete(0,END)

	def create_client(self,cl_id,nm,hg):
		cl = Client(cl_id,nm,hg)
		try:
			if cl_id=='' or nm=="" or hg==0:
				pass
			else:
				insert_client(cl)
				messagebox.showinfo('Creating New Client', f'{get_client_by_id(cl_id)[1]} Added Successfully')	
			self.clear_all()
		except:
			messagebox.showinfo('Client ID error',"The client id you specified already exists..!") 

		



class UpdateFrame(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="black")
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)

		self.upd_id=StringVar()
		self.id_lbl = Label(self, text ="ID",font=('Helvetica',12))	
		self.id_lbl.grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.id_entry = Entry(self, textvariable = self.upd_id)	
		self.id_entry.grid(row=0,column=1, sticky='nsew', padx = 10, pady =10)

		self.upd_name=StringVar()
		self.name_lbl = Label(self, text ="Name",font=('Helvetica',12))	
		self.name_lbl.grid(row=1, column=0, sticky='nsew', padx = 10, pady = 10)

		self.name_entry = Entry(self, textvariable = self.upd_name)	
		self.name_entry.grid(row=1,column=1, sticky='nsew', padx = 10, pady =10)

		self.upd_hgt=StringVar()
		self.hgt_lbl = Label(self, text ="Height",font=('Helvetica',12))	
		self.hgt_lbl.grid(row=2, column=0, sticky='nsew', padx = 10, pady = 10)

		self.hgt_entry = Entry(self, textvariable = self.upd_hgt)	
		self.hgt_entry.grid(row=2,column=1, sticky='nsew', padx = 10, pady =10)


		self.org_client_dict = {'c_id':self.upd_id.get(),'c_name':self.upd_name.get(),'c_height':self.upd_hgt.get()}
		self.set_text()

		# Buttons
		self.btnUpdData=Button(self,text = "Update", font=('arial',11,'bold'), bd=2,command = lambda:self.update_client()) # command = lambda:controller.show_frame(InsertFrame))
		self.btnUpdData.grid(row=0,column=2, padx=3, pady=1.5, sticky='nsew')


		self.btnBackData=Button(self,text = "Back", font=('arial',11,'bold'), bd=2, command = lambda:controller.show_frame(DetailsFrame))
		self.btnBackData.grid(row=1,column=2, padx=3, pady=1.5, sticky='nsew')
	
	

	def set_text(self):
		# clearing the previous data 
		self.id_entry.delete(0,END)
		self.name_entry.delete(0,END)
		self.hgt_entry.delete(0,END)
		# feeding the active client data into the the entry boxes
		try:
			self.id_entry.insert(0,activeClient.cl_id)
			self.name_entry.insert(0,activeClient.name)
			self.hgt_entry.insert(0,activeClient.height)
			# here it will feed the old data along with the update frame fields
			self.org_client_dict = {'c_id':activeClient.cl_id,'c_name':activeClient.name,'c_height':activeClient.height}
			print(activeClient.name)
		except:
			print("Data cannot be fed")


	def update_client(self):
		# here it will take the new data and feed it into the dict
		self.new_client_dict = {'c_id':self.upd_id.get(),'c_name':self.upd_name.get(),'c_height':float(self.upd_hgt.get())}
		print(self.org_client_dict)
		print(self.new_client_dict)

		# checking the difference 
		fields = self.new_client_dict.keys()
		update_fields = []

		# checking if no update is submitted
		if self.new_client_dict!=self.org_client_dict:
			for field in fields:
				if self.new_client_dict[field]!=self.org_client_dict[field]:
					update_fields.append(field)
					update_client_by_id(self.org_client_dict['c_id'], field, self.new_client_dict[field])
			
			messagebox.showerror('Update', f'Updated Successfully..!')

			print(update_fields)

		else:
			messagebox.showerror('Update', f'No cahnges has been done..!')
		# update_client_by_id(self.new_client_dict[id,fld,val)


app = Root()
app.mainloop()










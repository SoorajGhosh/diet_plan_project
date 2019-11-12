# Diet Plan Project GUI (FrontEnd)
import sqlite3
from tkinter import *
from tkinter import messagebox










#=========================================================== BackEnd ======================================================================


conn = sqlite3.connect("client.db")
c = conn.cursor()



#================Client DB Operations=====================

def create_client_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS client(
					c_id TEXT NOT NULL PRIMARY KEY,
					c_name TEXT NOT NULL,
					c_height REAL,
					c_weight REAL,
					c_date TEXT,
					c_addr TEXT,
					c_city TEXT,
					c_phone REAL,
					c_tot_payment REAL,
					c_payment_paid REAL,
					c_last_payment_date TEXT,
					c_payment_discount REAL,
					c_training_type TEXT,
					c_training_method TEXT,
					c_training_period REAL)
				""")


# Inserting into table
def insert_client(cl):
	with conn:
		c.execute( """INSERT INTO client VALUES (
												:c_id, :c_name, :c_height, :c_weight,:c_date,
												:c_addr, :c_city, :c_phone ,:c_tot_payment ,
												:c_payment_paid ,:c_last_payment_date ,
												:c_payment_discount ,:c_training_type ,
												:c_training_method ,:c_training_period)""",
				
				{'c_id':cl.c_id, 'c_name':cl.c_name, 'c_height':cl.c_height, 'c_weight':cl.c_weight, 
				'c_addr':cl.c_addr, 'c_city':cl.c_city, 'c_phone':cl.c_phone , 'c_date': cl.c_date,
				'c_tot_payment':cl.c_tot_payment, 'c_payment_paid' :cl.c_payment_paid ,
				'c_last_payment_date':cl.c_last_payment_date ,'c_payment_discount':cl.c_payment_discount ,
				'c_training_type':cl.c_training_type ,'c_training_method':cl.c_training_method ,'c_training_period':cl.c_training_period , }
				)

# QUERRY TABLES #

# selecting all clients
def get_all_clients():
	with conn:
		c.execute("SELECT * FROM client")
	return c.fetchall()

# selecting a specific client
def get_client_by_id(client_id):
	with conn:
		c.execute("SELECT * FROM client WHERE c_id = :client_id", {'client_id':client_id})
	return c.fetchone()

# Update client by id
def update_client_by_id(client_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE client SET {upd_fld} = :upd_val WHERE c_id = :client_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'client_id':client_id})

# DELETE ENTRY #
def delete_client_by_id(client_id):
	with conn:
		c.execute("DELETE FROM client WHERE c_id = :client_id", {'client_id':client_id})








#=========================Meal Db Operations=============================
def create_meal_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS meal(
					m_id TEXT NOT NULL PRIMARY KEY,
					m_name TEXT NOT NULL,
					m_type TEXT,
					m_desc Text)
				""")

# Inserting into table
def insert_meal(ml):
	with conn:
		c.execute( "INSERT INTO meal VALUES (:m_id, :m_name, :m_type, m_desc)",
			{'m_id':ml.id, 'm_name':ml.name, 'm_type':ml.type, 'm_desc':ml.desc})

# QUERRY TABLES #

# selecting all meal
def get_all_meals():
	with conn:
		c.execute("SELECT * FROM meal")
	return c.fetchall()

# selecting a specific meal
def get_meal_by_id(meal_id):
	with conn:
		c.execute("SELECT * FROM meal WHERE m_id = :meal_id", {'meal_id':meal_id})
	return c.fetchone()

# Update meal by id
def update_meal_by_id(meal_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE meal SET {upd_fld} = :upd_val WHERE m_id = :meal_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'meal_id':meal_id})

# DELETE ENTRY #
def delete_meal_by_id(meal_id):
	with conn:
		c.execute("DELETE FROM meal WHERE m_id = :meal_id", {'meal_id':meal_id})







#=========================Food Db Operations=============================

def create_food_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS food(
				f_id TEXT NOT NULL PRIMARY KEY,
				f_name TEXT NOT NULL,
				f_prot REAL,
				f_carbs REAL,
				f_fat REAL,
				f_qty REAL,
				f_desc Text
				)
		""")



#Inseerting food  into food table
def insert_food(fd):
	with conn:
		c.execute( "INSERT INTO food VALUES (:f_id, :f_name, :f_prot, :f_carbs, :f_fat, :f_qty, :f_desc)", 	# :meal_fk)",
			{'f_id':fd.id, 'f_name':fd.name, 'f_prot':fd.prot, 'f_carbs':fd.carbs, 'f_fat':fd.fat, 'f_qty': fd.qty, 'f_desc':fd.qty}) 	# 'meal_fk':fd.meal })


# QUERRY TABLES #

# selecting all food
def get_all_foods():
	with conn:
		c.execute("SELECT * FROM food")
	return c.fetchall()

# selecting a specific food
def get_food_by_id(food_id):
	with conn:
		c.execute("SELECT * FROM food WHERE f_id = :food_id", {'food_id':food_id})
	return c.fetchone()

# Update food by id
def update_food_by_id(food_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE food SET {upd_fld} = :upd_val WHERE f_id = :food_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'food_id':food_id})

# DELETE ENTRY #
def delete_food_by_id(food_id):
	with conn:
		c.execute("DELETE FROM food WHERE f_id = :food_id", {'food_id':food_id})









# Connecting tables to connect different tables together -===============work on this later

# this will connect the meal with the client table
# it will help us allocate different meals to different clients

def client_meal_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS client_meal(
					cm_id TEXT NOT NULL PRIMARY KEY,
					meal_fk TEXT REFERENCES meal(m_id),
					client_fk TEXT REFERENCES client(c_id))
				""")

#Inserting client_meal  into client_meal table
def insert_meal_client(clientMeal):
	with conn:
		c.execute( "INSERT INTO client_meal VALUES (:cm_id, :meal_fk, :client_fk)",
			{'cm_id':clientMeal.id, 'meal_fk':clientMeal.meal_id, 'client_fk':clientMeal.client_id}) 

# QUERRY TABLES #
# selecting all client meal
def get_all_cl_meal():
	with conn:
		c.execute("SELECT * FROM client_meal")
	return c.fetchall()

# selecting a specific client meal
def get_client_meal_by_id(cm_id):
	with conn:
		c.execute("SELECT * FROM client_meal WHERE cm_id = :cm_id", {'cm_id':cm_id})
	return c.fetchone()

# Update client meal by id
def update_client_meal_by_id(cm_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE client_meal SET {upd_fld} = :upd_val WHERE cm_id = :cm_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'cm_id':cm_id})

# DELETE ENTRY #
def delete_client_meal_by_id(cm_id):
	with conn:
		c.execute("DELETE FROM client_meal WHERE cm_id = :cm_id", {'cm_id':cm_id})








# this will connect the food with the meal table
# it will help us allocate different food to different meals

def food_in_meal_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS meal_food(
					mf_id TEXT NOT NULL PRIMARY KEY,
					food_fk TEXT  REFERENCES food(f_id),
					meal_fk TEXT REFERENCES meal(m_id),
				""")

#Inserting meal_food  into meal_food table
def insert_meal_food(clientMeal):
	with conn:
		c.execute( "INSERT INTO meal_food VALUES (:mf_id, :meal_fk, :client_fk)",
			{'mf_id':clientMeal.id, 'meal_fk':clientMeal.meal_id, 'client_fk':clientMeal.client_id}) 

# QUERRY TABLES #
# selecting all meal food
def get_all_cl_meal():
	with conn:
		c.execute("SELECT * FROM meal_food")
	return c.fetchall()

# selecting a specific meal food
def get_meal_food_by_id(mf_id):
	with conn:
		c.execute("SELECT * FROM meal_food WHERE mf_id = :mf_id", {'mf_id':mf_id})
	return c.fetchone()

# Update meal food by id
def update_meal_food_by_id(mf_id,upd_fld,upd_val):
	with conn:
		c.execute(f"UPDATE meal_food SET {upd_fld} = :upd_val WHERE mf_id = :mf_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'mf_id':mf_id})

# DELETE ENTRY #
def delete_meal_food_by_id(mf_id):
	with conn:
		c.execute("DELETE FROM meal_food WHERE mf_id = :mf_id", {'mf_id':mf_id})





# executing table creation commands

create_client_table()
create_meal_table()
create_food_table()




class Client:
	def __init__(self,c_id, c_name, c_height, c_weight,c_date,c_addr, c_city, c_phone ,c_tot_payment ,c_payment_paid ,c_last_payment_date ,c_payment_discount ,c_training_type , c_training_method ,c_training_period):
		self.c_id = c_id
		self.c_name = c_name
		self.c_height = c_height
		self.c_weight=c_weight
		self.c_date=c_date
		self.c_addr=c_addr
		self.c_city=c_city
		self.c_phone=c_phone
		self.c_tot_payment=c_tot_payment
		self.c_payment_paid=c_payment_paid
		self.c_last_payment_date = c_last_payment_date
		self.c_payment_discount=c_payment_discount
		self.c_training_type=c_training_type
		self.c_training_method = c_training_method
		self.c_training_period=c_training_period

# declared an active client
try:
	default_client = get_client_by_id(1)
	activeClientId = default_client[0]

except:
	print("No Data found")



class Meal:
	def __init__(id,name,type,client):
		self.id = id
		self.name = name
		self.type = type
		self.client = client

class Food:
	def __init__(id,name,prot,carbs,fat,qty,meal):
		self.id = id
		self.name = name
		self.prot = prot
		self.carbs = carbs
		self.fat = fat
		self.qty = qty
		self.meal = meal


# connecting classes

class MealClient:
	def __init__(cm_id, meal_fk, client_fk):
		self.cm_id = cm_id
		self.meal_fk = meal_fk
		self.client_fk = client_fk


class FoodMeal:
	def __init__(mf_id, food_fk,  meal_fk):
		self.mf_id = mf_id
		self.food_fk = food_fk
		self.meal_fk = meal_fk
		




# this is a very important fucntion as it collects the id and 
# sets the client class to hold the value of the client and returns that client which can be used anywhere in the program
def create_client_object_by_id(c_id):
	client = get_client_by_id(c_id)
	the_client = Client(c_id = client[0], 
						c_name = client[1],
						c_height = client[2], 
						c_weight= client[3], 
						c_date= client[4], 
						c_addr= client[5], 
						c_city= client[7], 
						c_phone= client[6], 
						c_tot_payment= client[8], 
						c_payment_paid= client[9], 
						c_last_payment_date = client[10], 
						c_payment_discount= client[11], 
						c_training_type= client[12], 
						c_training_method = client[13],
						c_training_period= client[14])
	return the_client

	

















#=================================================== Front-End ===================================================================
# checks if the call for AddClientPage was for adding new client or updating
update_active = False

class Root(Tk):
	def __init__(self,*args,**kwargs):
		Tk.__init__(self, *args, **kwargs)

		self.title('Diet Plan')
		self.geometry('800x500')
		self.minsize(800,500)

		container = Frame(self,bg="yellow") #Pink -- #fc6f79
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		#=================Menubar================

		menubar =Menu(self)	#Telling root that we have a menubar for you
		self.config(menu=menubar)	#Configuring roo to hae the menu as the menubar told before

		#submenues
		subMenu = Menu(menubar, tearoff=False)	#adding a new menu

		#adding cascade
		menubar.add_cascade(label="File", menu=subMenu)	#adding menu name

		#adding drop down list
		subMenu.add_command(label="Open")	#adding option in dropdown
		subMenu.add_command(label='Exit')	#adding option in dropdown

		#adding help
		subMenu = Menu(menubar, tearoff=False)
		menubar.add_cascade(label ='Help', menu = subMenu)

		#adding drop down
		subMenu.add_command(label='About Us')

		

		# ===============Adding Frames===============
		
		self.frames = {}

		for F in (StartPage,AddClientPage):
			frame = F(container, self)
			self.frames[F]=frame
			# frame.pack(fill="both", expand=True)
			frame.grid(row=0, column=0, sticky='nsew')
		self.show_frame(StartPage)
		
	def show_frame(self,f):
		frame = self.frames[f]
		if f == StartPage:	#this updates the lis in the detail frame
			frame.update_client_list()
		if f == AddClientPage:
			if update_active==True:
				frame.set_text()
			else:
				frame.clear_all()
		frame.tkraise()







class StartPage(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="blue")	#red-- #eb4034
		self.controller = controller
		self.parent = parent
		self.grid_columnconfigure(0, weight=2)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(0, weight=4)
		self.grid_rowconfigure(1, weight=4)
		self.grid_rowconfigure(1, weight=1)

		#=============Frames===================

		#client Frame
		self.clientFrame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='green')	#red--#9e0510  #width=1350, height=180,
		self.clientFrame.grid(row=0,column=0,rowspan=2,sticky='nsew', padx=5, pady=5)	#pack(side=LEFT)
		
		#Meal Frame
		self.mealFrame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='red')	#pink-- #f29da4 #width=1350, height=180,
		self.mealFrame.grid(row=0,column=1,sticky='nsew', padx=5, pady=5)	#pack(side=LEFT)

		#Food Frame
		self.foodFrame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='#7d040e')	#width=1350, height=180,
		self.foodFrame.grid(row=1,column=1,sticky='nsew', padx=5, pady=5)	#pack(side=LEFT)

		#Buttons Frame
		self.btnFrame = Frame(self, bd=1, relief=RIDGE, bg='#e30e0e')	#width=1350, height=180,  padx=1, pady=1,
		self.btnFrame.grid(row=2,column=0,columnspan=2,sticky='nsew', padx=5, pady=5)	#pack(side=LEFT)
		self.btnFrame.grid_rowconfigure(0, weight=1)
		self.btnFrame.grid_columnconfigure(0, weight=1)
		self.btnFrame.grid_columnconfigure(1, weight=1)
		self.btnFrame.grid_columnconfigure(2, weight=1)
		self.btnFrame.grid_columnconfigure(3, weight=1)
		self.btnFrame.grid_columnconfigure(4, weight=1)


		#=============List Box===================

		#Heading Label
		self.cl_heading = Label(self.clientFrame, text ="Client", font=('Helvetica',12), bg = "light green")	# label of the name
		self.cl_heading.pack(side=TOP,  fill="x")
		#client List Box
		self.cl_lbx = Listbox(self.clientFrame, font=('Verdana',8))
		self.cl_lbx.pack(side=LEFT,fill="both",expand=True)
		self.cl_sbr = Scrollbar(self.clientFrame,)
		self.cl_sbr.pack(side=RIGHT,fill="both")
		self.cl_sbr.config(command=self.cl_lbx.yview)
		self.cl_lbx.config(yscrollcommand=self.cl_sbr.set)

		#Meal List Box
		self.ml_heading = Label(self.mealFrame, text ="Meal", font=('Helvetica',12), bg = "light green")	# label of the name
		self.ml_heading.pack(side=TOP,  fill="x")
		self.ml_lbx = Listbox(self.mealFrame, font=('Verdana',16))
		self.ml_lbx.pack(side=LEFT, expand=True, fill="both")
		self.ml_sbr = Scrollbar(self.mealFrame,)
		self.ml_sbr.pack(side=RIGHT,fill="both")
		self.ml_sbr.config(command=self.ml_lbx.yview)
		self.ml_lbx.config(yscrollcommand=self.ml_sbr.set)

		#Food List Box
		self.fd_heading = Label(self.foodFrame, text ="Food", font=('Helvetica',12), bg = "light green")	# label of the name
		self.fd_heading.pack(side=TOP,  fill="x")
		self.fd_lbx = Listbox(self.foodFrame, font=('Verdana',16))
		self.fd_lbx.pack(side=LEFT, expand=True, fill="both")
		self.fd_sbr = Scrollbar(self.foodFrame,)
		self.fd_sbr.pack(side=RIGHT,fill="both")
		self.fd_sbr.config(command=self.fd_lbx.yview)
		self.fd_lbx.config(yscrollcommand=self.fd_sbr.set)

		# Buttons
		self.btnAddData=Button(self.btnFrame,text ="Add New", font=('arial',11,'bold'), height=1, width=16, bd=2, command = lambda:controller.show_frame(AddClientPage))
		self.btnAddData.grid(row=0,column=0, padx=3, pady=1.5, sticky='nsew')

		self.btnSelect = Button(self.btnFrame,text ="Select", font=('arial',11,'bold'), height=1, width=16, bd=2, command= self.active_client_id)
		self.btnSelect.grid(row=0,column=1, padx=3, pady=1.5, sticky='nsew')

		self.btnDelete=Button(self.btnFrame,text ="Delete", font=('arial',11,'bold'), height=1, width=16, bd=2, command= self.del_cl)
		self.btnDelete.grid(row=0,column=2, padx=3, pady=1.5, sticky='nsew')

		self.btnDetails=Button(self.btnFrame,text ="Details", font=('arial',11,'bold'), height=1, width=16, bd=2)
		self.btnDetails.grid(row=0,column=3, padx=3, pady=1.5, sticky='nsew')

		self.btnUpdate=Button(self.btnFrame,text ="Update", font=('arial',11,'bold'), height=1, width=16, bd=2,command= self.update_client)
		self.btnUpdate.grid(row=0,column=4, padx=3, pady=1.5, sticky='nsew')


		self.update_client_list()

	# Associated operations

	# client listbox Operations

	def active_client_id(self):
		client = self.cl_lbx.get(ACTIVE)
		global activeClientId
		activeClientId = client[0]
		return activeClientId

	def update_client(self):
		self.active_client_id()
		global update_active
		update_active = True
		global activeClientId
		self.controller.show_frame(AddClientPage)

	def update_client_list(self):
		clients = get_all_clients()		# use a better method for more data to handle like , generator
		self.cl_lbx.delete(0,END)
		for client in range(len(clients)):
			self.cl_lbx.insert(client,f'{clients[client][0]}   {clients[client][1]}')

	def del_cl(self):
		c_id = self.active_client_id()
		messagebox.showinfo('Client', f'Deleting Client {get_client_by_id(c_id)[1]}')
		delete_client_by_id(c_id)
		self.update_client_list()







# Adding new client
class AddClientPage(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="black")
		self.controller = controller
		self.parent = parent
		


		self.grid_rowconfigure(0, weight=4)
		self.grid_rowconfigure(1, weight=4)
		self.grid_rowconfigure(1, weight=1)		# here is an error but it makes the gui look better the error is the index of the row shoild be  here
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

		#=================Frame===============

		# Personal detail Frame
		self.cl_prsl_dtl_frame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='#4287f5')
		self.cl_prsl_dtl_frame.grid(row=0,column=0,rowspan=2,sticky='nsew', padx=5, pady=5)
		self.cl_prsl_dtl_frame.grid_columnconfigure(0, weight=1)
		self.cl_prsl_dtl_frame.grid_columnconfigure(1, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(0, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(1, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(2, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(3, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(4, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(5, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(6, weight=1)
		self.cl_prsl_dtl_frame.grid_rowconfigure(7, weight=1)

		# Payment Frame
		self.cl_pmnt_dtl_frame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='#ce42f5')
		self.cl_pmnt_dtl_frame.grid(row=0,column=1,columnspan=1,sticky='nsew', padx=5, pady=5)
		self.cl_pmnt_dtl_frame.grid_columnconfigure(0, weight=1)
		self.cl_pmnt_dtl_frame.grid_columnconfigure(1, weight=1)
		self.cl_pmnt_dtl_frame.grid_rowconfigure(0, weight=1)
		self.cl_pmnt_dtl_frame.grid_rowconfigure(1, weight=1)
		self.cl_pmnt_dtl_frame.grid_rowconfigure(2, weight=1)
		self.cl_pmnt_dtl_frame.grid_rowconfigure(3, weight=1)

		# Training Frame
		self.cl_trng_dtl_frame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='#66f542')
		self.cl_trng_dtl_frame.grid(row=1,column=1,columnspan=1,sticky='nsew', padx=5, pady=5)
		self.cl_trng_dtl_frame.grid_columnconfigure(0, weight=1)
		self.cl_trng_dtl_frame.grid_columnconfigure(1, weight=1)
		self.cl_trng_dtl_frame.grid_rowconfigure(0, weight=1)
		self.cl_trng_dtl_frame.grid_rowconfigure(1, weight=1)
		self.cl_trng_dtl_frame.grid_rowconfigure(2, weight=1)

		# Buttons Frame
		self.cl_btn_frame = Frame(self, bd=1, padx=1, pady=1, relief=RIDGE, bg='#eb4034')
		self.cl_btn_frame.grid(row=2,column=0,columnspan=2,sticky='nsew', padx=5, pady=5)
		self.cl_btn_frame.grid_columnconfigure(0, weight=1)
		self.cl_btn_frame.grid_columnconfigure(1, weight=1)
		self.cl_btn_frame.grid_columnconfigure(2, weight=1)
		self.cl_btn_frame.grid_columnconfigure(3, weight=1)
		

		#=================varialbles====================
		self.cl_id = StringVar()
		self.cl_name = StringVar()
		self.cl_height = StringVar()		# client Height (for BMI)
		self.cl_weight = StringVar()		# client Weight (for BMI)
		self.cl_date= StringVar()			# date he became client
		self.cl_addr = StringVar()			# clients full address
		self.cl_phone = StringVar()			# clients phone Number
		self.cl_city = StringVar()			# to segregate based on city
		self.cl_tot_payment = StringVar()	# Total amount he has to pay
		self.cl_payment_paid = StringVar()	# Amount he has paid already
		self.cl_last_payment_date = StringVar()# date client paid the last amount
		self.cl_payment_discount = StringVar() # Discount on the total Payment
		self.cl_training_type = StringVar()	# Gaining or loosing
		self.cl_training_method = StringVar()# is he taking a diet plan or workout plan or both
		self.cl_training_period = StringVar()# Client's total traning period



		#================labels and inputs===============

		#Personal Details
		self.id_lbl = Label(self.cl_prsl_dtl_frame, text ="Id",font=('Helvetica',12))	
		self.id_lbl.grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.id_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_id)	
		self.id_entry.grid(row=0,column=1, sticky='nsew', padx = 10, pady =10)

		self.name_lbl = Label(self.cl_prsl_dtl_frame, text ="Name",font=('Helvetica',12))	
		self.name_lbl.grid(row=1, column=0, sticky='nsew', padx = 10, pady = 10)

		self.name_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_name)	
		self.name_entry.grid(row=1,column=1, sticky='nsew', padx = 10, pady =10)

		self.ht_lbl = Label(self.cl_prsl_dtl_frame, text ="Height",font=('Helvetica',12))	
		self.ht_lbl.grid(row=2, column=0, sticky='nsew', padx = 10, pady = 10)

		self.ht_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_height)	
		self.ht_entry.grid(row=2,column=1, sticky='nsew', padx = 10, pady =10)

		self.wt_lbl = Label(self.cl_prsl_dtl_frame, text ="Weight",font=('Helvetica',12))	
		self.wt_lbl.grid(row=3, column=0, sticky='nsew', padx = 10, pady = 10)

		self.wt_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_weight)	
		self.wt_entry.grid(row=3,column=1, sticky='nsew', padx = 10, pady =10)

		self.dt_lbl = Label(self.cl_prsl_dtl_frame, text ="Client Date",font=('Helvetica',12))	
		self.dt_lbl.grid(row=4, column=0, sticky='nsew', padx = 10, pady = 10)

		self.dt_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_date)	
		self.dt_entry.grid(row=4,column=1, sticky='nsew', padx = 10, pady =10)

		self.phn_lbl = Label(self.cl_prsl_dtl_frame, text ="Phone",font=('Helvetica',12))	
		self.phn_lbl.grid(row=5, column=0, sticky='nsew', padx = 10, pady = 10)

		self.phn_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_phone)	
		self.phn_entry.grid(row=5,column=1,sticky='nsew',  padx = 10, pady =10)

		self.addr_lbl = Label(self.cl_prsl_dtl_frame, text ="Address",font=('Helvetica',12))	
		self.addr_lbl.grid(row=6, column=0, sticky='nsew', padx = 10, pady = 10)

		self.addr_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_addr)	
		self.addr_entry.grid(row=6,column=1, sticky='nsew', padx = 10, pady =10)

		self.city_lbl = Label(self.cl_prsl_dtl_frame, text ="City",font=('Helvetica',12))	
		self.city_lbl.grid(row=7, column=0, sticky='nsew', padx = 10, pady = 10)

		self.city_entry = Entry(self.cl_prsl_dtl_frame, textvariable = self.cl_city)	
		self.city_entry.grid(row=7,column=1, sticky='nsew', padx = 10, pady =10)


		# Payment Details
		self.totPmt_lbl = Label(self.cl_pmnt_dtl_frame, text ="Total Payment",font=('Helvetica',12))	
		self.totPmt_lbl.grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.totPmt_entry = Entry(self.cl_pmnt_dtl_frame, textvariable = self.cl_tot_payment)	
		self.totPmt_entry.grid(row=0,column=1, sticky='nsew', padx = 10, pady =10)

		self.pmtDiscount_lbl = Label(self.cl_pmnt_dtl_frame, text ="Discount",font=('Helvetica',12))	
		self.pmtDiscount_lbl.grid(row=1, column=0, sticky='nsew', padx = 10, pady = 10)

		self.pmtDiscount_entry = Entry(self.cl_pmnt_dtl_frame, textvariable = self.cl_payment_discount)	
		self.pmtDiscount_entry.grid(row=1,column=1, sticky='nsew', padx = 10, pady =10)
		
		self.pmtPaid_lbl = Label(self.cl_pmnt_dtl_frame, text ="Payment Paid",font=('Helvetica',12))	
		self.pmtPaid_lbl.grid(row=2, column=0, sticky='nsew', padx = 10, pady = 10)

		self.pmtPaid_entry = Entry(self.cl_pmnt_dtl_frame, textvariable = self.cl_payment_paid)	
		self.pmtPaid_entry.grid(row=2,column=1, sticky='nsew', padx = 10, pady =10)

		self.lastPmtDate_lbl = Label(self.cl_pmnt_dtl_frame, text ="Last Payment Date",font=('Helvetica',12))	
		self.lastPmtDate_lbl.grid(row=3, column=0, sticky='nsew', padx = 10, pady = 10)

		self.lastPmtDate_entry = Entry(self.cl_pmnt_dtl_frame, textvariable = self.cl_last_payment_date)	
		self.lastPmtDate_entry.grid(row=3,column=1, sticky='nsew', padx = 10, pady =10)


		# training details
		self.trngPeriod_lbl = Label(self.cl_trng_dtl_frame, text ="Training Period",font=('Helvetica',12))	
		self.trngPeriod_lbl.grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.trngPeriod_entry = Entry(self.cl_trng_dtl_frame, textvariable = self.cl_training_period)	
		self.trngPeriod_entry.grid(row=0,column=1, sticky='nsew', padx = 10, pady =10)

		self.trngType_lbl = Label(self.cl_trng_dtl_frame, text ="Training Type",font=('Helvetica',12))	
		self.trngType_lbl.grid(row=1,column=0, sticky='nsew', padx = 10, pady =10)

		self.trngType_entry = Entry(self.cl_trng_dtl_frame, textvariable = self.cl_training_type)	
		self.trngType_entry.grid(row=1,column=1, sticky='nsew', padx = 10, pady =10)
		
		self.trngMethod_lbl = Label(self.cl_trng_dtl_frame, text ="Training Method",font=('Helvetica',12))	
		self.trngMethod_lbl.grid(row=2,column=0, sticky='nsew', padx = 10, pady =10)

		self.trngMethod_entry = Entry(self.cl_trng_dtl_frame, textvariable = self.cl_training_method)	
		self.trngMethod_entry.grid(row=2,column=1, sticky='nsew', padx = 10, pady =10)

		
		# Button Widgets
		self.btnAddData=Button(self.cl_btn_frame,text ="Create", font=('arial',11,'bold'), height=1, width=16, bd=2, command = lambda:self.create_client(self.get_variables()))
		self.btnAddData.grid(row=0,column=0, padx=3, pady=0.5, sticky='nsew')

		self.btnViewUpdate = Button(self.cl_btn_frame,text ="View Update", font=('arial',11,'bold'), height=1, width=16, bd=2, command = self.check_update)
		self.btnViewUpdate.grid(row=0,column=1, padx=3, pady=0.5, sticky='nsew')

		self.btnClearAll=Button(self.cl_btn_frame,text ="Clear All", font=('arial',11,'bold'), height=1, width=16, bd=2, command = self.clear_all)
		self.btnClearAll.grid(row=0,column=2, padx=3, pady=0.5, sticky='nsew')

		self.btnUpdate=Button(self.cl_btn_frame,text ="Back", font=('arial',11,'bold'), height=1, width=16, bd=2, command = lambda:controller.show_frame(StartPage))
		self.btnUpdate.grid(row=0, column=3, padx=3, pady=0.5, sticky='nsew')

		

	# Associated function
	#all variables
	def get_variables(self):
		cl_details = {
					'cl_id':self.cl_id.get(),
					'cl_name':self.cl_name.get(),
					'cl_height':self.cl_height.get(),		
					'cl_weight':self.cl_weight.get(),		
					'cl_date':self.cl_date.get(),		
					'cl_addr':self.cl_addr.get(),			
					'cl_phone':self.cl_phone.get(),			
					'cl_city':self.cl_city.get(),			
					'cl_tot_payment':self.cl_tot_payment.get(),	
					'cl_payment_paid':self.cl_payment_paid.get(),
					'cl_last_payment_date':self.cl_last_payment_date.get(),
					'cl_payment_discount':self.cl_payment_discount.get(), 
					'cl_training_type':self.cl_training_type.get(),
					'cl_training_method':self.cl_training_method.get(),
					'cl_training_period':self.cl_training_period.get(),

		}
		return cl_details
		

	def clear_all(self):
		self.id_entry.delete(0,END)
		self.name_entry.delete(0,END)
		self.ht_entry.delete(0,END)		
		self.wt_entry.delete(0,END)		
		self.dt_entry.delete(0,END)		
		self.addr_entry.delete(0,END)			
		self.phn_entry.delete(0,END)			
		self.city_entry.delete(0,END)			
		self.totPmt_entry.delete(0,END)	
		self.pmtPaid_entry.delete(0,END)
		self.lastPmtDate_entry.delete(0,END)
		self.pmtDiscount_entry.delete(0,END) 
		self.trngType_entry.delete(0,END)
		self.trngMethod_entry.delete(0,END)
		self.trngPeriod_entry.delete(0,END)

	#creating a newclient
	def create_client(self,client_details):
		cl = Client(client_details['cl_id'],
					client_details['cl_name'],
					client_details['cl_height'],
					client_details['cl_weight'],
					client_details['cl_date'],
					client_details['cl_phone'],
					client_details['cl_addr'],
					client_details['cl_city'],
					client_details['cl_tot_payment'],
					client_details['cl_payment_paid'],
					client_details['cl_last_payment_date'],
					client_details['cl_payment_discount'],
					client_details['cl_training_type'],
					client_details['cl_training_method'],
					client_details['cl_training_period'])
			
		try:
			if client_details['cl_id']=='' or client_details['cl_name']=='':
				messagebox.showerror('Invalid', 'Kindly provide an Id and Name to create a new client..!')
				pass
			else:
				insert_client(cl)
				new_cl_name =get_client_by_id(client_details['cl_id'])[1]
				messagebox.showinfo('New Client', f'{new_cl_name} Added Successfully')	
				self.clear_all()
			
		except:
			messagebox.showinfo('Invalid Input',"Check all the values if anything is ") 

# does not clear the data AFTER DONE
	def set_text(self):
		# clearing the previous data 
		self.clear_all()
		# feeding the active client data into the the entry boxes
		try:
			self.activeClientDetails = create_client_object_by_id(activeClientId)
			self.id_entry.insert(0,self.activeClientDetails.c_id)
			self.name_entry.insert(0,self.activeClientDetails.c_name)
			self.ht_entry.insert(0,self.activeClientDetails.c_height)
			self.wt_entry.insert(0,self.activeClientDetails.c_weight)
			self.dt_entry.insert(0,self.activeClientDetails.c_date)
			self.phn_entry.insert(0,self.activeClientDetails.c_phone)
			self.addr_entry.insert(0,self.activeClientDetails.c_addr)
			self.city_entry.insert(0,self.activeClientDetails.c_city)
			self.totPmt_entry.insert(0,self.activeClientDetails.c_tot_payment)
			self.pmtDiscount_entry.insert(0,self.activeClientDetails.c_payment_discount)
			self.pmtPaid_entry.insert(0,self.activeClientDetails.c_payment_paid)
			self.lastPmtDate_entry.insert(0,self.activeClientDetails.c_last_payment_date)
			self.trngMethod_entry.insert(0,self.activeClientDetails.c_training_method)
			self.trngType_entry.insert(0,self.activeClientDetails.c_training_type)
			self.trngPeriod_entry.insert(0,self.activeClientDetails.c_training_period)
			
		except:
			print("Data cannot be fed")

		else:
			update_active=False


	def check_update(self):
		self.activeClientDetails
		# getting the original data from the database
		self.org_client_dict = {'c_id':self.activeClientDetails.c_id,
								'c_name':self.activeClientDetails.c_name,
								'c_height':self.activeClientDetails.c_height,
								'c_weight':self.activeClientDetails.c_weight,
								'c_date':self.activeClientDetails.c_date,
								'c_phone':self.activeClientDetails.c_phone,
								'c_addr':self.activeClientDetails.c_addr,
								'c_city': self.activeClientDetails.c_city,
								'c_tot_payment': self.activeClientDetails.c_tot_payment,
								'c_payment_discount': self.activeClientDetails.c_payment_discount,
								'c_payment_paid': self.activeClientDetails.c_payment_paid,
								'c_last_payment_date': self.activeClientDetails.c_last_payment_date,
								'c_training_method': self.activeClientDetails.c_training_method,
								'c_training_type': self.activeClientDetails.c_training_type,
								'c_training_period': self.activeClientDetails.c_training_period}
		print(self.org_client_dict.values())

		self.updated_client_dict = self.get_variables()
		print(self.updated_client_dict.values())


# class AddMealpage


app = Root()
app.mainloop()

































































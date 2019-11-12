import sqlite3
import tkinter


conn = sqlite3.connect("client_diet_plans.db")
c = conn.cursor()




# CREATE TABLES #

def create_client_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS client(
					c_id TEXT NOT NULL PRIMARY KEY,
					c_name TEXT NOT NULL,
					c_height REAL,
					c_weight REAL,
					c_payment REAL,
					c_location REAL)
				""")

def create_meal_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS meal(
					m_id TEXT NOT NULL PRIMARY KEY,
					m_name TEXT NOT NULL,
					m_type TEXT,
					client_fk TEXT REFERENCES client(c_id))
				""")

def create_food_table():
	with conn:
		c.execute("""CREATE TABLE IF NOT EXISTS food(
				f_id TEXT NOT NULL PRIMARY KEY,
				f_name TEXT NOT NULL,
				f_prot REAL,
				f_carbs REAL,
				f_fat REAL,
				f_qty TEXT,
				meal_fk TEXT REFERENCES meal(m_id))
		""")




# INSERT INTO TABLES #

def insert_client(cl):
	with conn:
		c.execute( "INSERT INTO client VALUES (:c_id, :c_name, :c_height, :c_weight,:c_payment, :c_location)",
			{'c_id':cl.id, 'c_name':cl.name, 'c_height':cl.height, 'c_weight':cl.weight, 'c_payment':cl.payment, 'c_location': cl.location })

def insert_meal(m):
	with conn:
		c.execute( "INSERT INTO meal VALUES (:m_id, :m_name, :m_type, :client_fk)",
			{'m_id':m.id, 'm_name':m.name, 'm_type':m.type, 'client_fk':m.client})

def insert_food(f):
	with conn:
		c.execute( "INSERT INTO food VALUES (:f_id, :f_name, :f_prot, :f_carbs, :f_fat, :f_qty, :meal_fk)",
			{'f_id':f.id, 'f_name':f.name, 'f_prot':f.prot, 'f_carbs':f.carbs, 'f_fat':f.fat, 'f_qty': f.qty, 'meal_fk':f.meal })




# QUERRY TABLES #

def get_client_by_id(client_id):
	with conn:
		c.execute("SELECT * FROM client WHERE c_id = :client_id", {'client_id':client_id})

def get_client_by_id(meal_id):
	with conn:
		c.execute("SELECT * FROM meal WHERE m_id = :meal_id", {'meal_id':meal_id})

def get_client_by_id(food_id):
	with conn:
		c.execute("SELECT * FROM client WHERE f_id = :food_id", {'client_id':food_id})




# UPDATE TABLES #

def update_client_by_id(client_id,upd_fld,upd_val):
	with conn:
		c.execute("UPDATE client SET :upd_fld = :upd_val WHERE c_id = :client_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'client_id':client_id})

def update_meal_by_id(meal_id,upd_fld,upd_val):
	with conn:
		c.execute("UPDATE meal SET :upd_fld = :upd_val WHERE m_id = :meal_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'meal_id':meal_id})

def update_food_by_id(food_id,upd_fld,upd_val):
	with conn:
		c.execute("UPDATE food SET :upd_fld = :upd_val WHERE f_id = :food_id", {'upd_fld':upd_fld, 'upd_val':upd_val, 'food_id':food_id})




# DELETE ENTRY #

def delete_client_by_id(client_id):
	with conn:
		c.execute("DELETE FROM client WHERE c_id = :client_id", {'client_id':client_id})

def delete_meal_by_id(meal_id):
	with conn:
		c.execute("DELETE FROM meal WHERE c_id = :meal_id", {'meal_id':meal_id})

def delete_client_by_id(client_id):
	with conn:
		c.execute("DELETE FROM food WHERE f_id = :food_id", {'food_id':food_id})






#Tables are alredy created just entering data 

# create_client_table()
# create_meal_table()
# create_food_table()

print("Created has been Database..!")



class Client:
	def __init__(self,id,name,height,weight,payment,location):
		self.id = id
		self.name = name
		self.height = height
		self.weight = weight
		self.payment = payment
		self.location = location

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



# Client insertion function #

def cl_db_entry():
	id = input("Enter clients's id: ")
	name = input("Enter clients's name: ")
	height = input("Enter clients's height: ")
	weight = input("Enter clients's weight: ")
	payment = input("Enter clients's payment: ")
	location = input("Enter clients's location: ")
	
	cl = Client(id, name, height, weight, payment, location)
	
	insert_client(cl)
	
	print(f"Data for {cl.name} has been entered ito the Database..!")




# meal entry function #

def ml_db_entry():
	id = input("Enter Meal id: ")
	name = input("Enter Meal name: ")
	type = input("Enter Meal Type: ")
	client = input("Enter Client Id for the meal: ")
	
	ml = Meal(id, name, type, client)
	
	insert_meal(ml)
	
	print(f"Data for {ml.name} has been entered ito the Database..!")





# Food insertion function #

def fd_db_entry():
	id = input("Enter food's id: ")
	name = input("Enter food's name: ")
	prot = input("Enter protein in food: ")
	carbs = input("Enter carbs in food: ")
	fat = input("Enter fat in food: ")
	qty = input("Enter qty of food required: ")
	meal = input("Enter the meal id for the food: ")
	
	fd = Food(id, name, prot, carbs, fat, qty, meal)
	
	insert_food(fd)
	
	print(f"Data for {fd.name} has been entered ito the Database..!")


while True:
	opt = input("Choose from client,food,meal or stop: ")
	
	if opt.lower() == "client":
		cl_db_entry()
	elif opt.lower() == "meal":
		ml_db_entry()
	elif opt.lower() == "food":
		fd_db_entry()
	elif opt.lower() == "stop":
		break
	else:
		continue

























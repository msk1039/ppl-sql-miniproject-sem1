
import mysql.connector as cn

cxt = cn.connect(
	host = "localhost",
	user = "root",
	passwd = "@Mysql@2005",
	database = "python_crud_app"
)

while(True):
	crs = cxt.cursor()

	print("ENTER CHOICE TO MAKE CHANGES")
	print("1. Enter to add user")
	print("2. Enter update user")
	print("3. Enter delete user")
	print("4. Enter search user")
	print("5. display all users")

	x = int(input("Enter Choice: "))

	if x == 1:
		name = input("Enter Name of User: ")
		email = input("Enter user Email: ")
		try:
			ins_q = "INSERT INTO users(username, email) VALUES(%s, %s)"
			val = (name, email)
			crs.execute(ins_q, val)
			cxt.commit()
			print("User data has been saved")
			last_user = crs.execute("select *from users order by iser_id DESC LIMIT 1;")
			print
		except cn.Error as error:
			print(error)
		finally:
			crs.close()


	elif x == 2:
		uid = input("Enter User Id to Update: ")
		try:
			find_user = "SELECT * FROM users WHERE iser_id = %s"
			user_id = (uid,)
			crs.execute(find_user, user_id)
			for (iser_id, username, email) in crs:
				print("You are about to update: {} {} {}".format(iser_id, username, email))
			name = input("Enter New Name: ")
			email = input("Enter New Email: ")
			try:
				update_user = "UPDATE users SET username = %s, email = %s WHERE iser_id = %s"
				update_values = (name, email, uid)
				crs.execute(update_user, update_values)
				cxt.commit()
				print("User has been updated")
			except cn.Error as error:
				print(error)
		except cn.Error as errors:
			print(errors)
		finally:
			crs.close()


	elif x == 3:
		uid = input("Enter user ID to delete: ")
		try:
			delete_sql = "DELETE FROM users WHERE iser_id = %s"
			delete_uid = (uid,)
			crs.execute(delete_sql, delete_uid)
			cxt.commit()
			print("User with ID ", uid, " has been deleted")
		except cn.Error as error:
			print(error)
		finally:
			crs.close()

	elif x == 4:
		uid = input("Enter the user ID to search: ")
		try:
			find_user = "SELECT * FROM users WHERE iser_id = %s"
			user_id = (uid,)
			crs.execute(find_user, user_id)
			for (iser_id, username, email) in crs:
				print("User ID: {} ".format(iser_id))
				print("User ID: {} ".format(username))
				print("User ID: {} ".format(email))
		except cn.Error as error:
			print(error)
		finally:
			crs.close()
	elif x == 5:
		try:
			crs.execute("SELECT * FROM users")
			result = crs.fetchall()
			for row in result:
				print(row)
		except cn.Error as error:
			print(error)
		finally:
			crs.close()

	else:
		print("invalid input")
	loop=input("do you want to continue? [y/n]: ")
	if loop== 'y':
		continue
	else:
		break;


cxt.close()



# Previous Process
# 1. Database creation
# 2. Table Creation

################# DATABASE CREATION ################
'''
try:
	crs.execute("create database python_crud_app")
	print("Database Created")
except cn.Error as er:
	print(er)

########### SHOW DATABASES ###############
 for x in crs:
	print(x)


############### CREATE TABLE ###################

try:
	sql = "CREATE TABLE users(iser_id int AUTO_INCREMENT PRIMARY KEY, username varchar(255), email varchar(255))"
	crs.execute(sql)
	print("table has been created")
except cn.Error as er:
	print(er)


#################### SHOW TABLES ###############

try:
	sql = "SHOW TABLES"
	crs.execute(sql)

	for tables in crs:
		print(tables)
except cn.Error as er:
	print(er)
finally:
	crs.close()
	cxt.close()

'''



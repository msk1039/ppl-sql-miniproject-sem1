# ppl-sql-miniproject-sem1



# Previous Process
# 1. Database creation
# 2. Table Creation

################# DATABASE CREATION ################
try:
	crs.execute("create database python_crud_app")
	print("Database Created")
except cn.Error as er:
	print(er)

########### SHOW DATABASES ###############
 for x in crs:
	print(x)


############### TABLE CREATION ###################

try:
	sql = "CREATE TABLE users(iser_id int AUTO_INCREMENT PRIMARY KEY, username varchar(255), email varchar(255))"
	crs.execute(sql)
	print("table has been created")
except cn.Error as er:
	print(er)





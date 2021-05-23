import mysql.connector
import csv
import re
import json

def create_database():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "")

	mycursor = WHRdb.cursor()
	#Create Database World Happiness Report
	mycursor.execute("CREATE DATABASE World_Happiness_Report")


def create_tables(Year):
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")
	#Enter the year of the report
	year = str(Year)
	#Open the report and read headers
	with open("Data_Files/["+"'"+year+"'"+"].csv") as csv_file:
		csvfile = csv.reader(csv_file, delimiter=',')
		headers = next(csvfile)
		#print(headers)

	#Remove all Special Characters in header
	Mheaders = []
	for name in headers:
		#Capitalize each word
		name = name.title()		
		name = re.sub('[^A-Za-z0-9]+', '', name)		
		Mheaders.append(name)

	#print(Mheaders)
	#Set initial header file name
	headers = Mheaders
	#print(headers)
	
	#Drop table if exists
	query = "DROP TABLE IF EXISTS `" + year + "`"
	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.execute(query)

	#Write the query to create table
	#First column is Country br default	
	query = "CREATE TABLE " + "`" + year + "`" + " (" + headers[0] + " VARCHAR(255)"
	#add csv headers
	for var in range(1,len(headers)):
		query += ", "		
		query = query + headers[var] +" FLOAT(10)"
	
	query = query + ")"

	
	print(query)
	#Wxecute query
	mycursor.execute(query)


def create_json_table():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")


	file = open("countries_continents_codes_flags_url.json", "r")
	country= file.read()
	file.close()

	country_info = json.loads(country)
	
	#print(country_info[0])

	#Extract the keys of the json file
	json_file_keys =[]
	for key,data in country_info[0].items():
		key = key.title()		
		key = re.sub('[^A-Za-z0-9]+', '', key)		
		#append the keys to the headers list
		json_file_keys.append(key)

	#print(json_file_keys)
	
	#Drop table if exists
	query = "DROP TABLE IF EXISTS `Country_info`"
	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.execute(query)

	query = "CREATE TABLE `Country_info` (" + json_file_keys[0] +" VARCHAR(255)"
	
	for key in range(1,len(json_file_keys)):
		query += ", "	
		query += json_file_keys[key] +" VARCHAR(255)"

	query = query + ")"

	print(query)
	#Wxecute query
	mycursor.execute(query)
	WHRdb.close()


def list_database():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "")

	mycursor = WHRdb.cursor()
	
	#To check if database created successfully
	
	mycursor.execute("SHOW DATABASES")
	for db in mycursor:
		print(db)
	

def list_tables():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "",
		database = "WorldHappinessReport")

	mycursor = WHRdb.cursor()
	
	#To check if database created successfully
	
	mycursor.execute("SHOW TABLES")
	for tb in mycursor:
		print(tb)

if __name__ == "__main__":
	
	#Create the database
	create_database()
	#Create tables for each report
	for year in range(2016,2020):
		create_tables(year)
	
	create_json_table()
	
	#Show current 
	#list_database()
	#list_tables()
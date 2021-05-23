import mysql.connector
import csv
import requests
from xml.etree import ElementTree as ET


def add_fields():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	query = "ALTER TABLE country_info ADD CapitalCity varchar(255), ADD Longitude FLOAT(10), ADD Latitude FLOAT(10)"
	print(query)

	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.execute(query)

def read_api_complement():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	
	#Read API data
	result = requests.get('http://api.worldbank.org/v2/country?format=json')
	#Convert the data to json format
	data = result.json()

	#print(data[1][0]['capitalCity'])
	list = data[1]
	#print(len(list))
	#Execute the query
	#mycursor = WHRdb.cursor()

	query = "SELECT Country from country_info"

	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.execute(query)
	result = mycursor.fetchall()

	CountryList = []
	for c in range(len(result)):
		CountryList.append(result[c][0])
	
	#print(CountryList)

	for i in range(len(list)):
		country_name = list[i].get("name")

		if(country_name in CountryList):
			capitalCity = list[i].get("capitalCity")
			longitude = list[i].get("longitude")
			latitude = list[i].get("latitude")

			query = "UPDATE country_info SET CapitalCity = %s, Longitude = %s, Latitude =%s WHERE Country = '" + country_name +"'"
			#print(query)
			mycursor.execute(query, (capitalCity,longitude,latitude))
		
	WHRdb.commit()
	WHRdb.close()	



if __name__ == "__main__":

	add_fields()
	read_api_complement()
import mysql.connector
import csv
import re
import json

def log_csv_data(Year):
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	year = str(Year)
	#Open the report and read data
	with open("Data_Files/["+"'"+year+"'"+"].csv") as csv_file:
		csvfile = csv.reader(csv_file, delimiter=',')
		headers = next(csvfile)
		#Remove all Special Characters in header
		Mheaders = []
		for name in headers:
			#Capitalize each word
			name = name.title()		
			name = re.sub('[^A-Za-z0-9]+', '', name)		
			Mheaders.append(name)
		#Set initial header file name
		headers = Mheaders
		#print(headers)


		#Create the list of data
		csvdata =[]
		for row in csvfile:
			csvdata.append(row)			
			
	#print(csvdata)

	query = "INSERT INTO " + "`" + year + "` "+ "(`" + headers[0]
	#ADD LOOP FOR CSV HEADERS
	for h in range(1,len(headers)):
		query +="`,`"
		query += headers[h]
	
	query += "`)" +" VALUES (%s" 

	for i in range(1,len(headers)):
		query += ", %s"
	query += ")"
	print(query)	
	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.executemany(query, csvdata)
	WHRdb.commit()
	WHRdb.close()



def log_json_data():
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	#WORK WITH JSON FILE
	file = open("countries_continents_codes_flags_url.json", "r")
	country= file.read()
	file.close()
	
	country_info = json.loads(country) #Creates list of dictionaries

	#Extract the keys of the json file
	json_file_keys =[]
	for key,data in country_info[0].items():
		key = key.title()		
		key = re.sub('[^A-Za-z0-9]+', '', key)		
		#append the keys to the headers list
		json_file_keys.append(key)

	#Write the query
	query = "INSERT INTO `country_info`  (`" + json_file_keys[0]
	for key in range(1,len(json_file_keys)):
		query +="`,`"
		query += json_file_keys[key]
	
	query += "`)" +" VALUES (%s" 

	for i in range(1,len(json_file_keys)):
		query += ", %s"
	query += ")"
	
	print(query)
	
	#Execute the query
	mycursor = WHRdb.cursor()

	for item in country_info:
		Country = item.get("country")
		ImagesFile= item.get("images_file")
		ImageUrl = item.get("image_url")
		Alpha2 = item.get("alpha-2")
		Alpha3 = item.get("alpha-3")
		CountryCode = item.get("country-code")
		Iso31662 = item.get("iso_3166-2")
		Region = item.get("region")
		SubRegion = item.get("sub-region")
		IntermediateRegion = item.get("intermediate-region")
		RegionCode = item.get("region-code")
		SubRegionCode = item.get("sub-region-code")
		IntermediateRegionCode = item.get("intermediate-region-code")
		#Execute command
		mycursor.execute(query, (Country,ImagesFile,ImageUrl,Alpha2,Alpha3,CountryCode,Iso31662,Region,SubRegion,IntermediateRegion,RegionCode,SubRegionCode,IntermediateRegionCode))
	WHRdb.commit()
	WHRdb.close()


if __name__ == "__main__":
	for year in range(2016,2020):
		log_csv_data(year)
	log_json_data()
import mysql.connector
import csv
import pandas as pd

def log_to_csv(Year,Country):
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	year = str(Year)
	country = Country
	
	#Find regionCode and ImageUrl
	query="SELECT ImageUrl,RegionCode,Region  FROM `country_info` WHERE Country='" +country +"'"
	#Execute the query
	mycursor = WHRdb.cursor()
	mycursor.execute(query)
	nextresult = mycursor.fetchall()
	#Assign values
	ImageUrl = nextresult[0][0]
	RegionCode = nextresult[0][1]
	Region = nextresult[0][2]
	Region = Region.upper()


	#Complement Rank in data pipeline
	if (year == "2016" or year == "2017"):
		#Find Overall Rank
		query = "SELECT Country,ROW_NUMBER() OVER(ORDER BY HappinessScore desc) FROM `" + year + "`"
		# WHERE Country='" +country +"'"
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		rank = mycursor.fetchall()
		for rank in rank:
			if(rank[0]==country):
				OverallRank= rank[1]
		#print(OverallRank)
	
		#Find Region Rank
		query = "SELECT `"+year+"`.HappinessScore, country_info.RegionCode,country_info.Country, ROW_NUMBER() OVER(ORDER BY HappinessScore desc) FROM `" + year + "` INNER JOIN `country_info` ON `" + year + "`.Country =country_info.Country WHERE RegionCode="+ RegionCode
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		rank = mycursor.fetchall()
		for rank in rank:
			if(rank[2]==country):
				RegionRank= rank[3]
		#print(RegionRank)

	if (year == "2018" or year == "2019"):
		#Find Overall Rank
		query = "SELECT CountryOrRegion,ROW_NUMBER() OVER(ORDER BY Score desc) FROM `" + year + "`"
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		rank = mycursor.fetchall()
		for rank in rank:
			if(rank[0]==country):
				OverallRank= rank[1]
		#print(OverallRank)
	
		#Find Region Rank
		query = "SELECT `"+year+"`.Score, country_info.RegionCode,country_info.Country, ROW_NUMBER() OVER(ORDER BY Score desc) FROM `" + year + "` INNER JOIN `country_info` ON `" + year + "`.CountryOrRegion =country_info.Country WHERE RegionCode="+ RegionCode
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		rank = mycursor.fetchall()
		for rank in rank:
			if(rank[2]==country):
				RegionRank= rank[3]
		#print(RegionRank)

	#FIND ALL PARAMETERS
	if (year == "2016" or year == "2017"):

		query="SELECT Country,HappinessScore,Family,HealthLifeExpectancy,Freedom,Generosity,TrustGovernmentCorruption,EconomyGdpPerCapita FROM `" + year+ "`"
		query+="WHERE Country='" +country +"'"

		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		result = mycursor.fetchall()
		#Assign values
		Country = result[0][0]
		HappinessScore = result[0][1]
		Family = result[0][0][2]
		HealthLifeExpectancy = result[0][3]
		Freedom = result[0][4]
		Generosity = result[0][5]
		TrustGovernmentCorruption = result[0][6]		
		SocialSupport = ""
		GDPperCapita = result[0][7] 
		#print(result[0])


	if (year == "2018" or year == "2019"):

		query="SELECT CountryOrRegion,Score,HealthyLifeExpectancy,FreedomToMakeLifeChoices,Generosity,PerceptionsOfCorruption,SocialSupport,GdpPerCapita FROM `" + year+ "`"
		query+="WHERE CountryOrRegion='" +country +"'"

		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		result = mycursor.fetchall()
		#Assign values
		Country = result[0][0]
		HappinessScore = result[0][1]
		Family = ""
		HealthLifeExpectancy = result[0][2]
		Freedom = result[0][3]
		Generosity = result[0][4]
		TrustGovernmentCorruption = result[0][5]
		SocialSupport = result[0][6]
		GDPperCapita = result[0][7]
		#print(result[0])

	#Set Happiness Status
	if(HappinessScore >5.6):
		HappinessStatus = 'Green'
	elif(HappinessScore >=2.6 and HappinessScore <=5.6 ):
		HappinessStatus = "Amber"
	elif(HappinessStatus <2.6):
		HappinessStatus = "Red"

	with open('Generated/record_model.csv', 'w', newline='') as newcsv:

		file = csv.writer(newcsv)
		file.writerow(['Column Name', 'Specifications'])
		file.writerow(['Year', year])
		file.writerow(['Country', country])
		file.writerow(['Country Url', ImageUrl])
		file.writerow(['Region Code', RegionCode])
		file.writerow(['Region', Region])
		file.writerow(['Rank Per Region', RegionRank])
		file.writerow(['Overall Rank', OverallRank])
		file.writerow(['Happiness Score', HappinessScore])
		file.writerow(['Happiness Status', HappinessStatus])
		file.writerow(['GDP per Capita', GDPperCapita])
		file.writerow(['Family', Family])
		file.writerow(['Social support', SocialSupport])
		file.writerow(['Health life expectancy', HealthLifeExpectancy])
		file.writerow(['Freedom to make life choices', Freedom])
		file.writerow(['Generosity', Generosity])
		file.writerow(['Perceptions of corruption', TrustGovernmentCorruption])


	#Convert csv to parquet
	log_to_parquet()


def log_to_parquet():
	#Convert to paruet with pandas,pyarrow library
	file = pd.read_csv('Generated/record_model.csv')
	file.to_parquet('Generated/parquet_record_model.parquet')
	print(file)


if __name__ == "__main__":
	log_to_csv(2018, "Norway")

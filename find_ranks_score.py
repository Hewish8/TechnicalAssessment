import mysql.connector
import csv
import json

def find_ranks_score(Country):
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	country = Country


	#HIGHEST AND LOWEST RANK
	LowestRank = 0
	HighestRank = 273 #Highest number of countries is 273
	LowestScore = 10 #Assumming score range is 0 -10
	HighestScore =0 
	year = ["2016","2017"]	
	for year in year:
		query = "SELECT Country,HappinessScore, ROW_NUMBER() OVER(ORDER BY HappinessScore desc) FROM `" + year + "`"
		#print(query)	

		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		score = mycursor.fetchall()
		#print(score)
		for score in score:
			if(score[0]==country):
				Rank= score[2]
				Score= score[1]
		#print(Score)

		if(Score<LowestScore):
			LowestScore =Score
		if(Score>HighestScore):
			HighestScore=Score

		
		if(Rank > LowestRank ):
			LowestRank= Rank
		if(Rank < HighestRank):
			HighestRank =Rank

	
	
	year = ["2018","2019"]
	for year in year:
		query = "SELECT CountryOrRegion,Score, ROW_NUMBER() OVER(ORDER BY Score desc) FROM `" + year + "`"
		#print(query)	

		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		score = mycursor.fetchall()
		for score in score:
			if(score[0]==country):
				Rank= score[2]
				Score= score[1]
		#print(Rank)

		if(Score<LowestScore):
			LowestScore =Score
		if(Score>HighestScore):
			HighestScore=Score
		
		if(Rank > LowestRank ):
			LowestRank= Rank
		if(Rank < HighestRank):
			HighestRank =Rank

	#print(LowestRank)
	#print(HighestRank)
	LowestHappinessScore = LowestScore
	#print(LowestHappinessScore)	
	HighestHappinessScore = HighestScore
	#print(HighestHappinessScore)

	
	data = []

	data.append({
		'Country': country,
		'Lowest_Rank': LowestRank,
		'Highest_Rank': HighestRank,
		'Lowest_Happiness_Score': LowestHappinessScore,
		'Highest_Happiness_Score': HighestHappinessScore})
	print(data)

	write_json(data,country)


def write_json(data, Country):
	filename = "Generated/consume_" + Country + ".json"
	with open(filename, "w") as f:
		json.dump(data, f, indent = 2)



if __name__ == "__main__":
	find_ranks_score("Germany")

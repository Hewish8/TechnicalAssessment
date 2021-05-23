import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import mysql.connector
from random import seed
from random import random

def plot_map(Year):	
	#Connect to MySQL
	WHRdb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "",
		database = "World_Happiness_Report")

	
	year = str(Year)
	#Get the countries and Scores DATASET
	if(year == "2016" or year =="2017"):
		query = "SELECT Country, HappinessScore FROM `" + year + "`"
		#print(query)
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)
		dataset = mycursor.fetchall()

	if(year == "2018" or year =="2019"):
		query = "SELECT CountryOrRegion, Score FROM `" + year + "`"
		#print(query)
		#Execute the query
		mycursor = WHRdb.cursor()
		mycursor.execute(query)		
		dataset = mycursor.fetchall()



	#Creating lists of the following
	Country = []
	HappinessScore = []
	HappinessStatus = []
	
	count = 0
	for r in dataset:
		Country.append(r[0]) # r[0] is score
		HappinessScore.append(r[1]) #r[1] is score
		#Set Happiness Status
		if(r[1]>5.6):
			Status = 'Green'
		elif(r[1]>=2.6 and r[1] <=5.6 ):
			Status = "Amber"
		elif(r[1] <2.6):
			Status = "Red"
		HappinessStatus.append(Status)

	#print(len(Country))
	#print(len(HappinessScore))
	#print(len(HappinessStatus))
	
	#Generate randon values for z
	# seed random number generator
	seed(1)
	z=[]
	# generate random numbers between 0-1
	for _ in range(len(Country)):
		value = random()
		z.append(value)

	#print(len(z))


	data = dict(type = 'choropleth',
				locations = Country,
				locationmode = 'country names',
				colorscale = 'Jet',
				text = HappinessStatus ,
				z = HappinessScore,
				colorbar = {'title': 'Score Colorbar'})
	title = 'World Happiness Score ' + year

	layout = dict(title= title,
					geo={'scope': 'world'})

	choromap = go.Figure(data = [data], layout = layout)
	choromap.show()

	

if __name__ == "__main__":
	for year in range(2016,2020):
		plot_map(year)



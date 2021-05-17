# TechnicalAssessment
## MCB Software Engineer Data Practical Test

### 1. First Create a Main Folder and Add all the codes above.
### 2. Inside the main folder
  -i) Create a folder 'Data_Files' and add all the csv reports.
  -ii)Create a folder 'Generated' to output all the generated files
### 3. Run the file Rename_files.py: 
  -The csv reports do not have standard names. This code will rename all of them as the year of the report by extracting the year from the name.
### 4. Question 1:-Run the file create_database.py 
  - This will create the MySQL database World_Happiness_report. 
  - It will also create tables with headers similar to the ones in the csv reports, taking into account change in report headers' names after year 2017
  - It will also create a table with headers as the keys of the json file provided
### 5. Question 2:- Run the file automated_data_pipeline.py:
  - This will extract all records from the csv files and load them to appropriate tables
  - The Json data will also be loaded in the table country_info.
### 6. Question 3: Before running the file modelling_record.py:
  - Assuming the data scientist wants to generate the modelling record for a particular Country and year; go to line 163 in the script and change the year and Country name in the function log_to_csv(Year, "Country Name") to desired one. The default here is log_to_csv(2018, "Norway")
  - Run the file modelling_record.py
  - The files record_model.csv and parquet_record_model.parquet will be generated for the chosen country and year.
### 7.Question 4: Before running the file find_ranks_score.py
  - Assuming the data scientist wants to generate the JSOn file for a particular Country; Go to line 104 in the script and change the Country name in the function find_ranks_score("Country Name") to the desired one. The default here is find_ranks_score("Germany").
  - Run the file find_ranks_score.py
  - The required extract will be generated in JSON format and saved in the folder Generated as consume_CountryName.json
### 8.Question 5:Run the file Dashboard.py
  -Four Dashboards will be generated for each year 2016 to 2019 each showing a World Map. When the cursor is hovered over a country, the Happiness Score, Happiness Status and Country Name is displayed. A Score color bar is also included.
  
### 9. Question 6: Run the file consume_api.py
  - Firstly, the columns CapitalCity, Latitude and Longitude will be added to the the table country_info in the database
  - Then the api will be read, required data extracted and logged to the table country_info.
 

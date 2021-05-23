import pathlib
import re

def rename_files():
	#find the folder with reports
	file_path = pathlib.Path('.')/"Data_Files"
	for file in file_path.iterdir():
		#Extract only the year from report name		
		year =re.findall('\d+',str(file))
		#re add csv extension
		year = str(year)+ ".csv"
		#rename the report as the year
		file.rename(file_path/year)
		print(file)
		

if __name__ == "__main__":
	rename_files()
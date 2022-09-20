# kvanme01_proj1
In the spirit of the WNBA 2022 Finals, this project aims to explore the Kaggle dataset "WNBA Draft Basketball Player Data (1997 - 2022)" using exploratory data analysis and use a Click CLI to build a starting lineup of WNBA players. 

[![Python application test with Github Actions](https://github.com/nogibjj/wnba-team-generator/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/wnba-team-generator/actions/workflows/main.yml)


<img width="814" alt="Screen Shot 2022-09-20 at 1 23 22 AM" src="https://user-images.githubusercontent.com/112578194/191174153-9b238f85-1c85-4515-8db8-d906743eaf0e.png">


Exploratory data analysis was first conducted in Jupyter Notebooks using the Kaggle API. Python packages pandas and seaborn were utilized to analyze the dataset in the form of dataframes and tables. The dataset was then tranfered from a kvanme01 repository to the codespace-enabled nogibjj/kvanme01 repository via .csv file. 

team_maker.py contains a simple CLI using click that takes in User's requested team name and generates a random list of 5 wnba players from the database to constitute a "starting lineup". 

I plan to continue adding to this command line tool to allow the user to add to their roster based on the players stats, years they played, college/ professional team etc. (all data from the Kaggle dataset). 

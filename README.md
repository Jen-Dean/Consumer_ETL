# for-now
> Sandwich Scraping Experts

## Table of contents

* [Project Proposal](#project-proposal)
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## Project Proposal

#### Brief Description of the Final Database : 
##### Fast Food nutrition. Accumulate fast food sandwich nutritional facts.

### Sandwich Fast Food Restaurants:
* Jimmy Johns - 32 sandwiches
* Panera - 22 sandwiches
* Subway - 38 sandwiches
* Quiznos - 24 sandwiches
* Blimpie - 35 sandwiches

#### Why is our final database useful to a hypothetical organization?
* To create a repository for people interested in nutrition and making positive food choices
* For a potential sandwich shop to get competitor data to create a better shop.
* We will also list out how much exercise it takes to burn the sandwiches off

#### A list of data sources :
*  [Food Nutrition.org](https://fastfoodnutrition.org/)
*  [Subway](https://www.subway.com/en-US/MenuNutrition/Nutrition/NutritionGrid)
*  [Blimpie](https://www.blimpie.com/assets/BlimpieNutritionalInfo.pdf)
*  [Jimmy Johns](https://resources.jimmyjohns.com/downloadable-files/NutritionGuide.pdf)
*  [Panera](https://www-beta.panerabread.com/content/dam/panerabread/integrated-web-content/documents/Panera-Nutrition.pdf)
*  [Quiznos](https://www.quiznos.com/assets/images/NutritionalInfo.pdf)
*  [Choose My Plate](https://www.choosemyplate.gov/resources/physical-activity-calories-burn)
*  [NutriStrategy](https://www.nutristrategy.com/caloriesburned.htm)

#### Brief summary of the 3 ETL steps we will take to create this database:

We will be using Postgres since our collective data is all similar and we are not having different kinds of data.  Also, since we have specific information, we can also make sure to secure its type. 

#### ETL STEPS
1. Scrape the data for sandwiches for the chosen joints from https://fastfoodnutrition.org/
2. Collect all the required data
3. Create a [Quick DBD flow chart](https://github.com/Jen-Dean/for-now/blob/main/QuickDBD_Set_Up/QuickDBD_ScreenShot.png)
4. Merge all the collected data into postgres sql database
5. Create a comprehensive ReadMe File
6. Create sample queries

#### Team Roles

| Team Member           | Role                          | Github username |        
| -----------           | -----------                   | -----------
| Veena Uppalapati      | Panera transformer            | veenauppalapati |
| Josh Acampado         | Scraping from a dying company | josh-acampado   |
| Sherin Mattappallil   | Subway Scraper                | sherinmatt      |
| Jennifer Dean         | Jimmy Johns Jockey            | Jen-Dean        |
| Shamikasule           | Blimpie Best                  | shamikasule     |

## General info
How do Sandwhiches Shop items and nutritional information relate to one another?

## Screenshots
*coming soon*

## Technologies
* SQL
* Splinter
* Beautifulsoup
* Pandas
* Python
* PostgresSQL

## Database Organization
##### Database Relationship
![quickdbd](https://github.com/Jen-Dean/for-now/blob/main/QuickDBD_Set_Up/QuickDBD_ScreenShot.png)

## Extrapolations & Notes

### Customizations of Sandwhiches
- Every single sandwich chain offers a unlimited number of customizations for each sandwich.  For a cleaner database we decided to forgo customizations and stick with the main "as is" offerings.
- We did note the differences in bread types, as well as sandwhich lengths

### Jimmy Johns
#### Average of Nutrition Values Across Bread Types
- Due to the nature of the Jimmy Johns website, there only existed ranges of each nutritional value field (calories, protein, fat etc) rather then exact amounts per bread type (French, Stone-Wheat, Unwich).
- To finish the datatables we took the averages of all the options as found in the Jimmy Johns PDF Nutrition file and applied the increases to the base "Unwich" stats - which are always the lowsest value.
- Below is the table for the values

| Bread Type  | Total Fat  | Cholesterol  | Total Carbs | Dietary Fiber | Protein    |
| ----------  | ---------- | -----------  | ----------  | ------------  | ---------  |
| Unwich      | base Value | base Value   | base Value  | base Value    | base Value |
| French      | +2         | +0           | +65         | +4            | +13        |
| Stone-Wheat | +8         | +0           | +57         | +3            | +16        |

### Exercise
- [See our data here](https://github.com/Jen-Dean/for-now/blob/main/Exercise_Scrape/exercise.csv) on all the exercises queried for our database.  This data is based on 1 hour of activity as well as 4 different weights.  The data is also of an "average" human male.
- The amount of calories expended is influenced by many factors, including body weight, intensity of activity, conditioning level and metabolism.
##### Exercise Examples
![Exercise Examples](https://github.com/Jen-Dean/for-now/blob/main/Exercise_Scrape/Exercise_screenshot.png)
  
### Blimpie
- We initially planned on scraping data from the Blimpie website, but because of unforseeable reasons, we weren't able to collect that data.
- Therefore, we just focused on extracting data from Panera, Quiznos, Subway and Jimmy Johns. 

### Subway 
- During the extraction process, because of the large amounts of information and time constraints, ended up focusing only on extracting the Subway sandwich length: 6" data only, using Beautiful soup etc. 
- The intial subway dataframe, before transformation, just had the following nutrient values: calories, total_fat, trans_fat, cholestrol, total_carbohydrates, dietary fiber, protein. 
- During the transformation process, the dataframe was cleaned up. More columns were added to the dataframe. Then, the final table was exported to csv for the loading process.

### Panera
- Extracted data Panera website and tranformed the data as

### Quiznos
- Extracted data from the PDF through Tabula into CSV (Used tabula to pull the data from 21 sanwiches). Created a document with sandwich description. Viewed the CSV's in Excel to reformat the data. Later, rows were shifted to match data and delete blank rows. Lastly, loaded the multiple csvs to merge in Jupyter Notebook (merged 3 csv files into one dataframe).
- During the tranformation process, firstly, cleaned up the dataframe. Renamed columns, and dropped any rows containing "Half Salad" or "Full Salad". Then, the index was reset. Exported final table as CSV to lead with group. Lastly, combined all the Restaurant csvs for final load.

### Loading 
- In progress: 



## Code Examples
*coming soon*

## Features
*coming soon*

## Status
Project is: _in progress_

## Inspiration
Hunger, and Rutgers Data Science Bootcamp

## Contact
Created by Jennifer Dean, Shamika Sule, Josh Acampado, Veena Uppalapati, Sherin Mattappallil

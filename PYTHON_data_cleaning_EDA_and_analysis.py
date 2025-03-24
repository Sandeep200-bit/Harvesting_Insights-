
#project 


"Harvesting Insights: A 57-Year Odyssey of Indian -"
    
      " - Agriculture and Climate Interplay" 



---------->  MySQL sever connection to python .


------------------------------------------------------------------------------------------------


pip install pymysql sqlalchemy pandas

import pymysql
import pandas as pd

# MySQL connection details
connection = pymysql.connect(
    host="localhost",        
    user="root",             
    password="Sandeep@1234", 
    database="india_agricultural_datasets"  
)

# Fetch temperature data
temperature_query = "SELECT * FROM temperature"
temperature_data = pd.read_sql(temperature_query, connection)

# Fetch rainfall data
rainfall_query = "SELECT * FROM rainfall"
rainfall_data = pd.read_sql(rainfall_query, connection)

# Fetch combined crop data
crops_query = "SELECT * FROM crops_master"
crops_data = pd.read_sql(crops_query, connection)

# Close the connection
connection.close()

# Display the first few rows of each dataset
print("Temperature Data:")
print(temperature_data.head())

print("\nRainfall Data:")
print(rainfall_data.head())

print("\nCrops Data:")
print(crops_data.head())

temperature_data

rainfall_data

crops_data


--------------------------------------------------------------------------------------------------


>>>+------> Data Cleaning 



temperature_data

rainfall_data

crops_data
 

print(temperature_data.info())

print(rainfall_data.info())

print(crops_data.info())


print(temperature_data.isnull().sum())
print(rainfall_data.isnull().sum())
print(crops_data.isnull().sum())


temperature_data.fillna(0, inplace=True)
rainfall_data.fillna(0, inplace=True)
crops_data.fillna(0, inplace=True)


# Rename Columns for Consistency: Standardize column names to make analysis easier:

temperature_data.rename(columns={"YEAR": "Year", "ANNUAL": "Annual_Temp"}, inplace=True)
rainfall_data.rename(columns={"ï»¿YEAR": "Year", "ANN": "Annual_Rainfall"}, inplace=True)
crops_data.rename(columns={"Value": "Production_Value", "Item": "Crop_Name"}, inplace=True)


# Check for Outliers: Use boxplots to visualize outliers and decide on handling them:

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=temperature_data, x="Annual_Temp")
plt.show()

temperature_data

rainfall_data

crops_data
 

# Convert Data Types: Ensure the Year column is of type integer and other numerical columns are floats:

temperature_data["Year"] = temperature_data["Year"].astype(int)
rainfall_data["YEAR"] = rainfall_data["YEAR"].astype(int)
crops_data["Production_Value"] = crops_data["Production_Value"].astype(float)


 # i want to add an index column named "id_of_item" to the crops_data DataFrame

# Add an index column starting from 1
crops_data["id_of_item"] = range(1, len(crops_data) + 1)

# Move the index column to the front (optional)
cols = ["id_of_item"] + [col for col in crops_data.columns if col != "id_of_item"]
crops_data = crops_data[cols]

# Display the first few rows to verify
print(crops_data.head())



---------------------------------------------------------------------------------------------------------------------------------

  >>-----> Exploratory Data Analysis (EDA)
  
Once the datasets are cleaned, start the EDA to understand trends, patterns, and relationships.


--------------------------
EDA Steps for the Temperature Dataset

temperature_data

print(temperature_data.describe())

===========


Visualize Annual Temperature Trends: Plot temperature changes over time:

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(temperature_data["Year"], temperature_data["Annual_Temp"], marker="o", linestyle="-")
plt.title("Annual Temperature Trend (1961-2018)")
plt.xlabel("Year")
plt.ylabel("Annual Temperature (°C)")
plt.grid()
plt.show()

==============

Seasonal Temperature Analysis: Compare seasonal averages (Jan-Feb, Mar-May, etc.):

temperature_data[["JAN-FEB", "MAR-MAY", "JUN-SEP", "OCT-DEC"]].mean().plot(kind="bar")
plt.title("Average Seasonal Temperatures")
plt.ylabel("Temperature (°C)")
plt.show()


-------------------------------------

EDA Steps for the Rainfall Dataset

rainfall_data 


Summary Statistics:

print(rainfall_data.describe())


================

Visualize Annual Rainfall Trends:


plt.figure(figsize=(10, 5))
plt.plot(rainfall_data["Year"], rainfall_data["Annual_Rainfall"], marker="o", linestyle="-", color="blue")
plt.title("Annual Rainfall Trend (1961-2018)")
plt.xlabel("Year")
plt.ylabel("Annual Rainfall (mm)")
plt.grid()
plt.show()

================

Monthly Rainfall Distribution: Compare rainfall across all months:

monthly_columns = rainfall_data.columns[1:13]  # Monthly columns
rainfall_data[monthly_columns].mean().plot(kind="bar", color="skyblue")
plt.title("Average Monthly Rainfall")
plt.ylabel("Rainfall (mm)")
plt.show()
    
================

Correlation Between Seasonal and Annual Rainfall: Check relationships:
    
 print(rainfall_data.corr())
   

rainfall_corr = rainfall_data.corr()

rainfall_corr

# Define the index values
index_values = [
    "Year", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP",
    "OCT", "NOV", "DEC", "Annual_Rainfall", "Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec"
]

# Add the index column to the DataFrame
rainfall_corr["months_of_year"] = index_values

# Set the new column as the index
rainfall_corr.set_index("months_of_year", inplace=True)

# Display the updated DataFrame
print(rainfall_corr)


------------------------------------


EDA Steps for the Crops Dataset

crops_data

Summary Statistics:


print(crops_data.describe())


===================================

Top Crops by Production: Find and visualize crops with the highest production values:

top_crops = crops_data.groupby("Crop_Name")["Production_Value"].sum().sort_values(ascending=False).head(10)
top_crops.plot(kind="bar", color="green")
plt.title("Top 10 Crops by Total Production")
plt.ylabel("Production Value")
plt.show()


===================================

Production Trends Over Time: Visualize production trends for specific crops:
    
crop_trend = crops_data[crops_data["Crop_Name"] == "Sugar cane"]
plt.plot(crop_trend["Year"], crop_trend["Production_Value"], marker="o", linestyle="-")
plt.title("Sugar Cane Production Trend")
plt.xlabel("Year")
plt.ylabel("Production Value")
plt.show()

===================================

Combine Crops with Climate Data:
    Merge crops_data with temperature_data and rainfall_data on the Year column to analyze
    the effect of temperature and rainfall on production:

combined_climate_crops = pd.merge(crops_data, temperature_data, on="Year", how="inner")
combined_climate_crops = pd.merge(combined_climate_crops, rainfall_data, on="Year", how="inner")
print(combined_climate_crops.head())



# Rename the climate data columns for better understanding and uniqueness
combined_climate_crops.rename(columns={
    "JAN-FEB": "Temp_Jan_Feb",
    "MAR-MAY": "Temp_Mar_May",
    "JUN-SEP": "Temp_Jun_Sep",
    "OCT-DEC": "Temp_Oct_Dec",
    "JAN": "Rain_Jan",
    "FEB": "Rain_Feb",
    "MAR": "Rain_Mar",
    "APR": "Rain_Apr",
    "MAY": "Rain_May",
    "JUN": "Rain_Jun",
    "JUL": "Rain_Jul",
    "AUG": "Rain_Aug",
    "SEP": "Rain_Sep",
    "OCT": "Rain_Oct",
    "NOV": "Rain_Nov",
    "DEC": "Rain_Dec",
    "Jan-Feb": "Rain_Jan_Feb",
    "Mar-May": "Rain_Mar_May",
    "Jun-Sep": "Rain_Jun_Sep",
    "Oct-Dec": "Rain_Oct_Dec"
}, inplace=True)

# Display the first few rows to verify the changes
print(combined_climate_crops.head())




temperature_data

rainfall_data

crops_data
 







































































































































































































































































































































































































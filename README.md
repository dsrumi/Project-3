# Project-3
# Data Visualization Project To Analyze Flu Trends  by US States,Age Groups and Virus Types 

## Project Overview
This project aims to create an interactive data visualization application using 
Python, specifically with Dash and Plotly. This project will analyze and visualize 
influenza trends, mortality rates, state-wise activity levels, and virus type 
distributions using historical data. The project will help identify key patterns, 
anomalies, and correlations that could inform public health decision-making

## Data Source
[CDC FluView Interactive](https://www.cdc.gov/fluview/overview/fluview-interactive.html)


## Specificity the Data Accessed:
National, Regional, and State Level Outpatient Illness and Viral 
Surveillance Data

Age Group Distribution of Influenza Positive Tests Reported by 
Public Health Laboratories Data

Outpatient Respiratory Illness Activity Map 

Influenza Mortality Surveillance from the National Center for health Statistics Mortality Surveillance System data.

### Tools:
Python Libraries:

Pandas: For data manipulation and analysis.

Matplotlib: For creating static visualizations.

Plotly/Dash: For interactive visualizations and dashboards.

 ### Project Structure
1. Data is loaded from PostgreSQL using  SQL Alchemy and Pandas and cleaned.
2. Analysis is done to explore various trends and visualizations are created.
3. Dashboard is developedwith filters to view trends interactively.

### Ethical Considerations:
   In this project, ethical considerations were prioritized by ensuring proper acknowledgment of the CDC as the data source and adhering to its terms of use. The data, being aggregated and anonymized, was handled responsibly to prevent misuse or unintended identification when combined with other datasets. Measures were taken to securely store and process the data, ensuring accuracy and avoiding misrepresentation. Insights derived from the data were communicated transparently with a focus on benefiting public health. All analyses were conducted in compliance with legal, institutional, and CDC guidelines.

## Instructions to Use:
Run the app.py file in terminal or through VS code.The dash board will start running in a port.Hover over the figure to see the data displayed in pop ups.

To use the user input dashboard,enter the week in drop down menu for which you want to see the result and the result will be displayed as chloropleth map for that week.

<img width="1680" alt="Screenshot 2024-12-15 at 8 34 00 PM" src="https://github.com/user-attachments/assets/61473c28-a6b3-4a41-8af4-6732bfc0134b" />

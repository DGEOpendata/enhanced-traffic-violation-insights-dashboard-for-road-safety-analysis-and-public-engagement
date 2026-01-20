python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = 'Traffic_Fines_2022-2025.csv'
data = pd.read_csv(data_path)

# Data Preprocessing
# Convert year column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Aggregate data by year and ticket type
agg_data = data.groupby(['Year', 'Ticket_Type']).size().reset_index(name='Count')

# Create a heatmap of ticket types over the years
heatmap_data = agg_data.pivot('Ticket_Type', 'Year', 'Count')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Heatmap of Traffic Tickets by Year and Type')
plt.xlabel('Year')
plt.ylabel('Ticket Type')
plt.show()

# Trend Analysis
trend_data = data.groupby('Year').size().reset_index(name='Total_Tickets')
plt.figure(figsize=(10, 6))
plt.plot(trend_data['Year'], trend_data['Total_Tickets'], marker='o')
plt.title('Trend of Total Traffic Tickets Over Years')
plt.xlabel('Year')
plt.ylabel('Total Tickets')
plt.grid()
plt.show()

# Bar Chart for Most Frequent Violations
violation_counts = data['Ticket_Type'].value_counts().head(10)
plt.figure(figsize=(12, 6))
violation_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Frequent Traffic Violations')
plt.xlabel('Ticket Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

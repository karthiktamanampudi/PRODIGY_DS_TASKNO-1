import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# Path to the ZIP file
zip_file_path = '1st_task\API_SP.POP.TOTL_DS2_en_csv_v2_56.zip'

# Open and read the ZIP file programmatically
with zipfile.ZipFile(zip_file_path, 'r') as z:
    # Extract and read the main dataset directly from the ZIP
    with z.open('API_SP.POP.TOTL_DS2_en_csv_v2_56.csv') as file:
        population_data = pd.read_csv(file, skiprows=4)

# Step 1: Preprocess Data
# Filter relevant columns (Country Name and the most recent year, 2023)
population_2023 = population_data[['Country Name', '2023']].dropna()
population_2023 = population_2023.rename(columns={'Country Name': 'Country', '2023': 'Population'})

# Filter valid countries and drop rows with zero or NaN values
population_2023 = population_2023[population_2023['Population'] > 0]

# Step 2: Visualization 1 - Histogram for Population Distribution
plt.figure(figsize=(10, 6))
sns.histplot(population_2023['Population'], bins=30, kde=True, color='blue')
plt.title('Histogram of Population Distribution (2023)', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Step 3: Visualization 2 - Bar Chart for Top 10 Populated Countries
# Sort and take the top 10 most populated countries
top_10_countries = population_2023.sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(
    x='Population',
    y='Country',
    data=top_10_countries,
    palette='viridis'
)
plt.title('Top 10 Countries by Population (2023)', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

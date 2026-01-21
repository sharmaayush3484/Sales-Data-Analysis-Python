import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month


monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales: ", monthly_sales)

plt.bar(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.show()

grouped_frame = df.groupby('Category')
print("Sales and profit by Category: ",grouped_frame[['Sales', 'Profit']].mean())

print("Total Sales by Product: ", df.groupby('Product')['Sales'].sum())
print("Total Profit by Region: ", df.groupby('Region')['Profit'].sum())

print("Information of the DataFrame:", df.info())
print("Head of the DataFrame:", df.head())
print("Description of the DataFrame:", df.describe())
print("Columns in the DataFrame:", df.columns)
print("Shape of the DataFrame:", df.shape)
print("Data Types in the DataFrame:", df.dtypes)
print("Index of the DataFrame:", df.index)
print("Unique Categories:", df['Category'].unique())
print("Value Counts for Regions:", df['Region'].value_counts())
print("Correlation Matrix:", df.corr())
print("Missing Values in each column:", df.isnull().sum())
print("Sorted DataFrame by Sales:", df.sort_values(by='Sales', ascending=False).head())
